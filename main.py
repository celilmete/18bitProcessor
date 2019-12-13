import sys
from Utils import *

add_group = ('ADD', 'AND', 'OR', 'XOR')
addi_group = ('ADDI', 'ANDI', 'ORI', 'XORI')
ld_group = ('LD', 'ST')
beq_group = ('BEQ', 'BLT', 'BGT', 'BLE', 'BGE')

if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
        config_file = "config.json"
        config = read_config(config_file)
        data = read_file(input_file)
    except:
        print("Please enter file as an argument")
        print("usage is: python3 main.py input.txt")
        sys.exit(1)
    out_list = []
    default_instructions = config['instructions']
    default_registers = config['registers']
    for item in data:
        instruction, registers = discriminator(item)
        opcode_digits = default_instructions[instruction]['opcode']
        print("opcode is", opcode_digits)
        if instruction in add_group:
            temp_binary = add_func(registers, default_registers, opcode_digits)
            temp_binary = "00" + temp_binary
            # print(temp_binary)
            hex_result = binary_to_hex(temp_binary)
            print(item)
            print(hex_result)
            print(temp_binary)
            out_list.append(hex_result)
            print(hex_result)
        elif instruction in addi_group:
            temp_binary = addi_func(registers, default_registers, opcode_digits)
            hex_result = binary_to_hex(temp_binary)
            out_list.append(hex_result)
            print(item)
            # print(temp_binary)
            print(hex_result)
        elif instruction in ld_group:
            temp_binary = ld_func(registers, default_registers, opcode_digits)
            hex_result = binary_to_hex(temp_binary)
            out_list.append(hex_result)
            print(item)
            #         print(temp_binary)
            print(hex_result)
        elif instruction in beq_group:
            temp_binary = beq_function(registers, default_registers, opcode_digits)
            hex_result = binary_to_hex(temp_binary)
            out_list.append(hex_result)
            print(item)
            #         print(temp_binary)
            print(hex_result)
        elif instruction == 'JUMP':
            temp_binary = jmp_func(registers, opcode_digits)
            hex_result = binary_to_hex(temp_binary)
            out_list.append(hex_result)
            print(item)
            #         print(temp_binary)
            print(hex_result)
        else:
            print("invalid instruction")

    # print("")
    # print(out_list)
    write_file(out_list)
