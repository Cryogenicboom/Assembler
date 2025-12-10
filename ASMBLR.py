# reading a file and storing it contents in list using readlines. 
# each element of a string is a line in a file 

dest_bits = {
    ""   : "000",
    "M"  : "001",
    "D"  : "010",
    "MD" : "011",
    "A"  : "100",
    "AM" : "101",
    "AD" : "110",
    "AMD": "111",
}

jump_bits = {
    ""   : "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

comp_bits = {
    "0"  : "0101010",
    "1"  : "0111111",
    "-1" : "0111010",
    "D"  : "0001100",
    "A"  : "0110000",
    "M"  : "1110000",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
    "!D" : "0001101",
    "!A" : "0110001",
    "!M" : "1110001",
    "-D" : "0001111",
    "-A" : "0110011",
    "-M" : "1110011",
}

def clean_line(line):
    ''' 
    finding index of '//' using .find()
    .find() --> return -1 if respective thing doesn't exist

    after getting index of //, we store everything into a variable, and contents after // is deleted.
    '''
    index = line.find("//")
    if(index != -1):
        before_comment = line[:index]
        before_comment = before_comment.strip()
        if(len(before_comment) == 0):
            return "empty"
        else: 
            return before_comment
    else:
        remove_whitespace_lines = line.strip()
        if(len(remove_whitespace_lines)== 0):
            return "empty"
        else:
            return remove_whitespace_lines

symbol_table = {
    'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
    'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
    'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
    'SCREEN':0x4000, 'KBD':0x6000
}

def main():
    filename = "Add.asm"
    hack_file = "Add.hack"

    with open (filename, 'r') as file:
        lines_list = file.readlines()

    with open(hack_file, 'w') as f:
        pass

    with open(hack_file,'a') as f:
        for line in lines_list:
            new_line = clean_line(line)
            if (new_line == "empty"):
                pass
            else:
    
                if(new_line.startswith("@")):
                    value = new_line[1:]
                    int_value = int(value)
                    bin_value = format(int_value, '016b')
                    f.write(bin_value+"\n")


                elif(new_line.startswith("(")):
                    # Labels are not converted to binary, their ROM address will be stored instead.
                    pass                  
      
                else:
                    if (";" in new_line):
                        # if jump is present
                        index = new_line.find(";")
                        jump = new_line[index+1:]
                        remaining = new_line[:index]

                        if("=" in remaining):
                            i = remaining.find("=")
                            dest = remaining[:i]
                            comp = remaining[i+1:]
                        else:
                            comp = remaining
                            dest = ""

                    # when jump is not present
                    elif("=" in new_line):
                        i = new_line.find("=")
                        dest = new_line[:i]
                        comp = new_line[i+1:]
                        jump = ""
                    else:
                        comp = new_line 
                        dest = ""
                        jump = ""

                    # print("C:"+new_line+" dest= "+dest+" comp= "+comp+" jump= "+jump)
                    
                    dest_bin = dest_bits[dest]
                    comp_bin = comp_bits[comp]
                    jump_bin = jump_bits[jump]
                    c_binary = "111"+comp_bin+dest_bin+jump_bin
                    f.write(c_binary+"\n")


main()
