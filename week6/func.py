'''def m(numbers):
    result = 1
    for num in numbers:
        result *= num    
    return result
numbers = [2, 3, 4, 5]
product = m(numbers)
print(f"Product: {product}") '''

'''def m(string):
    upper_count = sum(1 for char in string if char.isupper()) 
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

text = "Hello World"
upper, lower = m(text)
print(f"Upper: {upper}") 
print(f"Lower: {lower}")'''

'''def m(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

test1 = "A man a plan a canal Panama"
test2 = "Hello"
print(f"'{test1}' is palindrome: {m(test1)}")  
print(f"'{test2}' is palindrome: {m(test2)}")'''

'''import math
import time
def m(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)  
    return result
number = float(input("Enter a number: "))
delay = float(input("Enter delay in milliseconds: "))

result = m(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")'''

'''def m(tuple_elements):
    return all(tuple_elements)  

tuple1 = (True, True, 1, "hello")  
tuple2 = (True, False, 1, "hello")
tuple3 = (True, 0, 1, "hello")      

print(f"Tuple1 all true: {m(tuple1)}") 
print(f"Tuple2 all true: {m(tuple2)}") 
print(f"Tuple3 all true: {m(tuple3)}") '''
