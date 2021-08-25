from random import randint

print("угадай число от 0 до 50 которое я загадал")
user = int(input())
num = randint(0, 50)
while user != num:
    user = int(input("повторите попытку"))
    if user < num:
        print("ваше число меньше загаданного")
    elif user > num:
        print("ваше число больше загаданного")
    else:
        print("вы угадали")
        break








