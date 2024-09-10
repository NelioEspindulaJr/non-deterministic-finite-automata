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

    return lambda_closure


def search_closure(
    transitions: List[Tuple[str, str, str]],
    initial_state: str,
    alphabet_value: str,
    closure: List[str] = None,
):
    if closure is None:
        closure = []

    state_transitions = [
        x
        for x in transitions
        if x[0] == initial_state and (x[1] in ["λ", alphabet_value])
    ]

    for transition in state_transitions:
        if transition[1] == "λ":
            if transition[2] not in closure:
                closure.append(transition[2])
            search_closure(transitions, transition[2], alphabet_value, closure)
        else:
            if transition[2] not in closure:
                closure.append(transition[2])

    return closure
