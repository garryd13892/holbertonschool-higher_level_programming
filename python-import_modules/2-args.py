
#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("Number of argument(s): 0.")
    elif:
        arg_label = "argument" if num_arguments == 1 else "arguments"
        print(f"Number of argument(s): {num_arguments} {arg_label}:")
        
        for index in range(num_arguments):
        print(f"{index + 1}: {arguments[index]}")