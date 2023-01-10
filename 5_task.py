# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

num_1 = int(input("Введите число: "))

def Fibonacci(num):
        if num == 0:
            return 0
        if num == 1:
            return 1
        return Fibonacci(num-1)+Fibonacci(num-2)

list_1=[]
for i in range(1, num_1):
    list_1.append(str(Fibonacci(i)))
    list_1[i-1] = "-" + list_1[i-1] 
    
for i in range(num_1):
 list_1.append(str(Fibonacci(i)))

print(list_1)    

