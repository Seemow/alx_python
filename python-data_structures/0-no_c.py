def no_c(my_string):
    my_list = []
    for i in range(0, len(my_string) - 1):
        if my_string[i] != "c" and my_string[i] != "C":
            my_list.append(my_string[i])
    return ''.join(my_list)