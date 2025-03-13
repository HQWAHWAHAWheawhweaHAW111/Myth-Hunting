import pyautogui

def click_on(x, y):
    pyautogui.click(x, y)

def type_text(text):
    pyautogui.write(text, interval=0.1)

if __name__ == "__main__":
    click_on(100, 100)  # Example: Clicking at coordinates (100, 100)
    type_text("Hello, AI automation in action!")
