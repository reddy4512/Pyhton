Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(name)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
print('name')
name
print("Mohan Reddy First start")
Mohan Reddy First start
First_prog = "Mohan Reddy"
print(first prog)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(First_Prog)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(First_Prog)
NameError: name 'First_Prog' is not defined. Did you mean: 'First_prog'?
print("First_prog")
First_prog
Print(First_prog)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Print(First_prog)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(First_prog)
Mohan Reddy
print(type(First-prog))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(type(First-prog))
NameError: name 'First' is not defined. Did you mean: 'list'?
print(type(First_prog))
<class 'str'>
First_name = "Mohan"
Last_name ="Reddy"
Full_name= First_name + Last name
SyntaxError: invalid syntax
Full_name= First_name + Last_name
print(Full_name)
MohanReddy
Full_name= First_name   +   Last_name
print(Full_name)
MohanReddy
print(Full_name)
MohanReddy
Full_name= First_name   + "   " + Last_name
print(Full_name)
Mohan   Reddy
#Type of the variable
print(type(Full_name))
<class 'str'>
#Definition of string : A string is a series of characters
#Now lets combine some variables together
#Note: We can only combine the strings if they are of same data type#
First_name = "Mohan"

Last_name ="Reddy"
SyntaxError: multiple statements found while compiling a single statement
Last_name ="Reddy"
Full_name= First_name   +   Last_name
print(Hi Mr +" "+Full_name)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(Hi Mr +" "+ "Full_name")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Hi Mr" + Full_name)
Hi MrMohanReddy
#When we use any variable to print make sure we dont use any quotes because...For instance i use a variable Full_name with quotes lets see what happens
print("Hi Mr" + "Full_name")
Hi MrFull_name
#Whatever the info we give in quotes it will be printed automatically
#Now lets Move to Integers
int=50
datatype(int)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    datatype(int)
NameError: name 'datatype' is not defined
>>> Age=55
>>> type(Age)
<class 'int'>
>>> int=55
>>> type(int)
<class 'int'>
>>> #We can decrease and increase the age lets start with few basic examples
>>> age=25
>>> age=age+1
>>> age
26
>>> #Here in the above example concatenation is possible because they are same data types
>>> #Method 2 of adding age
>>> age+=1
>>> age
27
>>> #Example 2:
>>> age =age+2
>>> age
29
>>> type(age)
<class 'int'>
>>> print("HI MY AGE IS-->"+" "+ age)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print("HI MY AGE IS-->"+" "+ age)
TypeError: can only concatenate str (not "int") to str
>>> #Here concatenation is not possible as they are different data types so we will convert the integer into string
>>> print("HI MY AGE IS-->"+" "+ str(age))
HI MY AGE IS--> 29
>>> my
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    my
NameError: name 'my' is not defined
>>> my_age=print("HI MY AGE IS-->"+" "+ str(age))
HI MY AGE IS--> 29
>>> my_age="HI MY AGE IS-->"+" "+ str(age))
SyntaxError: unmatched ')'
>>> my_age="HI MY AGE IS-->"+" "+ str(age)
>>> type(my_age)
<class 'str'>
