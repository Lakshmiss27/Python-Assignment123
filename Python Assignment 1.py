# 1. String Concatenation

str1 = "Hello "
name = input("Enter your Name: ")

str2 = str1 + name
print(str2)

str3 = "welcome to Python programming"
str4 = str2 + str3

print(str4)


# 2. String Slicing and Indexing

print("First character:", str3[0])
print("Last character:", str3[-1])
print("First 5 characters:", str3[0:5])
print("Last 11 characters:", str3[-11:])
print("Reverse string:", str3[::-1])

start = str3.find("Python")
print("Word Python:", str3[start:start+6])

#3. String Methods

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize the sentence
print("Capitalize:", strM.capitalize())

# d. Count occurrences of character 't'
print("Count of t:", strM.count('t'))

# e. Replace Python with Machine Learning
print("Replace:", strM.replace("Python", "Machine Learning"))


# 4. Tuples

# Creating two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat the elements 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("Third element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])


