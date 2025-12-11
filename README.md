# Assembler
### Overview:
This project is a two pass assembler for the Hack computer from Nand2Tetris.
<br>
Working : File_name.asm --> Assembler --> File_name.hack
<br>
The assembler supports:
<br>
> A-instructions (@value), where value can be an integer or a string (variable)<br>
> C-instructions (destination = computation ;jump)<br>
> Labels ((LABEL))<br>
> Variables (allocated from RAM address 16)<br>
> Predefined symbols (SP, LCL, ARG, R0–R15, SCREEN, KBD)
<br>

1. The assembler is built to perform Line cleaning (strip out comments and whitespaces)<br>
2. Parse C-instruction (dest/comp/jump) <br>
3. Code tables (dest_bits, comp_bits, jump_bits)<br>
4. Symbol table
<br>
Two passes:<br>

> Pass 1: label resolution (ROM addresses)<br>
> Pass 2: machine code generation (A-instruction / c-instruction to binary)
<br>

## Code explaination: 
<br>
### Reading the file and preparing output: 

<h2>1. The file is read once at the beginning:<br>

> with open(filename, 'r') as file:<br>
> - lines_list = file.readlines()


lines_list is a list of strings.

Each element is one line from the .asm file.

Before writing .hack, the target file is cleared to avoid mixing old content with new assembly output:

with open(hack_file, 'w') as f:
    pass


Later, the assembler opens the same file in append mode to write the actual output:

with open(hack_file, 'a') as f:
    ...

3. Cleaning lines: removing comments and whitespace

Function: clean_line(line)

Goal: turn raw lines from the .asm file into logical instructions or "empty".

Steps:

Find inline comments

The Hack comment syntax is //.

line.find("//") gives the index of the first / in //.

If index != -1, it means a comment exists:

index = line.find("//")
if index != -1:
    before_comment = line[:index]
    before_comment = before_comment.strip()
    if len(before_comment) == 0:
        return "empty"
    else:
        return before_comment


Everything after // is discarded.

.strip() removes spaces and tabs from both ends.

If the remaining text is empty, the function returns "empty".

Handle lines without //
If no comment is found (index == -1), we only strip whitespace:

remove_whitespace_lines = line.strip()
if len(remove_whitespace_lines) == 0:
    return "empty"
else:
    return remove_whitespace_lines


So clean_line returns either:

a cleaned non-empty instruction string (e.g. "@2", "D=A", "(LOOP)"), or

the string "empty" for blank/comment-only lines.

4. Code tables: dest, comp, jump → bits

Three dictionaries are used to convert mnemonics into bit patterns:

dest_bits → 3-bit string

jump_bits → 3-bit string

comp_bits → 7-bit string
