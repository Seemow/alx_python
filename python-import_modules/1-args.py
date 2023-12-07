if __name__ == "__main__":
    from sys import argv

    num_arguments = len(argv) - 1 

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif num_arguments > 1:
        print("{} arguments:".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, argv[i]))
