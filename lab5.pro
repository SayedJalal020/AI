:- dynamic(environment/1).
:- dynamic(job/1).
:- dynamic(feedback/1).
:- dynamic(stimulus_situation/1).
:- dynamic(stimulus_response/1).

ask(Attribute) :-
    write('Enter the value for '),
    write(Attribute),
    write(': '),
    read(Value),
    nl,
    Term =.. [Attribute, Value],
    assert(Term).

get_environment :-
    ( environment(_) -> true ; ask(environment), get_environment ).

get_job :-
    ( job(_) -> true ; ask(job), get_job ).

get_feedback :-
    ( feedback(_) -> true ; ask(feedback), get_feedback ).

stimulus_situation(verbal) :-
    environment(papers) ; environment(manuals) ; environment(documents) ; environment(textbooks).

stimulus_situation(visual) :-
    environment(pictures) ; environment(illustrations) ; environment(photographs) ; environment(diagrams).

stimulus_situation(physical_object) :-
    environment(machines) ; environment(buildings) ; environment(tools).

stimulus_situation(symbolic) :-
    environment(numbers) ; environment(formulas) ; environment(computer_programs).

stimulus_response(oral) :-
    job(lecture) ; job(advising) ; job(counselling).

stimulus_response(hands_on) :-
    job(building) ; job(repairing) ; job(troubleshooting).

stimulus_response(documented) :-
    job(writing) ; job(typing) ; job(drawing).

stimulus_response(analytical) :-
    job(evaluating) ; job(reasoning) ; job(investigating).

medium(workshop) :-
    stimulus_situation(physical_object),
    stimulus_response(hands_on),
    feedback(required).

medium(lecture) :-
    (stimulus_situation(visual), stimulus_response(analytical), feedback(required));
    (stimulus_situation(visual), stimulus_response(oral), feedback(required));
    (stimulus_situation(verbal), stimulus_response(analytical), feedback(required)).

medium(videocassette) :-
    stimulus_situation(visual),
    stimulus_response(documented),
    feedback(not_required).

medium(role_play) :-
    stimulus_situation(verbal),
    stimulus_response(oral),
    feedback(required).

recommend :-
    get_environment,
    get_job,
    get_feedback,
    ( medium(M) -> write('Recommended training medium: '), write(M), nl ; write('No matching training medium found.'), nl ).

