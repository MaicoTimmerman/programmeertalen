%%
%   Maico Timmerman
%   Informatica
%   10542590
%
%   Boxes.erl
%       This program implements the game boxes and dots. A game where 2 players can place
%       corners to a grid of squares. The goal is to complete more boxes then your opponent.
%%
-module(boxes).
-export([init/0]).

init() ->
    Board = digraph:new(),
    add_init_vertices(49, Board),
    erlang:register(player1, spawn(boxes, player, [])),
    erlang:register(player2, spawn(boxes, player, [])),
    dnb(60,[0,0],Board,player1).

% Add the last recursive vertex.
add_init_vertices(1, Board) ->
    digraph:add_vertex(Board);

% Add the vertexes recusively. Every vertex counts as a box in the game.
add_init_vertices(X, Board) ->
    digraph:add_vertex(Board),
    add_init_vertices(X-1,Board).

% Add an edge between 2 specified vertices, return atom failed if unsuccesful
% else create the edge.
add_line(Board, P1, P2) ->
    digraph:add_edge(Board, ['$v'| P1], ['$v' | P2]).

% Test the grade of a box, 3 means almost full, 4 means full.
test_squaregrade(0, Board) ->
    digraph:out_degree(Board, ['$v' | 0]) + digraph:out_degree(Board, ['$v' | 0]);

test_squaregrade(X, Board) ->
    digraph:out_degree(Board, ['$v' | X]) + digraph:out_degree(Board, ['$v' | X]).

% Start the boxes and dots game. Send the current player the message that he can make his move
% and wait for the result of the move.
% Called recusively till the game runs out of moves.
dnb(0,Score,_,_) ->
    % Game ended and prints score for the current round.
    io:format('Game ended, final score:~n'),
    io:format('Player 1 score: ~p, Player 2 score: ~p',Score);

dnb(X,Score,Board, Player) ->
    % Game ongoing and calls dnb() with 1 less turn to go.
    if
        Player == player1 -> NextPlayer = player2;
        Player == player2 -> NextPlayer = player1
    end,
    Player ! {Score, Board},
    receive
        {NewScore,NewBoard} ->
            dnb(X-1, NewScore, NewBoard,NextPlayer)
    end.


player() ->
    receive
        {Score, Board} ->
            % TODO: Finish player AI.
            player()
    end.
