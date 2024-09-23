
def prime_numbers(n:int):
    for num in range(2, n):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num
    
for num in prime_numbers(15):
    print(num)