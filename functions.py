# It is good practice to put functions, procedures and processes in a separate file

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # setting default parameter, this can be changed when calling the function
    """ Read a text file and return the list of 
    to-do items.
    """  # doc (help) strings are writen in the first line of the function - be a good citizen and write doc strings
    with open(filepath, 'r') as file_local:  # 'with' will close the file after reading it
        todos_local = file_local.readlines()
    return todos_local  # if return is not present the function will return 'None'.


def write_todos(todos_arg, filepath=FILEPATH):  # This function behaves as a procedure without returning anything.
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:  # (filepath, todos_arg) are parameters in the function definition.
        file_local.writelines(todos_arg)


# print("Hello from functions")  # code experiment 135 - will print everytime the module is imported

# print(x)  # introducing an error to trace it back

# returns name depending on where it is being run from - if run from here it will execute the if statement
print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
