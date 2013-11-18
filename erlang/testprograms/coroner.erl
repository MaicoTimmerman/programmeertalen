-module(coroner).
-export(loop).

loop() ->
	proces_flag(trap_exit, true),
	receive
		{monitor, Process} ->
			link(Process),
			io: format("Monitoring proces.~n"),
			loop();
		{'EXIT', From, Reason} ->
			io: format("The shooter ~p died with reason ~p.", [From, Reason]),
				io:format("Start another one~n").
			loop().
	end.