#Built-in Functions:
ord('a')        #97
chr(97)         #a

#Built-in Types
hex(255)        #0xff
f'{255:x}'      #ff
f'{255:X}'      #FF
f'{255:#x}'     #0xff

oct(8)          #0x10
f'{8:o}'        #10
f'{8:#o}'       #0o10

bin(2)          #0b10
f'{255:b}'      #10
f'{255:#b}'     #0b10

"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
#'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

num = 2         #10
num.bit_length()#2

integer=5
#always use this method
integer.to_bytes((integer.bit_length()+7) // 8, byteorder='big',signed=True)    #b'\x05'
integer.from_bytes(b'\x05', byteorder='big',signed=True)                        #5

flt = 1.0
flt.is_integer()#True
flt.fromhex('FF')#255.0
flt=255.0;flt.hex()#0x1.fe00000000000p+7

#Built-in Exceptions
'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''

#Text Processing Services
'''
string.ascii_letters  : The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
string.ascii_lowercase : The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
string.ascii_uppercase : The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
string.digits : The string '0123456789'.
string.hexdigits  : The string '0123456789abcdefABCDEF'.
string.octdigits  : The string '01234567'.
string.punctuation  : String of ASCII characters which are considered punctuation characters in the C locale.
string.printable  : String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
string.whitespace  : A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
'''

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord) #'Coordinates: 37.24N, -115.81W'

'{:,}'.format(1234567890) #'1,234,567,890'

points = 19;total = 22
'Correct answers: {:.2%}'.format(points/total)  #'Correct answers: 86.36%'

"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
#'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

#difflib — Helpers for computing deltas
#find the closest python keyword to a given word
import difflib ,keyword
difflib.get_close_matches('wheel', keyword.kwlist)  #['while']
difflib.get_close_matches('accept', keyword.kwlist) #['except']


#Data Types:
from datetime import datetime
datetime.now().isoformat(timespec='auto') #2020-04-30T17:40:10.025874
datetime.now().isoformat(timespec='hours') #2020-04-30T17
datetime.now().isoformat(timespec='minutes') #2020-04-30T17:40
datetime.now().isoformat(timespec='seconds') #2020-04-30T17:40:10
datetime.now().isoformat(timespec='milliseconds') #2020-04-30T17:40:10.088
datetime.now().isoformat(timespec='microseconds') #2020-04-30T17:40:10.088275

#math — Mathematical functions
'''
math.isinf(x) : Return True if x is a positive or negative infinity, and False otherwise.
math.isnan(x) : Return True if x is a NaN (not a number), and False otherwise.
math.log(x[, base])  : With one argument, return the natural logarithm of x (to base e).
math.log2(x)  : Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).
math.inf : A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').
math.nan  : A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').
math.pi  : The mathematical constant p = 3.141592…, to available precision.
math.e  : The mathematical constant e = 2.718281…, to available precision.

'''

#Numeric and Mathematical Modules
'''
import random
cards = [str(i)+j for i in list(range(2,11)) + ["B","G","M","A"] for j in ["A", "B", "C", "D"]]
print(cards)
card1 = random.sample(cards,k=13)
for card in card1:cards.remove(card)
card2 = random.sample(cards,k=13)
for card in card2:cards.remove(card)
card3 = random.sample(cards,k=13)
for card in card3:cards.remove(card)
card4 = random.sample(cards,k=13)
for card in card4:cards.remove(card)
print(cards);print(card1);print(card2);print(card3);print(card4)
'''

#pathlib — Object-oriented filesystem paths
import os
os.path.exists("C:\\")  #True



'''
os.path.getatime(path) #last access
Return the time of last access of path. The return value is a floating point number giving the number of seconds since the epoch (see the time module). Raise OSError if the file does not exist or is inaccessible.

os.path.getmtime(path) #last modification
Return the time of last modification of path. The return value is a floating point number giving the number of seconds since the epoch (see the time module). Raise OSError if the file does not exist or is inaccessible.

os.path.getsize(path) 
Return the size, in bytes, of path. Raise OSError if the file does not exist or is inaccessible.

os.path.isfile(path) 
Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.

'''

#tempfile — Generate temporary files and directories
'''
import tempfile
# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read() #b'Hello world!'
# close the file, it will be removed
input("Go search for it...")
fp.close()
'''
"""289
#get specific line
import linecache
print(linecache.getline(__file__, 8))
#__file__ is the current python file name

#get storage info
import shutil
print(shutil.disk_usage("C:\\"))

#find python executable
#where in cmd
import shutil
print(shutil.which("python"))


#make archive of the files in the "to Archive" file in the current python file
import shutil
import os
shutil.make_archive("zipfilename","zip",root_dir=os.getcwd()+"\\to Archive")
#add only python files
import zipfile
python_archive = zipfile.PyZipFile("zipfilename.zip","w",optimize=0)
python_archive.write(os.getcwd())
python_archive.close()
#sqlite3 — DB-API 2.0 interface for SQLite databases
import sqlite3
try:
    #create a connecter to the database
    conn = sqlite3.connect("simple.db")
    #create a cursor to execute sql commands
    c = conn.cursor()
    #create a table
    c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
    #insert some data:
except:
    #will give an error if the database alread exist
    pass

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()
#close the database
conn.close()

#reopen the database
conn = sqlite3.connect("simple.db")
c = conn.cursor()
t = ('RHAT',) #to select RHAT and other name you may want
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())
#insert other data and you must to commit to save changes
data = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
        ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', data)
#get all data
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
#close
conn.commit()
conn.close()

#csv — CSV File Reading and Writing
table = [[str(i) for i in range(10)] for j in range(10)]
import csv
with open("data.csv","w",newline='') as f:
    Writer = csv.writer(f)
    Writer.writerows(table)
#reading info:
with open("data.csv","r",newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


#hashlib — Secure hashes and message digests
import hashlib
hasher = hashlib.sha256
print(hasher(b'hi').digest())
print(hasher(b'hi').hexdigest())
206"""

#Generic Operating System Services
#info
import os
os.getcwd() #C:\Users\ahmed\Desktop\Python Study\Docs and Books\Python Documentation 3.7.2
os.get_exec_path()   #['C:\\Windows\\system32', 'C:\\Windows', 'C:\\Windows\\System32\\Wbem', 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\', 'C:\\Program Files\\Microsoft\\Web Platform Installer\\', 'C:\\Program Files (x86)\\Microsoft ASP.NET\\ASP.NET Web Pages\\v1.0\\', 'C:\\Program Files (x86)\\Windows Kits\\8.0\\Windows Performance Toolkit\\', 'C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\', 'C:\\Users\\ahmed\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\', 'C:\\Users\\ahmed\\AppData\\Local\\Programs\\Python\\Python37\\']
os.getpid()     #Return the current process id.
os.getppid()    #Return the parent’s process id.
os.getlogin()   #Return the name of the user logged in 
#print("hi", os.getlogin())

#small explaination about process id
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
info('function f')

#remane file

import random
filename = str(int(random.random() * 10000000)) + ".txt"
with open(filename, "w") as f:
    f.write("")
os.rename(filename,"change" + filename) #if the new file name already exist you will get an error
filename = "change" + filename
os.remove(filename)
#print(os.name)


#os._exit(n) #Exit the process with status n
#os.kill(int(os.getppid()),1) #stop the whole python
#os.kill(int(os.getpid()),1)  #restart shell

#send commands
#os.system("dir")

os.times()   #Returns the current global process times.
'''
 •user - user time
 •system - system time
 •children_user - user time of all child processes
 •children_system - system time of all child processes
 •elapsed - elapsed real time since a fixed point in the past

'''

#io — Core tools for working with streams
filename = "newfile.txt"
with open(filename,"w") as f:
    f.write("Hello World")
f = open(filename,"r")
f.tell()
if(f.seekable()):#check if you can seek stream
    f.seek(1)
    f.read(1)
f.close()
os.remove(filename)

import time
#print(time.process_time_ns())


#argparse — Parser for command-line options, arguments and sub-commands
"""
import argparse
#to display help use -h --help

#provide main details about the program
#prog is used to define the pythonfilename that will be displayed in the help, if not defined the current filename will be used
#usage is used to define the row after the word usage in the discription    ... usage = "%(prog)s [OPTION]:"
#epilog to display a small message after the description
parser = argparse.ArgumentParser(description='Process some integers.',prog='myprogram', epilog = "small message after description")

#add an arg named integers and will be displayed as N , of type integer, and has the help message an integer for the accumulator
#default provides the defau;t value for the arg, None if not specified
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator',default = 1)

#add a switch named --sum to the main function accumulate that will sum the input if is was used:
#python pyfn.py --sum 1 2 3
#and will give the max only in not called
#python pyfn.py 1 2 3
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
try:
    #get the args
    args = parser.parse_args()
    #apply the function accumulate on the args called integers
    print(args.accumulate(args.integers))
finally:
    pass
"""

#getpass — Portable password input
import getpass
#password = getpass.getpass(prompt="enter password") # works only on shell
#user = getpass.getuser()
#print(user, password)

#platform — Access to underlying platform’s identifying data
import platform
'''
#Methiod #Desc $Example                                         
platform.machine() #Returns the machine type $ AMD64
platform.node() #Returns the computer’s network name $IK-PC
platform.processor() #Returns the (real) processor name $Intel64 Family 15 Model 4 Stepping 3, GenuineIntel
platform.release()  #Returns the system’s release, e.g. '2.2.0' or 'NT' An empty string is returned if the value cannot be determined.
platform.system() #Returns the system/OS name, e.g. 'Linux', 'Windows', or 'Java'. An empty string is returned if the value cannot be determined.
platform.version() #Returns the system’s release version, e.g. '#3 on degas'. An empty string is returned if the value cannot be determined.
platform.uname() #fairly portable uname interface. Returns a namedtuple() containing six attributes: system, node, release, version, machine, and processor.

platform.python_build() #tuple (buildno, builddate) $('tags/v3.7.2:9a3ffc0492', 'Dec 23 2018 23:09:28')
platform.python_branch() #Python implementation SCM branch. $tags/v3.7.2
platform.python_implementation() #Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.
platform.python_revision() #the Python implementation SCM revision.
platform.python_version() #Python version as string 'major.minor.patchlevel'.
platform.python_version_tuple() #tuple (major, minor, patchlevel) of strings.

platform.java_ver() #Returns a tuple (release, vendor, vminfo, osinfo)
'''
import sys
print(sys.api_version)
sys.platform #platform identifier  $win32
sys.copyright #A string containing the copyright pertaining to the Python interpreter.
sys.version #3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]

#time delay
'''
import time
print("sleep...-_- for 10 secs")
time.sleep(10)
print("0_0 : hi")
'''


#typedef c
'''
from typing import NewType
UserId = NewType('UserId',dict)
some_id = UserId({"key1":"val1"})
some_id["key2"] = "val2"
print(some_id)
'''

#Python Runtime Services

__name__ == "__main__" # True only if run as a script
