from init import *

print("\nWelcome to the ISA simulator! - Nathan, Veronica, and Lucie")

current_cycle = 0
instruction_index = 0
running = True

# -- Instruction Set -- #

def execute_instruction(index: int):
    global instruction_index, running
    name = instructionMemory.read_opcode(index)
    args = [instructionMemory.read_operand_1(index), instructionMemory.read_operand_2(index), instructionMemory.read_operand_3(index)]
    match name:
        case 'ADD':
            registerFile.write_register(args[0], registerFile.read_register(args[1]) + registerFile.read_register(args[2]))
        case 'SUB':
            registerFile.write_register(args[0], registerFile.read_register(args[1]) - registerFile.read_register(args[2]))
        case 'OR':
            registerFile.write_register(args[0], registerFile.read_register(args[1]) | registerFile.read_register(args[2]))
        case 'AND':
            registerFile.write_register(args[0], registerFile.read_register(args[1]) & registerFile.read_register(args[2]))
        case 'NOT':
            registerFile.write_register(args[0], ~registerFile.read_register(args[1]))
        case 'LI':
            registerFile.write_register(args[0], int(args[1]))
        case 'LD':
            registerFile.write_register(args[0], int(dataMemory.read_data(registerFile.read_register(args[1]))))
        case 'SD':
            dataMemory.write_data(int(registerFile.read_register(args[1])), registerFile.read_register(args[0]))
        case 'JR':
            instruction_index = int(registerFile.read_register(args[0])) - 1
        case 'JEQ':
            if registerFile.read_register(args[1]) == registerFile.read_register(args[2]):
                instruction_index = int(registerFile.read_register(args[0])) - 1
        case 'JLT':
            if registerFile.read_register(args[1]) < registerFile.read_register(args[2]):
                instruction_index = int(registerFile.read_register(args[0])) - 1
        case 'NOP':
            return
        case 'END':
            running = False

print('\n---Start of simulation---')

####################################
##        Simulation Start        ##

while running:
    if current_cycle < max_cycles:
        execute_instruction(instruction_index)
        instruction_index += 1
        current_cycle += 1
    else:
        running = False
        print("\n*!-!-!-!-!-!-!-!-!-!-!*")
        print("Exceeded maximum cycles")
        print("*!-!-!-!-!-!-!-!-!-!-!*")

print("\n*- End State Reached -*")
print(f"Total cycles: {current_cycle-1}\n")
registerFile.print_all()
print("")
dataMemory.print_used()

##         Simulation End         ##
####################################

print('\n---End of simulation---\n')