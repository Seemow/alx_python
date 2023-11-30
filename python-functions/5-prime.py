def is_prime(number):
    test = True
    if number <= 1:
        test = False
    elif number == 2:
        test = True
    else:
        for i in range(2,number):
            if number % i == 0:
                test = False
                break
    return test
