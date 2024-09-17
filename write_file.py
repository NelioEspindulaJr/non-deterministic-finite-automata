import os


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

    return output_filename

