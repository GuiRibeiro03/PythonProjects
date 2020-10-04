import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"


all=lower+upper+numbers
len=16
password = "".join(random.sample(all,len))
print(password)