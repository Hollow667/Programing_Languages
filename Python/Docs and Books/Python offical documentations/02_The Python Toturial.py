'''the python toturail'''
        #2: the interputer and its environmet:
#---
    #2-2-Source Code Incodeing:
'''
Usaualy UTF-8, to change it use:
# -*- encode: encoding -*-
'''
# -*- coding: cp-1252 -*-
#---

#3: An Informal Intrudoction to Python:

#--
    #3-1-using python as calculator:

#---
#3-1-2-Strings:

print('put several strings with in parantheses' 'to have joined together')
#but you can not concanet a varibale an a string lateral:
#word = "hi"; print(word ' there');#Wrong

word = "Python"
print(word[0])  #first letter P
print(word[-1]) #last letter n
#and you can use word[start position:end position] or word[:end_position] or word[start_position:]

#word[10]#wrong out of range of the string word = "Python"
#but if you use range indexes will not have an error
print(word[10:1])

#strings are immutable so you cannot change its value
word = "Python"
#word[0] = "h";#Wrong instead use:
def change_letter(string_to_change, letter_number, string_to_change_with):
    return string_to_change[:letter_number] + string_to_change_with + string_to_change[letter_number+1:]
word = change_letter(word, 0, "H")
print(word)
#---

#3-1-3-Lists:
#---
List = [1,2,3,4]

#lists are mutable
List[0] = 2;#make the first item value in the list 2

#Slicig
ShallowCopy = List[:] #slicing provides a shallow copy of the list
#replacing with slicing
List[1:2] = [1,2,3,4,5]
#removing with sclising
List[1:5] = []
#clear with slicing
List[:] = []

#get length of the list:
len(List);
#---

    #3-2-Fibonacci series:
#--
a,b=1,1
while a<1000:
    print(a,end=",")
    a,b=b,a+b
#--

        #4-More Control Flow Tools:
    #4-1-if statements:
#--
#if elif else
'''
x=int(input("enter an integer: "))
if x < 0:
    x = 0
    print("x value has been changed to Zero")
elif x == 0:
    print("x value is zero")
else:
    print("x is positive number")
'''
#--

    #4-2-for statements:
#--
#iterating through a list with the loop:
words = ["python", "is","great"]
for word in words:
    print(word)

#do not change the list while you are iterating it
#use slicing to get a shallow copy
words = ["python", "is","great"]
for word in words[:]: #now you're iterating through the copy... ^_^
    words.insert(len(words),"yes")
print(words)    

#iterating through dictionaries:
dic = {"key1":"val1","key2":"val2"}
for key, val in dic.items():
    print(key, ":", val)
#--

    #4-2-range():
#returns an arithmetic progression


#make a list of numbers:
List_of_numbers = list(range(10))
print(List_of_numbers)

    #4-3-break, continue, else
#else cluse of a for statements runs when no break cluse runs in the for statment
for j in range(2):
    for i in range(2):
        print(i)
    else:
        print("no breaks")

    for i in range(2):
        if i == 0 :
            break
        else:
            print(i)
    else:
        print("will not print bacuse there is a break cluse")

    #pass
#it does nothing and used for declearing empty classes, functions,or inside loops
for i in range(5):
    pass
        

    #4-7-More Defining Functions
#4-7-1-Defining Arguments Values
#---
#if you want to choose a type for an argument
def func(a, b=list()):
    print(type(b))
#but you still can change it
func(1,1)

#if you want to choose a type for an argument
def func(a : int, b : list,c:str):
    print(func.__annotations__)#will display the desired types or arguments
    print(type(b))
#but you still can change it
func(1,1,1)
                                            
#dynamically convert function args:
def main_func(a: int, b: float, c: str):
    print(a, b, c)
    pass
def call(func, *args):
    dic = func.__annotations__
    arg_list = list(args)
    if len(dic) != len(arg_list):
        print("Different args and paras")
        return
    try:
        x256 = 0
        for key, val in dic.items():
            dic[key] = val(arg_list[x256])
            x256 += 1
        func(**dic)
    finally:
        pass
call(main_func,1,2,3)

print(dic)

print(dic)
#if you want to make sure youu get value
def func2(a, b=None):
    if(b != None):
        print("I've got a value")
func2(1,1)
#---

#4-7-2-Key Word Arguements:
def concat(*args, sep=","):
    return sep.join(args)
print(concat("1","2","3"))

def print_keywords(**keywords):
    for var_name in keywords:
        print(var_name + ":" + str(keywords[var_name]))
print_keywords(i=0,j=1)

def print2(a,b):
    print(a)
    print(b)
a = {"b": 1, "a": 0}
print2(**a)

#4-7-5-lambda function:
#lambda args: return
def add(b):
    return lambda a: a + b
f = add(1) #a = 1
print(f(2))

#4-7-8-Doc a function:
def func_doc():
    '''write your doc here'''
    
    pass
print(func_doc.__doc__)

#5-1-2-list comprehesnsions:
List = [i for i in range(10)]
List = [[x, y] for x in [1, 2, 3] for y in [1, 2, 3] if x != y]
print(List)

#5-1-3-Nested Lists comprehensions:
Matrix = [[1,2,3],[1,2,3],[1,2,3]]
Col = [[row[i] for row in Matrix] for i in range(len(Matrix))]
print(Col)

#5-2-define a tuple:
tup = "hi", #notice the comma
print(tup)

#unpacking tuple
tup = 1, 2, 3
x, y, z = tup
print(x, y, z)


#6-2-Standard Modules:
#the variable sys.path is a string list used be the interpeter to search for modules
import sys as sys
sys.path.append('C:/Program Files/MATLAB/')



#
long_number = 10000
#same as
long_number = 10_000
print(long_number)


#7-1-1-Formating String laterals:
import math 
print(f"{math.pi:1.3}")
 
#7-1-2-The String Formate() Method:
print('{} = {}'.format("val1", "5"))
print('{key}: {val}'.format(key = "key1", val = "val1"))

#7-2-1-Methods of files objects:
#write ti a binary
'''
f=open("workflow","wb") #open file for writing or creates it if not exist
f.write(b"01234567890abcdefg")
f.close()
'''

#read from binary
f=open("workflow","rb")
f.seek(5);              #move to the 5 position in the file
print(f.read(1));       #reads one byte
f.close()

#8-3-Handling exceptions:
class B(Exception):
    pass
class C(Exception):
    pass
for cls in [C, B]:
    try:
        raise cls()
    except B:
        print("B Exception raised")
    except C:
        print("C Exception raised")

try:
    raise Exception('message1','message2')
except Exception as err:
    msg_list = list(err.args)
    msg1, msg2 = err.args
    print("Error Message List :",msg_list)
    print("msg1: ",msg1,",msg2: ",msg2)

#9-8-Iterators:

#iterate through file lines:
'''
for line in open("file.txt"):
    print(line)
'''

for char in ("string"):
    print(char)

#9-9-Generators:
#Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)


#10.Brief tour of the standard library:

#10-1-Current Working Directory
import os
print("Current Directory: ",os.getcwd())

#coppy a file:
import shutil
#shutil.copyfile("file_name","newfilename")

#10-2-file wildcards:
#search for all python files in the current directory:
import glob
print(glob.glob('*.py'))

#10-3-get command line args:
import sys
print("args: ",sys.argv)

#10-4-Error Output and Redirection:
import sys
sys.stderr.write('Error, file not found\n')
sys.stdout.write('hi\n')
#print('waiting user to enter a line...',end="");entr = sys.stdin.readline();print(entr)
#log messages are sent to a file or to sys.stderr:
import logging
logging.debug('Debugging information')

#10-6
#Random Choice
import random
print(random.choice(['apple','pear','banana']))

#statictics:
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("data: ", data)
print('mean: ', statistics.mean(data))
print('median: ',statistics.median(data))
print('stdev: ', statistics.stdev(data))
print('variance: ', statistics.variance(data))

#10-10- Measure execution time:
from timeit import Timer
print("code executing time is: ", Timer('i = 0').timeit())



#15-Foating Point arithmetic: Issues and limitions:
#0.1 is actualy 0.1000000000000000055511151231257827021181583404541015625
print(0.1 + 0.1 + 0.1 == 0.3) #False
