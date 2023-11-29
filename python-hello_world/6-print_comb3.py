for i in range(0,10):
    for j in range(i + 1, 10):
        if int(str(i)+str(j)) < 89:
            print(int(str(i)+str(j)) , end=", ")
        else:
            print(int(str(i)+str(j)))