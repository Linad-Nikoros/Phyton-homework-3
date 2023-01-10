# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов, отличной от 0.

list_1=[ 5.54, 45.47, 7.012, 5.3, 8, 12.61, 7.02, 9.88, 17.56, 63.32]
list_2=[]

for i in range(len(list_1)):
    list_2.append(round(list_1[i] % 1,3))

maximum=list_2[0]
minimum=list_2[0]

for i in range(len(list_2)):
   if list_2[i] !=0:       
     if list_2[i] > maximum: 
        maximum=list_2[i]
     if list_2[i] < minimum: 
        minimum=list_2[i]
              
difference=maximum-minimum
print(f'Разница между максимальным и минимальным значением дробной части равно: {difference}')    

