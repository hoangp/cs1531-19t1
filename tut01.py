# print Hello World to standard output.
print("Hello World\n")

# loop through a list of names and print them to standard output.
names = ["A", "B", "C"]
for name in names:
    print(name)
print()

# For a given number, find the sum of n + n^2 + n^3 + … + n^n
def sumN(n): 
    sum = 0  
    for i in range(1, n + 1): 
        sum += n**i 
    return sum

n = int(input("Enter a number: "))
print("The sum of %d + %d^2 + %d^3 + … + %d^%d = %d\n" % (n,n,n,n,n,sumN(n)))

# Write a program that takes n words from a user 
# and outputs a string that contains all the words separated by a space. 
# n here is the number of words the user would like to input.
num_words = int(input("Enter number of words: "))
words = []
for i in range(num_words):
    words.append(input("Enter word %d: " % (i+1)))

sentence = ""
if num_words > 0:
    sentence = words[0]

for i in range(1, num_words):
    sentence += " " + words[i]

print(sentence)
print()

# Given a base-string and a sub-string, 
# find the number of different ways the sub-string appears in the base-string
s = input("Enter the complete string: ")
sub_str = input("Enter the sub-string: ")

n = 0
for i in range(len(s)-len(sub_str)+1):
    if s[i:i+len(sub_str)] == sub_str:
        n += 1
print(n)