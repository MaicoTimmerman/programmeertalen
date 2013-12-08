%%
%
% Todo: Indexes are 1 off with the width.
%
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
    io:format("Spawned processes~n"),
    NewBoard = addLine(Board, 0,0,l),
    Player1_PID ! {NewBoard, {0,0}, Player2_PID}.

% Create the board with two arrays, one for horizontal and one for vertical edges.
createBoard(W,H) ->
    LinesX = array:new(H * (W + 1), {default,false}),
    LinesY = array:new(W * (H + 1), {default,false}),
    io:format("ArraySizeX: ~p~n",[(array:size(LinesX))]),
    io:format("ArraySizeY: ~p~n",[(array:size(LinesY))]),
    io:format("created board~n"),
    {W, H, LinesX, LinesY}.

% Add a line to square X,Y on the side(r,l,u,d) given.
addLine(Board, X, Y, Direction) ->
    {W, H, LinesX, LinesY} = Board,
    io:format("Added line: X = ~p, Y = ~p, Direction = ~p~n",[X,Y,Direction]),
    case Direction of
        r -> {W,H,array:set((X + 1) + ((W+1)*Y), true, LinesX),LinesY};
        l -> {W,H,array:set(X + ((W+1)*Y), true, LinesX),LinesY};
        u -> {W,H,LinesX,array:set(X + (W*Y), true, LinesY)};
        d -> {W,H,LinesX,array:set(X + (W*(Y+1)), true, LinesY)}
    end.

% Return a tupel of the edges in the format {u,r,d,l}
getEdges(Board, X, Y) ->
    {W, H, LinesX, LinesY} = Board,
    io:format("W: ~p~n",[W]),
    io:format("H: ~p~n",[H]),
    io:format("ArraySize Lines X: ~p~n",[(array:size(LinesX))]),
    io:format("ArraySize Lines Y: ~p~n",[(array:size(LinesY))]),
    % Formulas for accessing the array need to be changed.
    io:format("RightIndex is ~p~n",[((X + 1) + ((W+1)*Y))]),
    RightEdge = array:get((X + 1) + ((W+1)*Y), LinesY),
    io:format("LeftEdge Index is ~p~n",[(X + ((W+1)*Y))]),
    LeftEdge = array:get(X + ((W+1)*Y), LinesY),
    io:format("UpEdge Index is ~p~n",[(X + (W*Y))]),
    UpEdge = array:get(X + (W*Y), LinesX),
    io:format("DownEdge Index is ~p~n",[(X + (W*(Y+1)))]),
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
        {true, false, false, false} ->
            {{X, Y, r}, true};
        {false, true, false, false} ->
            {{X, Y, l}, true};
        {false, false, true, false} ->
            {{X, Y, u}, true};
        {false, false, false, true} ->
            {{X, Y, d}, true};
        _ ->
            case {X,Y} of
                {0,0} ->
                    randomNextMove(Board, W-1, H-1);
                {0,_} ->
                    checkNextMove(Board, W, Y-1);
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
        _ ->
            case {X,Y} of
                {0,0} ->
                    {{-1,-1, finished}, false};
                {0,_} ->
                    randomNextMove(Board, W, Y-1);
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
            {NextMove, Scored} = checkNextMove(Board, W, H),
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
            io:format("Thanks for playing!",[])
    end.
