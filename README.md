<h2 align="center">Instruction-Set Architecture Simulation</h2>
<h3 align="center">For DTU Cyber Systems Intro</h3>

This is an implementation of a simple ISA processor in python.  
It is limited to 8-bit unsigned integers and implements the following instruction set:  

| Instruction      |     Description     |
|:-----------------|:-------------------:|
| `ADD R1, R2, R3` |    R1 = R2 + R3     |
| `SUB R1, R2, R3` |    R1 = R2 - R3     |
| `OR R1, R2, R3`  |    R1 = R2 ⏐ R3     |
| `AND R1, R2, R3` |    R1 = R2 & R3     |
| `NOT R1, R2`     |      R1 = ~R2       |
| `LI R1, n`       |       R1 = n        |
| `LD R1, R2`      |   R1 = memory(R2)   |
| `SD R1, R2`      |   memory(R2) = R1   |
| `JR R1`          |      go to R1       |
| `JEQ R1, R2, R3` | if(R2==R3) go to R1 |
| `JLT R1, R2, R3` | if(R2<R3) go to R1  |
| `NOP`            |    no operation     |
| `END`            | end of instructions |

## Prerequisites
### VENV:
This does not use any external packages.  
It will work for `python 3.10` and above.

## Usage
### Test 1:
This is an arbitrary test of all instructions.  
Run the following command in the base folder of the repository:  
```python3 isa-sim.py 1000 test_1/program.txt test_1/data_mem.txt```  

### Test 2 - Bubble sort:
Run the following command in the base folder of the repository:  
```python3 isa-sim.py 1000 test_2/program.txt test_2/data_mem.txt```  
This will sort all the numbers in memory 0 to 9 and write them in memory 10-19.

### Test 3 - Largest prime factor algorithm:
Run the following command in the base folder of the repository:  
```python3 isa-sim.py 1000 test_3/program.txt test_3/seed_1.txt``` (change `seed_1` for other tests)  
This will generate a random number using the Fibonacci sequence based on values in memory.  
Check the seed file for the specific purpose of each value.

---
In any test, replace `1000` with your desired maximum cycles before simulation termination.  
