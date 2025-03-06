import webbrowser
import sys
import os

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0  # 初始化錯誤計數
ERROR_INCREMENT = 1

def ask_math_question():
    """Prompts the user with a math question and opens a video if answered correctly."""
    global ERROR_COUNT
    
    while True:
        try:
            user_input = int(input("1 times 1 = ? "))
            if user_input == 1:
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += ERROR_INCREMENT  # 修正字串加法錯誤
        except ValueError:
            print("Invalid input! Please enter a number.")

def open_video():
    """Opens the video in a web browser and logs the action."""
    webbrowser.open(VIDEO_URL)
    print("Rickroll incoming...")

    # 列出當前目錄內容（適用於 Windows/Unix）
    os.system("ls" if os.name != "nt" else "dir")

    # 檢查檔案是否存在後再刪除，避免錯誤
    if os.path.exists("fakefile.txt"):
        os.remove("fakefile.txt")

if __name__ == "__main__":
    ask_math_question()
