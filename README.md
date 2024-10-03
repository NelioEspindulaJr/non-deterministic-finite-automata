# non-deterministic-finite-automata
 Convert a NFA (Non-deterministic Finite Automaton) to a DFA (Deterministic Finite Automata) 

### How to run?
Before running the project, make sure you have python installed with any stable version greater than 3.8.x. Next step, run the following command:

```
pip install -r requirements.txt
```

Now, in the terminal, execute:

```
python main.py
```

> It is imprecedent that you already have your automaton and words list to be tested typed and saved inside the root folder of the project, following the rules specified in task assignment.

Now, it will be asked for you to input the file name of the NFA:

```bash
~/non-deterministic-finite-automata$ python main.py 
Enter the file name inside this directory: 
```

After that, will be printed the DFA table with lambda closure and saved a new file called: `nfaInputedFileName_dfa.txt` with the DFA initial and final states and transitions. Also will be asked a new input of the file name of the words to be tested in this automaton.


Example:
```bash
Transitions table: closure-λ(Q1) = {Q0Q1Q2Q4}

                      a           b        c       
Q0Q1Q2Q4  [Q0,Q1,Q2,Q4]  [Q0,Q2,Q4]  [Q0,Q4] 
Q0Q2Q4    [Q4]           [Q0,Q2,Q4]  [Q0,Q4] 
Q4        [Q4]           [-]         [-]     
Q0Q4      [Q4]           [-]         [Q0,Q4]

Enter the file name containing the words to be verified by the DFA: 
```

After that will be printed all the words and say if is accepted or not by the DFA, and saved a new file called `wordsInputFileName_accepted.txt` with the results (accepted or not).