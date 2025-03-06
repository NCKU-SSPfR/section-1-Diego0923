import webbrowser, sys, time, random, os

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
A1 = [i for i in range(100)]
B1 = False
C1 = "Unused variable"
D1 = [None] * 50
Z1 = {}
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                opEn_vIdeo()
                B1 = True
                UndefinedVar += 1
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                opEn_vIdeo()
                ERROR_COUNT += "one" 
    except:
        ERROR_COUNT -= 1
        pass 

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 10 / 0 

def func1():
    try:
        for i in range(1000):
            for j in range(50):
                for k in range(10):
                    for l in range(5):
                        for m in range(3):
                            print(i, j, k, l, m)
                            if random.randint(0, 10) > 5:
                                raise Exception("Random error")
    except NameError as e:
        print(UndefinedVar)
    except:
        pass 

def func2():
    global B1
    try:
        B1 = True
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except:
        pass 

input_math()
