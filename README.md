# non-deterministic-finite-automata
 Convert a NFA (Non-deterministic Finite Automaton) to a DFA (Deterministic Finite Automata) 

### Partial results until now: 10/09/2024 - 04:19am

Currently being capable of getting λ-closure states recursively, and generating the DFA super states. Using the following NFA:

![alt text](/assets/image.png)

WHAT MY CODE GENERATES:
```json
{
  "Q0Q1Q2Q4": [
    "Q1",
    "Q2",
    "Q0",
    "Q4"
  ],
  "Q0Q2Q4": [
    "Q2",
    "Q0",
    "Q4"
  ],
  "Q0Q4": [
    "Q0",
    "Q4"
  ],
  "Q4": [
    "Q4"
  ]
}
 ```

 WHAT SHOULD GENERATE:

 ```json
{
  "Q0Q1Q2Q4": [
    "Q0Q1Q2Q4",
    "Q0Q2Q4",
    "Q0Q4"
  ],
  "Q0Q2Q4": [
    "Q4",
    "Q0Q2Q4",
    "Q0Q4"
  ],
  "Q0Q4": [
    "Q4",
    "Ø",
    "Q0Q4"
  ],
  "Q4": [
    "Q4",
    "Ø",
    "Ø"
  ]
}
 ```

Is still very raw, but im going to improve on performance and optimizations later, my major priority now is to get the code working.

> Some references that helped me:
> * https://web.stanford.edu/class/archive/cs/cs103/cs103.1202/notes/Guide%20to%20the%20Subset%20Construction.pdf
>
>* https://github.com/Rahul-Jyoti/NFA-TO-DFA-CONVERSION/tree/master
>
>* ChatGPT ;)

### Partial results until now: 17/09/2024 - 02:42am

So far i have made very good advancements on code, with almost finishing half of the task assignment (part one). Only (all of part 2 ) remains to be completed.

![alt text](/assets/image.png)

input_file.txt:
```
Q1 Q2 Q0 Q4
Q1
Q1 Q2 Q0 Q4
Q1 a Q1
Q1 h Q2
Q2 b Q2
Q2 h Q0
Q0 c Q0
Q0 h Q4
Q4 a Q4
```
For now, i can convert any NFA to DFA, which prints me this:

Transitions table: \
closure-λ(Q1) = {Q0Q1Q2Q4}
> 
> |          | a             | b          | c       |
> |----------|---------------|------------|---------|
> | Q0Q1Q2Q4 | [Q0,Q1,Q2,Q4] | [Q0,Q2,Q4] | [Q0,Q4] |
> | Q0Q2Q4   | [Q4]          | [Q0,Q2,Q4] | [Q0,Q4] |
> | Q4       | [Q4]          | [-]        | [-]     |
> | Q0Q4     | [Q4]          | [-]        | [Q0,Q4] |

And saves the following file on my directory:

input_file_dfa.txt:
```
Q0Q1Q2Q4 Q0Q2Q4 Q4 Q0Q4
Q0Q1Q2Q4
Q0Q1Q2Q4 Q0Q2Q4 Q4 Q0Q4
Q0Q1Q2Q4 a Q0Q1Q2Q4
Q0Q1Q2Q4 b Q0Q2Q4
Q0Q1Q2Q4 c Q0Q4
Q0Q2Q4 a Q4
Q0Q2Q4 b Q0Q2Q4
Q0Q2Q4 c Q0Q4
Q4 a Q4
Q0Q4 a Q4
Q0Q4 c Q0Q4
```

I've checked some [gaphviz documentations](https://www.graphviz.org/), but didnt have much success implementing it, so i'm letting for a further point in future. And also, [this python library](https://pysimpleautomata.readthedocs.io/en/latest/index.html) seems very useful, and worth to check it later.

Very good job made so far, and im proud of my accomplishments on this assignment.