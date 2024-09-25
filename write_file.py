import os
from typing import Dict, List


def write_dfa_file(new_states, initial_closure, final_states, input_filename):
    output_filename = os.path.splitext(input_filename)[0] + "_dfa.txt"

    all_states = list(new_states.keys())

    initial_state = "".join(initial_closure)

    dfa_final_states = [
        state for state in all_states if any(f in state for f in final_states)
    ]

    with open(output_filename, "w") as file:
        file.write(" ".join(all_states) + "\n")

        file.write(initial_state + "\n")

        file.write(" ".join(dfa_final_states) + "\n")

        for state, transitions in new_states.items():
            for letter, destination in transitions.items():
                if destination[0] != "-":
                    file.write(f"{state} {letter} {''.join(destination)}\n")

    return initial_state, output_filename, dfa_final_states, all_states


def write_accepted_words_file(
    dfa_states: Dict[str, Dict[str, List[str]]],
    initial_dfa_state: str,
    words: List[str],
    words_file_name: str,
):
    output_words_file_name = os.path.splitext(words_file_name)[0] + "_accepted.txt"

    with open(output_words_file_name, "w") as words_file:
        for word in words:
            current_state = initial_dfa_state
            accepted = True  # Para verificar se a palavra foi aceita ou não

            for char in word:
                # Verifica se o estado atual e o caractere possuem uma transição
                next_state = dfa_states.get(current_state, {}).get(char)

                if not next_state:
                    print(f"Word {word} is not accepted by the automaton.")
                    words_file.write(f"{word} -> não aceito\n")
                    accepted = False
                    break

                # Atualiza o estado atual para o próximo estado
                current_state = "".join(next_state)

            if accepted:
                words_file.write(f"{word} -> aceito\n")
                print(f"Word {word} is accepted by the automaton.")
