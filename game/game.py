from random import randint as r

while True:
    try:
        i = int(input("Level: "))
        if i > 0:
            break
    except:
        pass

ar = r(1, i)

while True:
    try:
        a = int(input("Guess: "))
        if a != 0:
            if a < ar:
                print("Too small!")
            elif a > ar:
                print("Too large!")
            else:
                print("Just Right!")
                break
    except:
        pass
