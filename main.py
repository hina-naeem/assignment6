from typing import List
# *Create a function* that takes an array, an index, and a value as parameters. Inside the function,
#  use the insert method to insert the value at the specified index in the array. Return the modified array.

def insert_intoarray(array,index,value):
    array.insert(index,value)
    return array
myArray:List[int] =[1,2,3,4,5,6]
indexNum:int=3
num:int=23
newArray:List[int]=insert_intoarray(myArray,indexNum,num)
print(newArray)

# #. *Implement a simple shopping cart program* using an array. Create functions to add items, remove items, and update quantities using array methods.
# #  Print the cart's contents after each operation.
def add_items(array:List[str],value:str):
    array.append(value)
    return array

def remove_items(array:List[str],value:str):
    array.remove(value)
    return array
def update(array:List[str],value:str,num:int):
    x:int=array.count(value)
    print (x)
    return array

cart_items:List[str]=["shirt","socks","tie","pants"]
print(cart_items)
cart_updated:List[str]=add_items(cart_items,"jeans")
print(cart_updated)
cart_updated=remove_items(cart_items,"socks")
print(cart_updated)
items_num:int=4
cart_updated=update(cart_items,"shoes",items_num) 
print(cart_items)   


# 3. *Write a program* that uses a while loop to print the first 25 integers.
number:int = 1
while number <= 25:
    print(number)
    number += 1

# 4. *Write a program* that uses a while loop to print the first 10 even numbers.

number:int=1
count:int =1
while count<=10:
    if(number%2==0):
        print(number)
    count += 1
    number += 1

# 5. *Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.
def factorial(num:int):
    result:int=1
    while(num>0):
        result=result*num
        num -= 1
    return result

number:int=int(input("enter the number to which to find factorial: " ))
x:int=factorial(number)
print(x)

# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
array:List[int]=[2,6,-3,0,78,-45,87]
positive_numbers = [num for num in array if num >= 0]
print(positive_numbers)

# 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.
def add_arraylist(array:List):
    sum:int=0
    i:int=0
    while i<len(array):
        sum=sum+array[i]
        i= i+1
    return sum
array:List[int]=[6,9,14,23]
sum = add_arraylist(array)
print(f"the sum of the list given is  {sum}")
# 8. *Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using
#  the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
i:int=0
tempArray:List[int]=[]
tempArray_f:List[int]=[]
while i<5:
    # tempArray[i]=int(input("enter the temperature in celsius:  "))
    tempArray.append(int(input("enter the temperature in celsius:  ")))
    tempArray_f.append(tempArray[i]*(9/5)+32)
    i=i+1
print(f"the list of celsius temperature is {tempArray}")
print(f"the list of fahrenheit temperature is {tempArray_f}")

# 9. *Write a program* to remove all the odd numbers from an array.
array:List[int]=[2,6,-3,0,78,-45,87]
positive_numbers = [num for num in array if num %2 != 0]
print(positive_numbers)