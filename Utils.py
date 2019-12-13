import json


def read_config(file_path):
    with open(file_path) as config_file:
        data = json.load(config_file)
    return data


def read_file(file_path):
    with open(file_path) as f:
        data = f.readlines()
    return data


def discriminator(string):
    out = string.split()
    instruction = out[0]
    registers = out[1]
    registers = registers.split(',')
    return instruction, registers


def add_func(registers, def_registers, opcode):
    temp_binary = ''
    for register in registers:
        temp_binary = def_registers[register] + temp_binary
    temp_binary = temp_binary + opcode
    return temp_binary


def addi_func(registers, def_registers, opcode):
    temp_binary = ''
    temp_binary = def_registers[registers[0]] + temp_binary
    temp_binary = def_registers[registers[1]] + temp_binary
    # print(bin(int(registers[2]))[2:])
    temp_binary = bin(int(registers[2]))[2:] + temp_binary
    temp_binary = temp_binary + opcode
    # print(temp_binary)
    # print(len(temp_binary))
    try:
        for i in range(18 - len(temp_binary)):
            temp_binary = '0' + temp_binary
    except:
        print("IMM value is not accepted")
    # print(temp_binary)
    # print(len(temp_binary))
    return temp_binary


def jmp_func(address, opcode):
    temp_binary = ''
    temp_binary = temp_binary + opcode
    temp_binary = bin(int(address[0]))[2:] + temp_binary
    try:
        for i in range(18 - len(temp_binary)):
            temp_binary = '0' + temp_binary
    except:
        print("ADDR value is not accepted")
    return temp_binary


def ld_func(registers, def_registers, opcode):
    temp_binary = ''
    temp_binary = temp_binary + opcode
    temp_binary = def_registers[registers[0]] + temp_binary
    temp_binary = bin(int(registers[1]))[2:] + temp_binary
    try:
        for i in range(18 - len(temp_binary)):
            temp_binary = '0' + temp_binary
    except:
        print("ADDR value is not accepted")
    return temp_binary


def beq_function(registers, def_registers, opcode):
    temp_binary = ''
    temp_binary = temp_binary + opcode
    temp_binary = def_registers[registers[0]] + temp_binary
    temp_binary = def_registers[registers[1]] + temp_binary
    temp_binary = bin(int(registers[2]))[2:] + temp_binary
    try:
        for i in range(18 - len(temp_binary)):
            temp_binary = '0' + temp_binary
    except:
        print("ADDR value is not accepted")
    return temp_binary


def binary_to_hex(binary_val):
    hex_result = hex(int(binary_val, 2))
    # print(hex_result[2:])
    hex_result = hex_result[2:]
    if len(hex_result) < 5:
        for i in range(5 - len(hex_result)):
            hex_result = '0' + hex_result
    return hex_result


def write_file(result):
    with open('out.hex', 'w') as file:
        file.write('v2.0 raw\n')
        column_flag = 1
        tab_flag = 0
        for i in result:
            file.write(i)
            tab_flag += 1
            if tab_flag % 16 == 0:
                file.write('\n')
            elif tab_flag % 4 == 0:
                file.write('   ')
            else:
                file.write(' ')
