import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "[]{}*;/,.-_"

all = lower + upper + nums + symbols
length = input("enter the length :")
length = int(length)
password = "".join(random.sample (all,length))
print ("password is :",password)