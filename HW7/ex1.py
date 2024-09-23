my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reverse_lst(lst):
    for i in range(len(lst)-1, -1, -1):
        yield lst[i]

for num in reverse_lst(my_list):
    print(num)