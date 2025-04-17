import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*()-_+={}[];:?/><.,"
all_char=lower+upper+number+symbol
leng=int(input("enter length:"))
password=' '.join(random.sample(all_char,leng))
print("GENERATE PASSWORD:",password)
