
#    1    2     3
#1 ['🐻','🐻','🐻']
#2 ['🐻','🐻','🐻']
#3 ['🐻','🐻','🐻']

import random
import sys

row1=['🐻','🐻','🐻']
row2=['🐻','🐻','🐻']
row3=['🐻','🐻','🐻']
map=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')

computer_choice= random.choice([11,12,13,21,22,23,31,32,33])

u_input1=input("Enter your 1st choice:")
row = int(u_input1[0])-1
column = int(u_input1[1])-1
if int(u_input1)==computer_choice:
      print("Yeah! You got the treasure")
      map[row][column] ='💸'
      print((f'{row1}\n{row2}\n{row3}'))
      sys.exit("")
#marking users choice
map[row][column] = '🦊'
print((f'{row1}\n{row2}\n{row3}'))

u_input2=input("Enter your 2nd choice:")
row = int(u_input2[0])-1
column = int(u_input2[1])-1
if int(u_input2)==computer_choice:
      print("Yeah! You got the treasure")
      map[row][column] ='💸'
      print((f'{row1}\n{row2}\n{row3}'))
      sys.exit("")
#marking users choice
map[row][column] = '🦊'
print((f'{row1}\n{row2}\n{row3}'))

u_input3=input("Enter your 3rd choice:")
row = int(u_input3[0])-1
column = int(u_input3[1])-1
if int(u_input3)==computer_choice:
      print("Yeah! You got the treasure")
      map[row][column] ='💸'
      print((f'{row1}\n{row2}\n{row3}'))
      sys.exit("")
#marking users choice
map[row][column] = '🦊'
print((f'{row1}\n{row2}\n{row3}'))