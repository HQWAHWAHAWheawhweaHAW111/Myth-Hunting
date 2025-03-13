import pyautogui
import time

def capture_screen(output_path="screen.png"):
    time.sleep(1)  # Short delay before capture
    screenshot = pyautogui.screenshot()
    screenshot.save(output_path)
    return output_path

if __name__ == "__main__":
    print("Screenshot saved:", capture_screen())
