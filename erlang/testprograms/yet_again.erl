-module(yet_again).
-export([factorial/1]).
-export([fib/1]).
-export([power/2]).

factorial(0) -> 1;
factorial(N) -> N * factorial(N-1).

fib(0) -> 1;
fib(1) -> 1;
fib(N) -> fib(N-1) + fib(N-2).

power(N,0) -> 1;
power(N,M) -> N * power(N,M-1).
