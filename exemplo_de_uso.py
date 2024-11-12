import os
os.system("cls")
def fibonacci(n):
    sequence = [0, 1]  
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]  
        sequence.append(next_value)  
    return sequence

n = int(input("digite um valor: "))
print(fibonacci(n))