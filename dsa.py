# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def PairSum(array, length, sum_):
    for i in range(length):
        for j in range(i, length):
            if (array[i] + array[j]) == sum_:
                print(array[i], array[j])


array = [-1, 8, 3, 11, 2, 7, 6, 4, 9]
sum_ = 10
length=len(array)
print("Array:", array)
print("Pairs whose sum is",sum_,"are:")
PairSum(array, length, sum_)
print("*"*50)
array_1 = [1, -3, -5, 7, -2, 3, -9]
sum_1 = -2
length_1=len(array_1)
print("Array:", array_1)
print("Pairs whose sum is",sum_1,"are:")
PairSum(array_1, length_1, sum_1)

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array.You have to update the original array.

def ReverseArray(array):
    return "The Reverse Array is:",array[::-1]
array = ["c","h","a","i","t","u"]
print("Original Array:", array)
print(ReverseArray(array))
print("*"*30)
array1 = [0,2,4,6,8]
print("Original Array:", array1)
print(ReverseArray(array1))

# Q3. Write a program to check if two strings are a rotation of each other?

def StringRotationCheck(s1, s2): 
    temp = '' 
    temp = s1 + s1 
    if s2 in temp: 
        return True 
    else: 
        return False
s1 = "ABACADABC"
s2 = "CDABABACD"
if StringRotationCheck(s1, s2): 
    print("Given Strings are a rotation of each other.")
else: 
    print("Given Strings are not a rotation of each other.")
print("*"*30)
s1_1 = "ABACD"
s2_2 = "CDABA"
if StringRotationCheck(s1_1, s2_2): 
    print("Given Strings are a rotation of each other.")
else: 
    print("Given Strings are not a rotation of each other.")
    
    
    
# Q4. Write a program to print the first non-repeated character from a string?

from collections import Counter
inp_str = input("Enter string: ")
counter = Counter(inp_str)
non_repeated = {inp_str.index(i):i for i in counter.keys() if counter[i] == 1}
if non_repeated:
  first_non_repeated = min(non_repeated.keys())
  print("first non-repeated character is", non_repeated[first_non_repeated])
else:
  print("all characters are repeated")


# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerHanoi(Disks, Source, Auxiliary, Target):  
    if(Disks == 1):  
        print ("Move Disk 1 from Source",Source,"To Destination",Target)
        return  
    TowerHanoi(Disks - 1, Source, Target, Auxiliary)  
    print ("Move Disk",Disks,"From Source",Source,"To Destination",Target)  
    TowerHanoi(Disks - 1, Auxiliary, Source, Target)  


Disks = int(input('Enter The Number of Disks: ')) 

TowerHanoi(Disks, 'Rod_A', 'Rod_B', 'Rod_C')

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

postfix = input("Enter postfix expression: ")
s = []
for i in postfix:
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(i+op2+op1)
print("prefix expression is",*s)


# Q7. Write a program to convert prefix expression to infix expression.

prefix = input("Enter prefix expression: ")
s = []
for i in reversed(prefix):
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(f"({op1}{i}{op2})")
print("infix expression is",*s)


# Q8. Write a program to check if all the brackets are closed in a given code snippet.

expression = input("Enter Brackets expression: ")
s = []
o = "{[("
c = "}])"
for i in expression:
    if i in o:
        s.append(i)
    else:
        if len(s) == 0:
            print("Not Balanced")
            break

        b = s.pop()
        if o.index(b) != c.index(i):
            print("Not Balanced")
            break
else:
    if len(s) == 0:
        print("Balanced")
    else:
        print("Not Balanced")
 
# Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.Elements = []
    def push(self, value):
        self.Elements.append(value)
    def pop(self):
        return self.Elements.pop()
    def empty(self):
        return self.Elements == []
    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)

stack = Stack()
stack.push(0)
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(8)
stack.push(10)
print("Original Stack")
stack.show()

print("\nStack after Reversing")
Reverse(stack)
stack.show()

# Q10. Write a program to find the smallest number using a stack.

stack = list(map(int, input("enter values of stack separated by space : ").split()))
small_num = stack.pop()
for _ in range(len(stack)):
  i = stack.pop()
  if i < small_num:
    small_num = i
print(f"smallest number in given stack is {small_num}")
