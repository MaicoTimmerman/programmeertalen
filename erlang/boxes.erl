%%
%
% Name: Maico Timmerman
% Num:  10542590
%
% boxes.erl:
%   This program contains two player who play the dots and boxes game.
%   The program will run until the board is complete filled.
%
%%
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
addLine(Board, X, Y, Direction) ->
    {W, H, LinesX, LinesY} = Board,
    io:format("Added line: X = ~p, Y = ~p, Direction = ~p~n",[X,Y,Direction]),
    case Direction of
        r -> {W,H,LinesX,array:set((X + 1) + (W*Y), true, LinesY)};
        l -> {W,H,LinesX,array:set(X + (W*Y), true, LinesY)};
        u -> {W,H,array:set(X + (W*Y), true, LinesX),LinesY};
        d -> {W,H,array:set(X + (W*(Y+1)), true, LinesX),LinesY}
    end.

% Return a tupel of the edges in the format {u,r,d,l}
getEdges(Board, X, Y) ->
    {W, H, LinesX, LinesY} = Board,
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

% returns the first square found with grade 3.
checkNextMove(Board, X, Y) ->
    {W, H, _, _} = Board,
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
                    randomNextMove(Board, W-1, H-1);
                {0,_} ->
                    checkNextMove(Board, W-1, Y-1);
                {_,_} ->
                    checkNextMove(Board, X-1, Y)
            end
    end.

% find a random non-filled square.
randomNextMove(Board, X, Y) ->
    {W, _, _, _} = Board,
    case getEdges(Board, X, Y) of
        {false, _, _, _} ->
            {{X, Y, r}, false};
        {_, false, _, _} ->
            {{X, Y, l}, false};
        {_, _, false, _} ->
            {{X, Y, u}, false};
        {_, _, _, false} ->
            {{X, Y, d}, false};
        {true, true, true, true} ->
            case {X,Y} of
                {0,0} ->
                    {{-1,-1, finished}, false};
                {0,_} ->
                    randomNextMove(Board, W-1, Y-1);
                {_,_} ->
                    randomNextMove(Board, X-1, Y)
            end
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
                finished ->
                    io:format("Game finished~n", []),
                    io:format("Final Score: Player A: ~p, Player B: ~p~n", [OtherPlayerScore, ThisPlayerScore]),
                    OtherPlayerPID ! finished;
                _ ->
                    NewBoard = addLine(Board, X, Y, Direction),
                    NewScore = getNewScore(Score, Scored),
                    OtherPlayerPID ! {NewBoard, NewScore, self()},
                    player()
            end;
        finished ->
            io:format("Thanks for playing!~n",[])
    end.
