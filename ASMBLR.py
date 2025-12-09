# reading a file and storing it contents in list using readlines. 
# each element of a string is a line in a file 

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
            
def main():
    filename = "Add.asm"
    hack_file = "Add.hack"

    with open (filename, 'r') as file:
        lines_list = file.readlines()

    # the below statement is used to clear the file before appending into it
    with open(hack_file, 'w') as f:
        pass

    with open(hack_file,'a') as f:
        for line in lines_list:
            new_line = clean_line(line)
            if (new_line == "empty"):
                pass
            else:
                f.write(new_line+"\n")
    
main()
