import string
import random
s1=string.ascii_lowercase
# print(s1)
s2=string.digits
# print(s2)
s3=string.punctuation
# print(s3)
s4=string.ascii_uppercase
# print(s3)
plenght=int(input("enter password length: "))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
random.shuffle(s)
print("your password is:")
print("".join(s[0:plenght]))
