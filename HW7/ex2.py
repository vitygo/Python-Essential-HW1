

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# генератор
def square_list_numbers(lst:list):
    for num in lst:
        yield num ** 2

for num in square_list_numbers(my_list):
    print(num)

#цикл
for num in my_list:
    print(num ** 2)

    