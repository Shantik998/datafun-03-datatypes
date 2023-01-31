The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) Shantis-MacBook-Pro:datafun-03-datatypes shantikandel$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.7.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: #creating a dictionary

In [2]: country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}

In [3]: country_codes
Out[3]: {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}

In [4]: #Determining dictionary is empty

In [5]: len(country_codes)
Out[5]: 3

In [6]: if country_codes:
   ...:     print('country_codes is not empty')
   ...:     else:
   ...:         print('country_codes is empty')
  Cell In[6], line 3
    else:
    ^
SyntaxError: invalid syntax


In [7]: if country_codes:
   ...:     print('country_codes is not empty')
   ...: else:
   ...:     print('country_codes is not empty')
   ...: 
country_codes is not empty

In [8]: Country_codes.clear()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 Country_codes.clear()

NameError: name 'Country_codes' is not defined

In [9]: country_codes.clear()

In [10]: if country_codes:
    ...:     print('country_codes is not empty')
    ...: else:
    ...:     print('country_codes is is empty')
    ...: 
country_codes is is empty

In [11]: #create a dictionary named states that maps three state abbreviations to their state name, then display the dictionary

In [12]: states = {'VT': 'Vermont', 'NH': 'New Hampshire', 'MA': 'Massachusetts'}

In [13]: states
Out[13]: {'VT': 'Vermont', 'NH': 'New Hampshire', 'MA': 'Massachusetts'}

In [14]: #Iterating through a Dictionary

In [15]: days_per_month = {'January': 31, 'February': 28, 'March': 31}

In [16]: days_per_month
Out[16]: {'January': 31, 'February': 28, 'March': 31}

In [17]: for month, days in days_per_month.items():
    ...:     print(f'{month} has {days} days')
    ...: 
January has 31 days
February has 28 days
March has 31 days

In [18]: #Basic dictionary operations

In [20]: roman_numerals= {'I':1, 'II':2, 'III':3, 'V':5, 'X':100}

In [21]: roman_numerals
Out[21]: {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

In [22]: Accesing the value associated with a key
  Cell In[22], line 1
    Accesing the value associated with a key
             ^
SyntaxError: invalid syntax


In [23]: Accesing the value associated with a key
  Cell In[23], line 1
    Accesing the value associated with a key
             ^
SyntaxError: invalid syntax


In [24]: #Accesing the value associated with a key

In [25]: roman_numerals['V']
Out[25]: 5

In [26]: #Adding a New Key-Value Pair

In [27]: roman_numerals['L']= 50

In [28]: roman_numerals
Out[28]: {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100, 'L': 50}

In [29]: #removing key value pair

In [30]: del roman_numerals['III']

In [31]: roman_numerals
Out[31]: {'I': 1, 'II': 2, 'V': 5, 'X': 100, 'L': 50}

In [32]: #Dictionary methods keys and values

In [33]: months = {'January':1, 'February':2, 'March':3}

In [34]: for month_name in months.keys():
    ...:     print(month_name, end='   ')
    ...: 
January   February   March   


In [37]: for month_number in months.values():
    ...:     print(month_number, end=' ')
    ...: 
1 2 3 


In [40]: month_view = months.keys()


In [43]: for month_number in months.values():
    ...:     print(month_number, end=' ')
    ...: 
1 2 3 
In [44]: #dictionary view

In [45]: months_view = months.keys()

In [46]: for key on months_view:
    ...:     print(key, end=' ')
  Cell In[46], line 1
    for key on months_view:
            ^
SyntaxError: invalid syntax


In [47]: for key on months_view:
    ...:     print(key, end=' ')
  Cell In[47], line 1
    for key on months_view:
            ^
SyntaxError: invalid syntax


In [48]: months_view = months.keys()

In [49]: for key in months_view:
    ...:     print(key, end=' ')
    ...: 
January February March 
In [50]: months['December'] = 12

In [51]: months
Out[51]: {'January': 1, 'February': 2, 'March': 3, 'December': 12}

In [52]: for key in months_view:
    ...:     print(key, end=' ')
    ...: 
January February March December 
In [53]: #Dictionalry comparisons

In [54]: country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}

In [55]: country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}

In [56]: country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussel'}

In [57]: country_capitals1 = country_capitals2


In [59]: country_capitals1 == country_capitals2
Out[59]: True

In [60]: country_capitals1 == country_capitals3
Out[60]: False

In [61]: country_capitals1 != country_capitals3
Out[61]: True