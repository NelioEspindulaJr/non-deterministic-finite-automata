from typing import List, Tuple


def is_non_deterministic(transitions: List[Tuple[str, str, str]]) -> bool:
    """How this function works:
        Knowing that a dictionary accepts only unique keys, we can use this property
        to check if a transition is non-deterministic. By receiveing all transitions
        as a list of tuples, we can iterate over them and check if the current state
        and input character are already in the dictionary. If they are, we return True,
        otherwise we add the current state and input character to the dictionary and
        move on to the next transition. If we reach the end of the list of transitions,
        we return False, meaning that the automaton is deterministic.

    Args:
        transitions (List[Tuple[str, str, str]]): A list of tuples representing the
        transitions of an automaton.

    Returns:
        bool: True if the automaton is non-deterministic, False otherwise.
    """
    transition_map = {}

    for current_state, input_char, next_state in transitions:

        if input_char == "h" or input_char == "λ":
            return True

        if (current_state, input_char) in transition_map:
            return True

        transition_map[(current_state, input_char)] = next_state

    return False


def fetch_lambda_closure(
    transitions: List[Tuple[str, str, str]],
    initial_state: str,
    lambda_closure: List[str] = None,
):
    """Calculates the lambda closure (ε-closure) of a given state in a Non-Deterministic Finite Automaton (NFA).

       The lambda closure of a state is the set of states reachable from the given state via λ (epsilon) transitions,
       where ε transitions are transitions that occur without consuming any input symbol. This function recursively
       determines all states reachable by ε transitions and accumulates them in the closure set.

    Args:
        transitions (List[Tuple[str, str, str]]): A list of tuples representing the transitions of the NFA,
            where each tuple contains (current state, input symbol, next state).
        initial_state (str): The state for which the λ-closure is to be computed.
        lambda_closure (List[str], optional): Accumulator list for storing the states in the λ-closure.
            If not provided, a new list will be initialized.

    Returns:
        List[str]: A list of states representing the λ-closure of the given state, including the initial state.
    """
    if lambda_closure is None:
        lambda_closure = []

    if initial_state not in lambda_closure:
        lambda_closure.append(initial_state)

    lambda_transitions = [
        x for x in transitions if x[0] == initial_state and (x[1] == "λ" or x[1] == "h")
    ]

    for transition in lambda_transitions:
        next_state = transition[2]
        if next_state not in lambda_closure:
            fetch_lambda_closure(transitions, next_state, lambda_closure)

    lambda_closure.sort()

    return lambda_closure

def get_closure_key(closure: List[str]):
    return "".join(closure)

def closure_finder(
    closure: List[str],
    transitions: List[Tuple[str, str, str]],
    alphabet: List[str],
    states_dictionary: dict[str, dict[str, List[str]]],
) -> dict[str, dict[str, List[str]]]:
    """
    Recursively computes the closure of states in a non-deterministic finite automaton (NFA) and
    constructs the deterministic finite automaton (DFA) transition table.

    Args:
        closure (list): The current closure of states to be expanded.
        transitions (list of tuples): A list of tuples representing transitions of the NFA.
                                      Each tuple is of the form (current_state, symbol, next_state).
        alphabet (list): The list of input symbols (excluding lambda transitions) in the automaton.
        states_dictionary (dict): The dictionary representing the DFA transition table being built.
                                  Keys are concatenated strings of states, and values are dictionaries
                                  mapping symbols to the next state closure.

    Returns:
        dict: The updated DFA transition table as a dictionary with state closures as keys and their
              respective transitions as values.

    This function performs the following steps:
    1. Iterates over each input symbol in the alphabet.
    2. Finds all possible transitions for each symbol from the current set of states.
    3. Expands the current state closure by recursively including any lambda transitions.
    4. Updates the transition table (`states_dictionary`) for each state based on the computed closure.
    5. Recursively calls `closure_finder` on newly discovered closures to explore further transitions.
    6. Handles cases where no transition is found by assigning an empty transition ("-").

    Notes:
    - The function modifies `states_dictionary` in place, which holds the DFA state transition table.
    - The function ensures that newly computed closures are sorted to maintain consistent state keys.
    - Recursion continues until all reachable state closures have been processed.
    """
    current_closure = closure

    for letter in alphabet:
        new_state_closure = []

        for state in current_closure:
            letter_state_transitions = [
                x for x in transitions if x[0] == state and x[1] == letter
            ]

            for transition in letter_state_transitions:
                next_state = transition[2]
                if next_state not in new_state_closure:
                    new_state_closure.append(next_state)

                lambda_closure = fetch_lambda_closure(transitions, next_state)
                for closure_state in lambda_closure:
                    if closure_state not in new_state_closure:
                        new_state_closure.append(closure_state)

        new_state_closure.sort()

        if new_state_closure:
            closure_key = get_closure_key(current_closure)
            new_closure_key = get_closure_key(new_state_closure)

            if closure_key not in states_dictionary:
                states_dictionary[closure_key] = {}

            if letter not in states_dictionary[closure_key]:
                states_dictionary[closure_key][letter] = new_state_closure

            if new_closure_key not in states_dictionary:
                states_dictionary[new_closure_key] = {}
                closure_finder(
                    new_state_closure, transitions, alphabet, states_dictionary
                )
        else:
            new_state_closure = ["-"]
            closure_key = get_closure_key(current_closure)
            new_closure_key = get_closure_key(new_state_closure)

            if letter not in states_dictionary[closure_key]:
                states_dictionary[closure_key][letter] = new_state_closure

    return states_dictionary

