'''Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.'''

cod = {}
q=[]
a,b,d,g = input(),input(),input(),input()
for i in range(len(a)):
    cod[a[i]]=b[i]
for i in range(len(d)):
    print(cod[d[i]], end='')
print()
for i in range(len(g)):
    for key, value in cod.items():
        if value == g[i]:
            print(key, end='')