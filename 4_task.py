# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num_1=int(input("Ввдите число в десятичной системе измерения: "))

Remains= " "
while num_1 > 0:
    Remains=str(num_1 % 2)+Remains
    num_1//=2

print(f' В двоичной системе измерения число иимеет вид: {Remains}')