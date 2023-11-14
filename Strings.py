Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Strings : Series of Characters
#EXAMPLE: "This is a business deal"
#Example 2: 'This is a business deal'
First_name='Mohan Reddy'
print(First_name)
Mohan Reddy
Title=print(First_name.Title())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Title=print(First_name.Title())
AttributeError: 'str' object has no attribute 'Title'. Did you mean: 'title'?
Title=print(First_name.title())
Mohan Reddy
Title
Print(First_name.upper())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Print(First_name.upper())
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(First_name())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(First_name())
TypeError: 'str' object is not callable
print(First_name.upper())
MOHAN REDDY
print(First_name.lower())
mohan reddy
first_name='Mohan'
last_name='Reddy'#
SyntaxError: unterminated string literal (detected at line 1)
full_name = f"{first_name){last_name}"
SyntaxError: f-string: unmatched ')'
first_name="Mohan"
last_name="Reddy"
full_name = f"{first_name){last_name}"
SyntaxError: f-string: unmatched ')'
full_name = f"{first_name}{last_name}"
print(full_name.title())
Mohanreddy
first_name = 'Mohan'
last_name = 'Reddy'
full_name = first_name + last_name
print(full_name)
MohanReddy
#Now lets add some space between firt and last name
full_name = first_name + " "+last_name
print(full_name)
Mohan Reddy
#The above method of adding data types is called concatenation
#finding data types
name="Mohan"
type(name)
<class 'str'>
name='Mohan'
type(name)
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
len(name)
5
name[0]
'M'
name[0:3]
'Moh'
name[2:]
'han'
#print first letter of name
name[0]
'M'
#print second letter of name
name[1]
'o'
#print last letter of name
name[-1]
'n'
#print last two letters
name[-1:-2]
''
name[-1:0]
''
name[-2:-1]
'a'
name[-2::-1]
'ahoM'
name[-2:]
'an'
name[-3:]
'han'
 name[0::]
 
SyntaxError: unexpected indent
 name[0::3]
 
SyntaxError: unexpected indent
name[-1::3]
'n'
>>> name[-1::-3]
'no'
>>>  name[-1::-5]
...  
SyntaxError: unexpected indent
>>> name[-1::-4]
'nM'
>>> name[-1:-4]
''
>>> name[-4::-1]
'oM'
>>> #program = "python"programming"
SyntaxError: unterminated string literal (detected at line 1)
>>> #What happened in the above syntax is there is an undertermined string,the solution for this is we have to use either single quotes inside the string or use an escape sequence
>>> program = "pyhton'programming'"
>>> print(program)
pyhton'programming'
>>> program = "python"programming" # Here i will get an error beacuse the string is not identified
SyntaxError: unterminated string literal (detected at line 1)
>>> #lets try with few escape sequences
>>> #Examples are #/"
>>> #/'
>>> #//
>>> #/n
>>> program= "python /""programming"
>>> print(program)
python /programming
>>> program= "python /"programming"
SyntaxError: unterminated string literal (detected at line 1)
>>> program= "python \"programming"
>>> print(program)
python "programming
>>> program= "python \'programming"
>>> print(program)
python 'programming
>>> program= "python \\programming"
>>> print(python)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(python)
NameError: name 'python' is not defined
>>> print(program)
python \programming
>>> program= "python /n"programming"
SyntaxError: unterminated string literal (detected at line 1)











