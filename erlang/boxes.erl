% Name: Maico Timmerman
% Num:  10542590
%
% boxes.erl:
%   This program contains two player who play the dots and boxes game.
%   The program will run until the board is complete filled.
%   When there is a box with 3 sides drawn the AI will always take the point,
%   else it will put a random line on the board where there is none.
-module(boxes).
-export([init/2, player/0]).


% Initialize the board and startup two players which start communicating
% until the game is completed.
init(W, H) ->
    Board = createBoard(W,H),
    Player1_PID = spawn(boxes, player, []),
    Player2_PID = spawn(boxes, player, []),
    Player1_PID ! {Board, {0,0}, Player2_PID}.

% Create the board with two arrays, one for horizontal and one for vertical edges.
createBoard(W,H) ->
    LinesY = array:new(H * (W + 1), {default,false}),
    LinesX = array:new(W * (H + 1), {default,false}),
    {W, H, LinesX, LinesY}.

% Add a line to square X,Y on the side(r,l,u,d) given.
% Prints the line added by a player.
addLine(Board, X, Y, Direction, Player) ->
    {W, H, LinesX, LinesY} = Board,
    io:format("Player ~p added line: X = ~p, Y = ~p, Direction = ~p~n",[Player,X,Y,Direction]),
    case Direction of
        r -> {W,H,LinesX,array:set((X + 1) + (W*Y), true, LinesY)};
        l -> {W,H,LinesX,array:set(X + (W*Y), true, LinesY)};
        u -> {W,H,array:set(X + (W*Y), true, LinesX),LinesY};
        d -> {W,H,array:set(X + (W*(Y+1)), true, LinesX),LinesY}
    end.

% Return a tupel of the edges in the format {r,l,u,d}
getEdges(Board, X, Y) ->
    {W, _, LinesX, LinesY} = Board,
    RightEdge = array:get((X + 1) + (W*Y), LinesY),
    LeftEdge = array:get(X + (W*Y), LinesY),
    UpEdge = array:get(X + (W*Y), LinesX),
    DownEdge = array:get(X + (W*(Y+1)), LinesX),
    {RightEdge, LeftEdge, UpEdge, DownEdge}.

% Swaps the score to send to the next player and adds 1 point to score if Scored is true.
getNewScore(Score, Scored) ->
    {OtherPlayerScore, ThisPlayerScore} = Score,
    case Scored of
        true ->
            {ThisPlayerScore + 1, OtherPlayerScore};
        _ ->
            {ThisPlayerScore, OtherPlayerScore}
    end.

% Checks all squares on the board for a non-filled square.
% Returns false if there is space left, true if board is filled.
checkBoardFull(Board, X, Y) ->
    {W, _, _, _} = Board,
    case getEdges(Board, X, Y) of
        {true,true,true,true} ->
            case {X,Y} of
                {0,0} ->
                    true;
                {0,_} ->
                    checkBoardFull(Board, W-1, Y-1);
                {_,_} ->
                    checkBoardFull(Board, X-1, Y)
            end;
        {_,_,_,_} ->
            false
    end.

% Returns the first square found with grade 3. else it will return a random next move.
% If a square with grade 3 is given, scored is true, else false.
checkNextMove(Board, X, Y) ->
    {W, H, _, _} = Board,
    case checkBoardFull(Board, W-1, H-1) of
        false ->
            case getEdges(Board, X, Y) of
                {false, true, true, true} ->
                    {{X, Y, r}, true};
                {true, false, true, true} ->
                    {{X, Y, l}, true};
                {true, true, false, true} ->
                    {{X, Y, u}, true};
                {true, true, true, false} ->
                    {{X, Y, d}, true};
                _ ->
                    case {X,Y} of
                        {0,0} ->
                            randomNextMove(Board);
                        {0,_} ->
                            checkNextMove(Board, W-1, Y-1);
                        {_,_} ->
                            checkNextMove(Board, X-1, Y)
                    end
            end;
        true ->
            {{-1,-1, finished}, false}
    end.

% Find a random non-filled square.
randomNextMove(Board) ->
    {W, H, _, _} = Board,
    % Set a random seed based on the current system time.
    {A1,A2,A3} = now(),
    random:seed(A1,A2,A3),
    X = random:uniform(W) - 1,
    Y = random:uniform(H) - 1,
    % Check if edge has empty side, then fill it, else generate next square.
    case getEdges(Board, X, Y) of
        {false, _, _, _} ->
            {{X, Y, r}, false};
        {_, false, _, _} ->
            {{X, Y, l}, false};
        {_, _, false, _} ->
            {{X, Y, u}, false};
        {_, _, _, false} ->
            {{X, Y, d}, false};
        {true,true,true,true} ->
            randomNextMove(Board)
    end.


% Process of a player. Waits for turn message with new state of the game.
% Checks his next move, if no more moves send other player atom(finished),
% else send the other player the new state of the game.
player() ->
    receive
        {Board, Score, OtherPlayerPID} ->
            {W, H, _, _} = Board,
            {OtherPlayerScore, ThisPlayerScore} = Score,
            {NextMove, Scored} = checkNextMove(Board, W-1, H-1),
            {X, Y, Direction} = NextMove,
            case Direction of
                % When finished print scores and winning player.
                finished ->
                    io:format("Game finished!~n", []),
                    io:format("Final Score:~nPlayer A: ~p, Player B: ~p~n", [OtherPlayerScore, ThisPlayerScore]),
                    case OtherPlayerScore > ThisPlayerScore of
                        true ->
                            io:format("Player A won with ~p points~n",[OtherPlayerScore]);
                        false ->
                            case OtherPlayerScore == ThisPlayerScore of
                                true ->
                                    io:format("Its a draw! Both players had: ~p points~n",[OtherPlayerScore]);
                                false ->
                                    io:format("Player B won with ~p points~n",[ThisPlayerScore])
                            end
                    end,
                    OtherPlayerPID ! finished;
                % Players move on his turn.
                _ ->
                    NewBoard = addLine(Board, X, Y, Direction, self()),
                    NewScore = getNewScore(Score, Scored),
                    OtherPlayerPID ! {NewBoard, NewScore, self()},
                    player()
            end;
        finished ->
            io:format("Thanks for playing!~n",[])
    end.
