import pyautogui
import time
import cv2
import numpy as np

def locate_accept_button():
    try:
        # Take a screenshot of the current screen
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Load the reference image of the accept button
        accept_button = cv2.imread("accept_button.jpg", cv2.IMREAD_UNCHANGED)

        # Convert both images to grayscale
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        accept_button_gray = cv2.cvtColor(accept_button, cv2.COLOR_BGRA2GRAY)

        # Use template matching to find the accept button in the screenshot
        result = cv2.matchTemplate(screenshot_gray, accept_button_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If the match is strong enough, return the location
        threshold = 0.8
        if max_val >= threshold:
            accept_button_w = accept_button.shape[1]
            accept_button_h = accept_button.shape[0]
            accept_button_center = (max_loc[0] + accept_button_w // 2, max_loc[1] + accept_button_h // 2)
            return accept_button_center
        else:
            return None
    except pyautogui.PyAutoGUIException as e:
        print(f"Error taking screenshot: {e}")
        return None

def main():
    while True:
        accept_button_location = locate_accept_button()
        if accept_button_location:
            pyautogui.click(accept_button_location)
            print("Match Accepted!")
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()