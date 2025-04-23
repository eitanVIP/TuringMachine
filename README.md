# Turing Machine
A busy beaver kind turing machine that can execute rules and draw the board.\
In addition there is a random rule generator.

## How To Recreate A Machine
After you run a machine and print it out, you should get something like this:\
TuringMachine([10000000000000001101], pos- 0, Instruction(1RB), Rule(0: 0LA, 1: 1SD), [Rule(0: 1RB, 1: 1LA), Rule(0: 0LA, 1: 1SD), Rule(0: 0RC, 1: 1SB), Rule(0: 0RB, 1: 0SD)])\
\
The first number in [] is the strip of numbers the machine works with.\
The pos is the position the head of the machine is now(0 is left).\
The instruction is what the machine is running now, for example 1RB translates to "write 1, move right, jump to rule B".\
The rule is the current running rule, it first mentions what to run if machine reads 0 and then mentions what to run if machine read 1. Notice that the instruction is the part of the current rule according to what the machine is reading.\
Then there is a list of all the rules of the machine. When you run the program yourself you can choose any names you want but in the images I provided the rules are named A, B, C, D in this order.\
So in this example to recreate the machine you need to create a machine with rules:\
A: Rule(0: 1RB, 1: 1LA)\
B: Rule(0: 0LA, 1: 1SD)\
C: Rule(0: 0RC, 1: 1SB)\
D: Rule(0: 0RB, 1: 0SD)\
**In Code:**\
![Code](https://github.com/user-attachments/assets/9e056801-d676-4820-bb20-f59cd1976e1d)


## Randomly Generated Examples
These are randomly generated rules and turing machines that created these boards.

**The Plane**
![Turing Machine Console Image](https://github.com/user-attachments/assets/a4024218-e86e-42f8-85ac-21b0131c4d34)

**The Mountain**
![Turing Machine Console Image](https://github.com/user-attachments/assets/f616174e-a450-4243-b221-413801bc1d66)

**The Zig-Zag Parallelogram**
![Turing Machine Console Image](https://github.com/user-attachments/assets/a58429dc-7615-4f0b-8f94-c352e98d1030)

**The Kinda Binary Counter**\
Counts in binary from the right side. every few frames the number goes up by one and then there are a lot of frames where it fixes the number to be correct before countinuing to count.
![Turing Machine Console Image](https://github.com/user-attachments/assets/75d62547-adbd-4acf-bf73-b14754fe83ef)
![Turing Machine Console Image](https://github.com/user-attachments/assets/12ec44c9-806e-4d07-a54b-62cde9675c02)
![Turing Machine Console Image](https://github.com/user-attachments/assets/80b69ae9-dd2d-4590-9602-77e9b8b8bbc6)
![Turing Machine Console Image](https://github.com/user-attachments/assets/32e98897-2fa3-4e3c-9c27-2115ee822374)
