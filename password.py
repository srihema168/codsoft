import random
import array
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
len= int(input("Enter password length: "))
comb = lower+upper+special+digit
rd=random.choice(digit)
ru=random.choice(upper)
rl=random.choice(lower)
rs=random.choice(special)
temp_password = rd+ru+rl+rs
for _ in range(len - 4):
    temp_password += random.choice(comb)
temppasslist = array.array('u', temp_password)
random.shuffle(temppasslist)
password = ""
for i in temppasslist:
    password += i
print("Password:", password)