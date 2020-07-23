#!/usr/bin/python
import datetime
import random
from random import choice
from string import ascii_letters
nu = random.randint(80000, 150000)
c = (random.randint(1700, 2900))
c1 = (c * 9)
c2 = (c1 * 9)
c3 = (c2 * 9)
c4 = (c3 * 7)
m = ['[Jira]', '[Zabbix]', '[Bamboo]', '[Conf]', '[BitBucket]']
t = random.choice(m)
nu1 = str(nu)
x = ''.join(choice(ascii_letters) for i in range(100, 500))
nu2 = (nu1 + x)
nu5 = 'holaholahola'
nu3 = nu2.replace(str(nu2[3]), str("\x0a"))
nu4 = nu2.replace(str(nu2[1]), "$")
type = '[INFO]'
ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nu1 = str(nu)
nu2 = (nu1 + x)
nu33 = 'close_multistring'
f= open("truelog4.log", "w")
for i in range(c):
    f.write(str([ts])+''+str(type)+''+str(t)+''+str([nu2])+ "\r")
    f.close

for i in range(c):
    with open('truelog4.log', 'a') as file:
        f.write(str([ts])+'\n'+str(type)+'\n'+str(t)+'\n'+str([nu2])+'\n'+str([nu3])+'\n'+str(nu33)+'\n' "\r")
 
f= open("truelog3.log", "w")
for i in range(c1):
        f.write(str([ts])+''+str(type)+''+str(t)+''+str([nu2])+ "\r")
        f.close
f= open("truelog3.log", "a")
for i in range(c2):
        f.write(str([ts])+'\n'+str(type)+'\n'+str(t)+'\n'+str([nu2])+'\n'+str([nu3])+'\n'+str([nu4])+'\n'+str([nu5])+'\n'+str([nu])+'\n'+str(nu1)+'\n'+str(ts)+'' "\r")
        f.close
f= open("truelog2.log", "w+")
for i in range(c2):
        f.write(str([ts])+''+str(type)+''+str(t)+''+str([nu2])+ "\r")
        f.close
f= open('truelog2.log', 'a')
f.write(str([ts])+'\n'+str(type)+'\n'+str(t)+'\n'+str([nu2])+'\n'+str([nu3])+'\n'+str([nu4])+'\n'+str([nu5])+'\n'+str([nu])+'\n'+str(nu1)+'\n'+str(ts)+'' "\r")
f.close
f= open("truelog1.log", "w+")
for i in range(c3):
        f.write(str([ts])+''+str(type)+''+str(t)+''+str([nu2])+ "\r")
        f.close
with open('truelog1.log', 'a') as file:
    f.write(str([ts])+'\n'+str(type)+'\n'+str(t)+'\n'+str([nu2])+'\n'+str([nu3])+'\n'+str([nu4])+'\n'+str([nu5])+'\n'+str([nu])+'\n'+str(nu1)+'\n'+str(ts)+'' "\r")
f.close
f= open("truelog.log", "w+")
with open('truelog.log', 'a') as file:
    f.write(str([ts])+'\n'+str(type)+'\n'+str(t)+'\n'+str([nu2])+'\n'+str([nu3])+'\n'+str([nu4])+'\n'+str([nu5])+'\n'+str([nu])+'\n'+str(nu1)+'\n'+str(ts)+'' "\r")
f.close

print(c4)

print(c3)

print(c2)

print(c1)

print(c)