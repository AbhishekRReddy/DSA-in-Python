def print_num(num):
    if num>5:
        return
    print(num)
    print_num(num+1)



print_num(1)