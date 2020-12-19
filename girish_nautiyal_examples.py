# Write a program to merge two python dictionaries and print merged dictionary
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


# write a python function to concatenate two integers like string concatenation and return concatenated number as integer
def concat_two_numbers(num1, num2):
    combined_num = str(num1) + str(num2)
    return int(combined_num)


# With a given integral number n, write a program to generate a dictionary that contains (i, i*i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
n = 8
d = dict()
for i in range(1,n+1):
    d[i] = i*i*i
print(d)

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False

# Write a Python function to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10, 5, 2, 1]
  x = 0
  for i in range(9):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x


# Write a Python function to find the number of zeros at the end of a factorial of a given positive number.
def factendzero(n):
  x = n // 5
  y = x 
  while x > 0:
    x /= 5
    y += int(x)
  return y


# Write a Python function for Binary Search
def binary_search(l, num_find):
    '''
    This function is used to search any number.
    Whether the given number is present in the
    list or not. If the number is present in list
    the list it will return TRUE and FALSE otherwise.
    '''
    start = 0
    end = len(l) - 1
    mid = (start + end) // 2
    found = False
    position = -1
    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
    return (found, position)


# Write a Python function to remove leading zeros from an IP address
import re
regex = '\.[0]*'
def remove_leading_zeros(ip):
    modified_ip = re.sub(regex, '.', ip)
    return modified_ip


# Write a Python function to return binary value of a given integer
def int_to_bin(a):
  return bin(a)


# Write a Python function to return octal value of a given integer
def int_to_oct(a):
  return oct(a)


# Write a Python function to return hexadecimal value of a given integer
def int_to_hex(a):
  return hex(a)


# Write a Python program to typecast given input to integer
num = int(input("Input a value: "))
print(num)


# Write a Python program to typecast given input to float
num = float(input("Input a value: "))
print(num)


# Write a Python program to check/test multiple variables against a value
a = 10
b = 20
c = 30
if 10 in {a, b, c}:
  print("True")
else:
  print("False")  


# Write a Python class that will initiate a number, input a number and print the number
class Number:
	def __init__(self, num):
		self.num = num

	def inputNum(self):
		self.num = int(input("Enter an integer number: "))

	def printNum(self):
		print(self.num)


# Write a Python function to find the simple interest in Python when principle amount, rate of interest and time is given
def simple_interest(p,r,t):
    si = (p*r*t)/100
    return si


# Write a Python function to find the compound interest in Python when principle amount, rate of interest and time is given
def compound_interest(p,r,t):
    ci = p * (pow((1 + r / 100), t)) 
    return ci


# Write a Python function to check whether a person is eligible for voting or not based on their age
def vote_eligibility(age):
	if age>=18:
	    status="Eligible"
	else:
	    status="Not Eligible"
	return status


# Write a Python function to find the BMI for given weight and height of a person
def bmi_calculator(height, weight):
	bmi = weight/(height**2)
	return bmi

# Write a Python function to check whether a given number is perfect number or not
def perfect_number_checker(num):
    i = 2
    sum = 1
    while(i <= num//2 ) :
        if (num % i == 0) :
            sum += i
        i += 1
    if sum == num :
        return f'{num} is a perfect number'

    else :
        return f'{num} is not a perfect number'

# Write a Python function to find the maximum ODD number from a given list
def odd_max_checker(list1):
	maxnum = 0
	for num in list1:
	    if num%2 != 0:
	        if num > maxnum:
	            maxnum = num
	return maxnum


# Write a Python function to find the maximum EVEN number from a given list
def even_max_checker(list1):
	maxnum = 0
	for num in list1:
	    if num%2 == 0:
	        if num > maxnum:
	            maxnum = num
	return maxnum


# Write a Python function to print the root of the quadratic equation
def quadratic_root(A,B,C):
	import math
	d=((B**2)-4*A*C)

	if d>=0:
	    s=(-B+(d)**0.5)/(2*A)
	    p=(-B-(d)**0.5)/(2*A)
	    print(math.floor(s),math.floor(p))
	else:
	    print('The roots are imaginary')


# Write a Python program to print the calendar of any given year
import calendar
year=2020
print(calendar.calendar(year))


# Write a Python function to print whether the given Date is valid or not
def date_validator(d,m,y):
	import datetime 
	try:
		s=datetime.date(y,m,d)
		print("Date is valid.")
	except ValueError: 
		print("Date is invalid.")


# Write a Python function to find the N-th number which is both square and cube
def nth_sq_and_cube(N):
	R = N**6
	return R


# Write a Python function to check whether a number is a power of another number or not
def power_checker(a,b):
	import math
	s=math.log(a,b)
	p=round(s)
	if (b**p)==a:
	    return f'{a} is the power of {b}.'
	else:
	    return f'{a} is NOT the power of {b}.'


# Write a Python function to 
def binary_palindrome(n):
	s=int(bin(n)[2:])
	r=str(s)[::-1]
	if int(r)==s:
	    return "The binary representation of the number is a palindrome."
	else:
	    return "The binary representation of the number is NOT a palindrome."


# Write a Python program to print the list of all keywords
import keyword
print("Python keywords are...")
print(keyword.kwlist)


# Write a Python function to find the intersection of two arrays
def array_intersection(A,B):
	inter=list(set(A)&set(B))
	return inter


# Write a Python function to find the union of two arrays
def array_union(A,B):
	union=list(set(A)|set(B))
	return union


# Write a Python program that prints a new set with all items from both sets by removing duplicates
# ---------------------------------------------------------
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))


# Write a Python program that Given two Python sets, update first set with items that exist only in the first set and not in the second set
# ---------------------------------------------------------
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference_update(set2))


# Write a Python program that prints a set of all elements in either A or B, but not both
# ---------------------------------------------------------
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))


# Write a Python program that determines whether or not the following two sets have any elements in common. If yes display the common elements
# ---------------------------------------------------------
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))


# Write a Python function to print number with commas as thousands separators 
def formattedNumber(n):
  return ("{:,}".format(n))


# Write a Python program to find the total number of uppercase and lowercase letters in a given string
str1='TestStringInCamelCase'
no_of_ucase, no_of_lcase = 0,0
for c in str1:
    if c>='A' and c<='Z':
        no_of_ucase += 1
    if c>='a' and c<='z':
        no_of_lcase += 1

print(no_of_lcase)
print(no_of_ucase)


# Write a Python program to find the total number of letters and digits in a given string
str1='TestStringwith123456789'
no_of_letters, no_of_digits = 0,0
for c in str1:
  no_of_letters += c.isalpha()
  no_of_digits += c.isnumeric()

print(no_of_letters)
print(no_of_digits)


# Write a Python function to count occurrence of a word in the given text
def text_searcher(text, word):
    count = 0
    for w in text.split():
        if w == word:
            count = count + 1
    return count


# Write a Python function to capitalizes the first letter of each word in a string
def capitalize(text):
  return text.title()


# Write a Python function to remove falsy values from a list
def newlist(lst):
  return list(filter(None, lst))


# Write a Python function to to find the sum of all digits of a given integer
def sum_of_digits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sum_of_digits(int(num / 10))


# Write a Python function to check all elements of a list are the same or not
def check_equal(a):
  return a[1:] == a[:-1]


# Write a Python program to convert string into a datetime object
from datetime import datetime
date_string = "Mar 26 2021  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)


# Write a Python function that returns the integer obtained by reversing the digits of the given integer
def reverse(n):
    s=str(n) 
    p=s[::-1]
    return p 


# Write a Python program that updates set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)


# Write a Python program that removes items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)


# Write a Python program to reverse a tuple
aTuple = (10, 20, 30, 40, 50)
aTuple = aTuple[::-1]
print(aTuple)


# Write a Python program to swap two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)


# Write a Python program to modify the second item (33) of a list inside a following tuple to 333
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][1] = 333
print(tuple1)


# Write a Python program to sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)


# Write a Python function to check if all items in the following tuple are the same
def check_tuple_same(sampleTuple):
    return all(i == sampleTuple[0] for i in sampleTuple)


# Write a Python program to print current time in milliseconds
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)


# Write a Python function func1() such that it can accept a variable length of  argument and print all arguments value
def func1(*args):
    for i in args:
        print(i)

# Write a Python program that Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

# Write a Python function that Given a string, display only those characters which are present at an even index number
def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )


# Write a Python function that Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
def removeChars(str, n):
  return str[n:]


# Write a Python function that Given a list of numbers, return True if first and last number of a list is same
def isFirst_And_Last_Same(numberList):
    firstElement = numberList[0]
    lastElement = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False


# Write a Python function that Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def findDivisible(numberList):
    for num in numberList:
        if (num % 5 == 0):
            print(num)


# Write a Python function that Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
def mergeList(list1, list2):
    thirdList = []
    for num in list1:
        if (num % 2 != 0):
            thirdList.append(num)
    for num in list2:
        if (num % 2 == 0):
            thirdList.append(num)
    return thirdList


# Write a Python program to return a set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))


# Write a Python program to Subtract a week ( 7 days) from a given date in Python 
from datetime import datetime, timedelta
given_date = datetime(2020, 2, 25)
days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print(res_date)


# Write a Python program to Find the day of week of a given date
from datetime import datetime
given_date = datetime(2020, 7, 26)
print(given_date.strftime('%A'))


# Write a Python program to Convert following datetime instance into string format
from datetime import datetime
given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)


# Write a Python program to convert two equal length sets to dictionary
keys = {'Ten', 'Twenty', 'Thirty'}
values = {10, 20, 30}
sampleDict = dict(zip(keys, values))
print(sampleDict)



# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))


# Write a program that will determine the object type

def typeIdentifier(object):
  return f'object type : {type(object)}'

# Write a Python class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. 

class IOString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = IOString()
strObj.getString()
strObj.printString()


# Write a program that will determine the memory usage by python process
import os, psutil
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

# Write a function that will provide the ascii value of a character

def charToASCII(chr):
  return f'ASCII value of {chr} is: {ord(chr)}'
  
# Write a function to reverse a string

def revStr(inp):
  inp = inp[::-1]
  return inp

# Write a function to determine the bits used by any number

def totalBits(n):
	return f'total number of bits used in {n} is : {len(bin(n)[2: ])}'


# write a function to find the sum of Sine series

import math
def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine


# Write a function to determine whether a given number is even or odd recursively

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!")


# Write a program to swap two variables inplace
a,b = b,a

# Write a program that prints the words in a comma-separated sequence after sorting them alphabetically.

items=[x for x in input().split(',')]
items.sort()
print(','.join(items))


# Write a function that takes a base and a power and finds the power of the base using recursion.

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))


# Write a function to repeat M characters of a string N times

def multTimes(str, m, n):
    front_len = m
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]
    result = ''
    for i in range(n):
        result = result + front
    return result
print (multTimes('Hello', 3, 7))


# Write a function that will convert a string into camelCase

from re import sub
def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]


# Write a function to remove empty list from a list using list comprehension
def removeEmptyList(li):
  res = [ele for ele in li if ele != []] 
  return res


# Write a function to Find the size of a Tuple in Python without garbage values
Tuple = (10,20)
def sizeOfTuple(tup):
  return f'Size of Tuple: {str(Tuple.__sizeof__())} bytes' 

# Write a function, which will find all such numbers between 1000 to 9999 that each digit of the number is an even number.

values = []
for i in range(1000, 9999):
  s = str(i)
  if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
      values.append(s)


# Write a function that finds a list is homogeneous 

def homoList(li):
  res = True
  for i in li: 
      if not isinstance(i, type(li[0])): 
          res = False 
          break
  return res


# Write a function to remove a given date type elements from a list.

def removeDataType(li,dType):
    res = []
    for i in li:
        if not isinstance(i, dType):
            res.append(i)
    return res


# Write a python function to find out the occurence of "i" element before first "j" in the list

def firstOccurence(arr, i,j):
  res = 0
  for k in arr:         
      if k == j: 
          break
      if k == i: 
          res += 1
  return res


# Write a program to check whether a file/path/direcory exists or not
file_path = "path/here"
import os.path
os.path.exists(file_path)


# Write a program to merge two python dictionaries
x={'key1':'val1','key2':'val2'}
y={'key3':'val3','key4':'val4'}
z = {**x, **y} # z = x | y  


# Write a program to convert dictionary into JSON
import json
data = {"key1" : "value1", "key2" : "value2"}
jsonData = json.dumps(data)
print(jsonData)

# Write a program to find common divisors between two numbers in a given pair
def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i
        i+=1
    return gcd
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

# Write a function to Check whether following json is valid or invalid
import json
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

# Write a function to remove and print every third number from a list of numbers until the list becomes empty
def remove_nums(int_list):
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1


# Write a program to take a string and print all the words and their frequencies
string_words = '''This assignment is of 900 marks. Each example if 9 marks.
If your example is similar to someone else, then you score less.
The formula we will use is 9/(repeated example). That means if 9 people write same example,
then you get only 1. So think different! (if examples are mentioned here and in the sample file, you will score less)'''
word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))


# Write a program to get a list of locally installed Python modules
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)

# Write a function to create all possible permutations from a given collection of distinct numbers
def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

# Write a function to add two positive integers without using the '+' operator
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a

# Write a program to find the median among three given number
x=10
y=20
z=30
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
elif y < z and z < x:
    print(z)    
elif x < z and z < y:
    print(z)

# Write a function to count the number of carry operations for each of a set of addition problems
def carry_number(x, y):
  ctr = 0
  if(x == 0 and y == 0):
    return 0
  z = 0  
  for i in reversed(range(10)):
      z = x%10 + y%10 + z
      if z > 9:
        z = 1
      else:
        z = 0
      ctr += z
      x //= 10
      y //= 10
  if ctr == 0:
    return "No carry operation."
  elif ctr == 1:
    return ctr
  else:
    return ctr

# Write a program to compute the number of digits in multiplication of two given integers
a,b = 312, 410
print(len(str(a*b)))

# Write a function to return the area of a rhombus
def area(d1, a): 
    d2 = (4*(a**2) - d1**2)**0.5
    area = 0.5 * d1 * d2 
    return(area) 

# Write a function that Given a number, find the most significant bit number which is set bit and which is in power of two
def setBitNumber(n): 
    if (n == 0): 
        return 0
    msb = 0 
    n = int(n / 2) 
    while (n > 0): 
        n = int(n / 2) 
        msb += 1
    return (1 << msb) 

# Write a function to calculate volume of Triangular Pyramid
def volumeTriangular(a, b, h): 
    return (0.1666) * a * b * h 
  
# Write a function to calculate volume of Square Pyramid  
def volumeSquare(b, h): 
    return (0.33) * b * b * h 
  
# Write a function to calculate Volume of Pentagonal Pyramid  
def volumePentagonal(a, b, h): 
    return (0.83) * a * b * h 
  
# Write a function to calculate Volume of Hexagonal Pyramid  
def volumeHexagonal(a, b, h): 
    return a * b * h