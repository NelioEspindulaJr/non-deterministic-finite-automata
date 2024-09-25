import sys

from utils import is_non_deterministic


def read_file(file_name: str = "", get_deterministic: bool = False):
    file = None
    states = []
    initial_state = None
    final_states = []
    transitions = []
    alphabet = []
    file_name = file_name

    while file is None:
        if not file_name:
            file_name = input("Enter the file name inside this directory: ")

        try:
            with open(file_name, "rt") as search_file:
                lines = search_file.readlines()

                if len(lines) < 4:
                    print("File is not formatted correctly. Please try again.")
                    break
                else:
                    states = lines[0].strip().split()
                    initial_state = lines[1].strip()
                    final_states = lines[2].strip().split()

                    for index, line in enumerate(lines[3:], start=3):
                        transition_parts = line.strip().split()

                        if len(transition_parts) != 3:
                            print(
                                f"Transition it's not properly inserted on line number {index + 1}. Please correct it and try again"
                            )
                            sys.exit()
                        else:
                            current_state, input_char, next_state = transition_parts
                            if input_char == "h":
                                input_char = "λ"
                            else:
                                alphabet.append(input_char)
                            transitions.append((current_state, input_char, next_state))
                    if not get_deterministic and not is_non_deterministic(transitions):
                        print(
                            "Oops! It seems that this automaton is deterministic. Try another one."
                        )
                        sys.exit()
        except FileNotFoundError:
            file_name = ""
            print("File not found. Please try again.")
        else:
            return states, initial_state, final_states, transitions, alphabet, file_name


def read_words():
    file = None
    file_name = ""
    words = []

    while file is None:
        if not file_name:
            file_name = input(
                "Enter the file name containing the words to be verified by the DFA: "
            )

        try:
            with open(file_name, "rt") as file:
                words = file.read().splitlines()
        except FileNotFoundError:
            file_name = ""
            print("File not found. Please try again.")
        else:
            return words, file_name
