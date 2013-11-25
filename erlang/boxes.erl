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
    % do something.
    Board = digraph:new(),
    add_init_vertices(49, Board),
    erlang:register(player1, spawn(boxes, player, [])),
    erlang:register(player2, spawn(boxes, player, [])),
    dnb(60,[0,0],Board,player1),
    player(Board).

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

% create board and manage fields.
dnb(0,Score,_,_) -> 
    io:format('Game ended, final score:~n'),
    io:format('Player 1 score: ~p, Player 2 score: ~p',Score);

dnb(X,Score,Board, Player) ->
    %do something
    io:format('test'),
    if
        Player == player1 -> NextPlayer = player2;
        Player == player2 -> NextPlayer = player1
    end,
    Player ! turn,
    receive

    dnb(X-1, NewScore, NewBoard,NextPlayer). 


player(Board) ->
    % manage player AI.
    io:format('test~n'),
    digraph:vertices(Board).
