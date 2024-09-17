import pandas as pd

from read_file import read_file
from write_file import write_dfa_file
from utils import fetch_lambda_closure, closure_finder, get_closure_key

states, initial_state, final_states, transitions, alphabet, file_name = read_file()

lambda_closure = []

fetch_lambda_closure(transitions, initial_state, lambda_closure)

new_states = {}

new_states[get_closure_key(lambda_closure)] = {}

closure_finder(lambda_closure, transitions, alphabet, new_states)

df = pd.DataFrame(new_states).transpose()

print(f"\nTransitions table:\closure-λ({initial_state}) = {'{'}{"".join(lambda_closure)}{'}'}\n\n", df)

output_file_name = write_dfa_file(new_states, lambda_closure, final_states, file_name)