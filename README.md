# Hack Assembler (Python)

This project is a simple assembler written in Python for the **Hack computer** from the *Nand2Tetris* course.  
It converts `.asm` assembly programs into `.hack` binary machine code.

The goal of this project was to understand how assembly instructions are translated into binary at a low level, instead of relying on existing tools.

---

## What this assembler does

- Reads a `.asm` file line by line
- Removes comments and extra whitespace
- Handles **A-instructions**, **C-instructions**, and **labels**
- Builds and manages a **symbol table**
- Converts instructions into 16-bit binary format
- Writes the output into a `.hack` file

This assembler follows the Hack instruction format exactly.

---

## Instruction handling

### A-instructions
- Format: `@value`
- Supports:
  - Numeric values (e.g. `@21`)
  - Predefined symbols (`SP`, `R0`, `SCREEN`, etc.)
  - User-defined variables (assigned RAM addresses starting from 16)

### C-instructions
- Supports all valid combinations of:
  - `dest=comp;jump`
- Uses lookup tables for:
  - `dest`
  - `comp`
  - `jump`

The binary output is generated as:

## Two-pass approach

### Pass 1: Symbol table
- Scans the file to find labels like `(LOOP)`
- Stores their ROM addresses
- Labels are not converted into binary

### Pass 2: Code generation
- Converts instructions into binary
- Assigns RAM addresses to variables
- Writes final machine code into the `.hack` file

---

## Project structure

- `assembler.py` – main assembler code
- Input: `program.asm`
- Output: `program.hack`

The `.asm` file must be in the same directory as `assembler.py`.

---

## How to run

1. Place your `.asm` file in the same folder as `assembler.py`
2. Run the program:
3. Enter the file name **without** `.asm`
4. The output `.hack` file will be generated automatically

This project is part of my learning in computer architecture and low-level systems.

---

## Limitations

- No error handling for invalid instructions
- Assumes input follows Hack assembly rules
- Single-file implementation for learning clarity

---

## References

- Nand2Tetris course
- Hack Computer Specification
