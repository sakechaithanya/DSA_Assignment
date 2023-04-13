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
