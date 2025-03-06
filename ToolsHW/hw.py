import webbrowser, sys, time, random, os  

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
VIDEO_PLAYED = False     
ERROR_COUNT = 0

def input_math():
    global VIDEO_PLAYED, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                opEn_vIdeo()
                VIDEO_PLAYED = True
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
    webbrowser.open(VIDEO_URL)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 0 

input_math()
