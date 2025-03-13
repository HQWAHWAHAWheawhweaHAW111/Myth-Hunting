from modules.screen_capture import capture_screen
from modules.ocr_processing import extract_text
from modules.ai_assistant import ask_ai
from modules.automation import click_on, type_text

def main():
    # Capture screen
    print("Capturing screen...")
    image_path = capture_screen()
    print(f"Screen saved to: {image_path}")

    # Extract text from the screenshot
    print("Extracting text from the screen...")
    text = extract_text(image_path)
    print(f"Extracted text: {text}")

    # Ask AI about the extracted text
    print("Asking AI about the extracted text...")
    ai_response = ask_ai(text)
    print(f"AI Response: {ai_response}")

    # Example of automation (you can customize this)
    print("Automating screen interaction...")
    click_on(100, 100)  # Example coordinates (clicking on screen)
    type_text(ai_response)  # Type the AI response

if __name__ == "__main__":
    main()

enable_automation = False  # Set this to False to disable automation
