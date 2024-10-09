import pandas as pd

from read_file import read_file, read_words
from write_file import write_dfa_file, write_accepted_words_file
from utils import fetch_lambda_closure, closure_finder, get_closure_key

states, initial_state, final_states, transitions, alphabet, file_name = read_file()

lambda_closure = []

fetch_lambda_closure(transitions, initial_state, lambda_closure)

new_states_dict = {}

new_states_dict[get_closure_key(lambda_closure)] = {}

closure_finder(lambda_closure, transitions, alphabet, new_states_dict)

df = pd.DataFrame(new_states_dict).transpose()

print(f"\nTransitions table: closure-λ({initial_state}) = {'{'}{"".join(lambda_closure)}{'}'}\n", df)

new_initial_state, output_file_name, new_final_states, new_states = write_dfa_file(new_states_dict, lambda_closure, final_states, file_name)

words, words_file_name = read_words()

write_accepted_words_file(new_states_dict, new_initial_state, new_final_states, words, words_file_name,)
