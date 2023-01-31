The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) Shantis-MacBook-Pro:datafun-03-datatypes shantikandel$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.7.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: #lists ..Creating list (List typically stores homogenous data)

In [2]:  c = [-45, 6, 0, 72, 1543]

In [3]: c
Out[3]: [-45, 6, 0, 72, 1543]

In [4]: #assessing elements of the list 

In [5]: c[0]
Out[5]: -45

In [6]: c[4]
Out[6]: 1543

In [7]: #determining the list's length

In [8]: len(c)
Out[8]: 5

In [9]: #Accesing elements from the end of the list with Negative Indices

In [10]: c[-1]
Out[10]: 1543

In [11]: c[-5]
Out[11]: -45

In [12]: #indices must be integers and Integer Expresions 

In [13]: a = 1

In [14]: b = 2

In [15]: c[a+b]
Out[15]: 72

In [16]: Lists are mutable
  Cell In[16], line 1
    Lists are mutable
          ^
SyntaxError: invalid syntax


In [17]: #lists are muatable

In [18]: c[4]=17

In [19]: c
Out[19]: [-45, 6, 0, 72, 17]

In [20]: #some sequence are Immutable

In [21]: s = 'hello'

In [22]: s[0]
Out[22]: 'h'

In [23]: s[0] = 'H'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 s[0] = 'H'

TypeError: 'str' object does not support item assignment

In [24]: #Using list elements in expressions

In [25]: x[0] +c[1] +c[2]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[25], line 1
----> 1 x[0] +c[1] +c[2]

NameError: name 'x' is not defined

In [26]: c[0] + c[1] +c[2]
Out[26]: -39

In [27]: #Appending to a list with +=

In [28]: a_list = []

In [29]: for number in range(1,6):
    ...:     a_list += [number]
    ...: 

In [30]: a_list
Out[30]: [1, 2, 3, 4, 5]

In [31]: letters =[]

In [32]: letters += 'Python'

In [33]: letters
Out[33]: ['P', 'y', 't', 'h', 'o', 'n']

In [34]: #Concatenating lists with +

In [35]: list1 =[10,20,30]

In [36]: list2 =[40, 50]


In [40]: concatenated_list = list1 + list2

In [41]: concatenated_list
Out[41]: [10, 20, 30, 40, 50]

In [42]: #using for and range to access list indices and values

In [43]: for i in range(len(concatenated_list)):
    ...:     print(f'{i}: {concatenated_list[i]}')
    ...: 
0: 10
1: 20
2: 30
3: 40
4: 50

In [44]: #comparison operators

In [45]: a =[1, 2, 3]

In [46]: b=[1, 2, 3]

In [47]: c=[1, 2, 3, 4]

In [48]: a == b #true: corresponding elements in both are equal
Out[48]: True

In [49]: a==c #false: a and c have different elements and lenght
Out[49]: False

In [50]: a < c #True: a has fwewer elements than c
Out[50]: True

In [51]: c >= b #True: elements 0-2 are equal but c has more elements
Out[51]: True

In [52]: #Tuples

In [53]: #creating tUOPLES

In [54]: #CREATING TUPLES

In [55]: student_tuple = ()

In [56]: student_tuple
Out[56]: ()

In [57]: len(student_tuple)
Out[57]: 0

In [58]: student_tuple = 'John', 'Green', 3.3

In [59]: student_tuple
Out[59]: ('John', 'Green', 3.3)

In [60]: len
Out[60]: <function len(obj, /)>

In [61]: len(student_tuple)
Out[61]: 3

In [62]: #Accessing Tuple Elements

In [63]: time_tuple = (9, 16, 1)

In [64]: time_tuple
Out[64]: (9, 16, 1)

In [65]: time_tuple[0] * 3600 + time_tuple[1]+ time_tuple[2]
Out[65]: 32417

In [66]: #Adding items to a String or tuples

In [67]: tuple1 = (10, 20, 30)

In [68]: tuple2 = tuple1

In [69]: tuple2
Out[69]: (10, 20, 30)

In [70]: tuple1 += (40, 50)

In [71]: tuple1
Out[71]: (10, 20, 30, 40, 50)

In [72]: tuple2
Out[72]: (10, 20, 30)

In [73]: #Appending Tuples to list

In [74]: numbers = [1, 2, 3, 4, 5]

In [75]: numbers += (6, 7)

In [76]: numbers
Out[76]: [1, 2, 3, 4, 5, 6, 7]

In [77]: #Unpacling sequences

In [78]: #unpacking sequences

In [79]: student_tuple = ('Amanda', [98, 85, 87])

In [80]: first_name, grades = student_tuple

In [81]: first_name
Out[81]: 'Amanda'

In [82]: grades
Out[82]: [98, 85, 87]

In [83]: #create the list names conatining three name strings

In [84]: names = ['Amanda', 'Sam', 'David']

In [85]: for i, name in enumerate(names):
    ...:     print(f'{i}: {name}')
    ...: 
0: Amanda
1: Sam
2: David

In [86]: #Sequence Slicing

In [87]: numbers = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

In [88]: numbers[2:6]
Out[88]: [5, 7, 9, 11]

In [89]: #specifying a slice with only an Ending Index

In [90]: numbers[:6]
Out[90]: [2, 3, 5, 7, 9, 11]

In [91]: numbers[0:6]
Out[91]: [2, 3, 5, 7, 9, 11]

In [92]: #specifying a slice with no indices

In [93]: numbers[:]
Out[93]: [2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

In [94]: #slicing with steps

In [95]: numbers[::2]
Out[95]: [2, 5, 9, 13, 17]

In [96]: #slicing with negative indices and steps

In [97]: numbers[::-1]
Out[97]: [19, 17, 15, 13, 11, 9, 7, 5, 3, 2]

In [98]: #Modifying list via Slices

In [99]: numbers[0:3] = ['two', 'three', 'five']

In [100]: numbers
Out[100]: ['two', 'three', 'five', 7, 9, 11, 13, 15, 17, 19]

In [101]: #Del statement

In [102]: numbers = list(range(0, 10))

In [103]: numbers
Out[103]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [104]: del numbers[-1]

In [105]: numbers
Out[105]: [0, 1, 2, 3, 4, 5, 6, 7, 8]

In [106]: #deleting the slice from a list

In [107]: del numbers[0:2]

In [108]: numbers
Out[108]: [2, 3, 4, 5, 6, 7, 8]

In [109]: del numbers[::2]

In [110]: numbers
Out[110]: [3, 5, 7]

In [111]: Deleting slice representing the entire list
  Cell In[111], line 1
    Deleting slice representing the entire list
             ^
SyntaxError: invalid syntax


In [112]: #deleting slice representing the entire list

In [113]: del numbers[:]

In [114]: numbers
Out[114]: []

In [115]: #Sortung lists

In [116]: numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

In [117]: numbers.sort()

In [118]: numbers
Out[118]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [119]: #Sorting a list in descending order

In [120]: numbers.sort(reverse=True)

In [121]: numbers
Out[121]: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

In [122]: #FILTER, MAP AND REDUCE

In [123]: #Filtering a Sequence's Values with the buid-In filter Function

In [124]: numners = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

In [125]: def is_odd(x)
  Cell In[125], line 1
    def is_odd(x)
                 ^
SyntaxError: invalid syntax


In [126]: def is_odd(x):
     ...:     """Returns True only if x is odd"""
     ...:     return x % 2!= 0
     ...: 

In [127]: list(filter(is_odd, numbers))
Out[127]: [9, 7, 5, 3, 1]

