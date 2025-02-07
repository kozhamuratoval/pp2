''' 1
def function(grams):
    ounces = 28.3495231 * grams
    print(ounces)
a = int(input())
function(a)''' 

''' 2 
def FahTemp(F):
    c = (5/9) * (F - 32)
    print(c)
a = int(input())
FahTemp(a)
'''

'''3
def func(numheads, numlegs):
    y=(numlegs-2*numheads)//2
    x =numheads-y
    if x <0 or y<0 or 2*x+4*y!= numlegs:
        print("No valid solution")
    else:
        print(f"Chickens {x}, Rabbits {y}")
func(35, 94)
''' 

'''4
import random
ee = []
for i in range(10):
    a = random.randint(1, 30)
    ee.append(a)
print(ee)
print()
def filter_prime(a):
    for i in a:
        count = 0
        for e in range(1,i):
            if i % e == 0:
                count+=1
        if count >= 2:
            continue
        else:
            print(i)
filter_prime(ee)'''


''' 5
from itertools import permutations

def func(s):
    a = permutations(s) 
    for i in a:
        print(''.join(i))
str = input()
func(str) 
'''

''' 6 
def reverse_words(sent):
    words = sent.split()
    reversed =words[::-1]
    reversed=' '.join(reversed)
    return reversed
a = input("Enter a sentence: ")
reversed = reverse_words(a)
print("Reversed sentence:", reversed)
'''

''' 7 
def func(a):
    for i in range(len(a)-1):
        if a[i]==3 and a[i + 1]== 3:
            return True
    return False
print(func([1, 3, 3]))       
print(func([1, 3, 1, 3]))  
print(func([3, 1, 3]))      
print(func([3, 3, 1]))     
print(func([1, 2, 3, 4, 5]))
'''

''' 8 
def func(nums):
    sequence=[0, 0, 7]
    index=0  
    for num in nums:
        if num==sequence[index]:
            index +=1  
            if index ==len(sequence):
                return True
    return False
print(func([1, 2, 4, 0, 0, 7, 5]))  
print(func([1, 0, 2, 4, 0, 5, 7]))  
print(func([1, 7, 2, 0, 4, 5, 0])) 
print(func([0, 0, 7, 1, 2, 3]))    
print(func([0, 7, 0, 7]))   
'''

''' 9 
def func(radius):
    vol= (4/3)*3.14*(radius ** 3)
    return vol
radius = float(input())
print(func(radius))
'''

''' 10
def unique_elements(a):
    unique=[]
    for item in a:
        if item not in unique:
            unique.append(item)
    return unique
e=[1, 2, 2, 3, 4, 4, 5]
print(unique_elements(e))
'''

''' 11 
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
example = input()
print(is_palindrome(example)) 
'''


''' 12
def histogram(lst):
    for num in lst:
        print("*" * num)
a = int(input())
b = int(input())
c = int(input())
histogram([a, b, c])
'''

''' 13
import random
def func():
    print("Hello! What is your name?")
    name=input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        print("Take a guess")
        guess = int(input())
        attempts += 1
        if guess<number:
            print("Your guess is too low")
        elif guess>number:
            print("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
func()
'''