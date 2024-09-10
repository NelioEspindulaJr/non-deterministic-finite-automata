import pandas as pd

from read_file import read_file
from utils import fetch_lambda_closure, search_closure

states, initial_state, final_states, transitions, alphabet = read_file()

lambda_closure = []

fetch_lambda_closure(transitions, initial_state, lambda_closure)

print(lambda_closure)  # automaton3.txt -> ['Q0', 'Q1', 'Q2', 'Q3', 'Q4']

new_states = {}
current_state_closure = lambda_closure
current_index = "".join(sorted(current_state_closure))

# first loop of the above for
#   new_states = {'Q0Q1Q2Q3Q4': }

for value in alphabet:
    temp_closure = []

    if current_index not in new_states:
        new_states[current_index] = []

    for state in current_state_closure:
        for temp_state in search_closure(transitions, state, value):
            if temp_state not in temp_closure:
                temp_closure.append(
                    temp_state
                )  # DEBUGAR PRA ENTENDER PQ OS VALORES NAO ESTAO SENDO
                # ADICIONADOS CORRETAMENTE NO ARRAY DO ESTADO CRIADO
        print(state, "->", value, "-> current: ", current_state_closure)

    current_state_closure = temp_closure

    current_index = "".join(sorted(current_state_closure))

    new_states[current_index] = current_state_closure

    print("new: ", current_state_closure)

print("\n", new_states)
#   pd.DataFrame(data=new_states, index)
#
