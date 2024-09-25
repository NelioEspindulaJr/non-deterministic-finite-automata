import pandas as pd

from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

from read_file import read_file, read_words
from write_file import write_dfa_file, write_accepted_words_file
from utils import fetch_lambda_closure, closure_finder, get_closure_key

# Função para escrever o resultado no arquivo de saída
def write_results(output_file_name, results):
    with open(output_file_name, 'w') as file:
        for word, result in results:
            file.write(f"{word} -> {result}\n")

states, initial_state, final_states, transitions, alphabet, file_name = read_file()

lambda_closure = []

fetch_lambda_closure(transitions, initial_state, lambda_closure)

new_states = {}

new_states[get_closure_key(lambda_closure)] = {}

closure_finder(lambda_closure, transitions, alphabet, new_states)

df = pd.DataFrame(new_states).transpose()

print(f"\nTransitions table: closure-λ({initial_state}) = {'{'}{"".join(lambda_closure)}{'}'}\n\n", df)

new_initial_state, output_file_name, new_final_states, new_states = write_dfa_file(new_states, lambda_closure, final_states, file_name)

words, words_file_name = read_words()

write_accepted_words_file(new_states, new_initial_state, words, words_file_name)

def plot_dfa():
    dfa = DFA(

    )
