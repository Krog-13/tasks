'''Выведите таблицу размером n×n заполненную
числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке'''
r=int(input())
q=[[0 for i in range(r)] for i in range(r)]
t,u=0,1
n,m=len(q),len(q[0])

for i in range (n):
    for j in range (t,m-t):
        q[i][j]=u
        u+=1
    for j in range (-m+t,(-m+1)+t):
        for i in range (t+1,n-t):
            q[i][-j-1]=u
            u+=1
        for i in range (-n+t,(-n+1)+t):
            for j in range ((t+2),m-t):
                q[-i-1][-j]=u
                u+=1
            for j in range (0+t,t+1):
                for i in range(t+1,n-t):
                    q[-i][j]=u
                    u+=1
            t+=1
for i in range (m):
    print(*q[i])