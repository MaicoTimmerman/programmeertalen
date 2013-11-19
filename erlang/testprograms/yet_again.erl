-module(yet_again).
-export([another_factorial/1]).
-export([another_fib/1]).
-export([power/2]).

another_factorial(0) -> 1;
another_factorial(N) -> N * another_factorial(N-1).

another_fib(0) -> 1;
another_fib(1) -> 1;
another_fib(N) -> another_fib(N-1) + another_fib(N-2).

power(N,0) -> 1;
power(N,1) -> N;
power(N,M) -> N * power(N,M-1).
