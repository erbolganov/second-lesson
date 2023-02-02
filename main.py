
# 1
a = int(input("a= "))
if a == 10:
    print("true")
else: print("false", f"{a} is not equal 10")

print("-----------------------------------------------")

# 2
min = int(input("enter number: "))

if min >= 0 and min < 15:
    print(" min in 1st quarter")
elif min >= 15 and min < 30:
    print(" min in 4th quarter")
elif min >= 30 and min < 45:
    print(" min in 3rd quarter")
else: print("min in 2nd quarter")

print("-----------------------------------------------")

# 3
a = int(input("a= "))
if a > 1:
    print("a is bigger than 1")
else: print("a is not bigger than  1")

print("-----------------------------------------------")

# 5
name = input("What is your name? ")
if name != '':
    print(f"Hello {name}")
elif name == '':
    print(f"Hello stranger")

print("-----------------------------------------------")

# 6

a = int(input('Enter pin: '))
if a == 9583 or a == 1747:
    print("доступны модули баз А, В и С")
elif a == 3331 or a == 7922:
    print("доступны модули баз В и С")
elif a == 9455 or a == 8997:
    print("доступны модуль базы С")