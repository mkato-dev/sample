import pyautogui
import time

start_time = time.time()
DURATION_SECONDS = 3600  # 1時間で終了
INTERVAL_SECONDS = 300

try:
    while True:

        if time.time() - start_time > DURATION_SECONDS:
            print("1 hour passed. Program will exit.")
            break

        try:
            pyautogui.keyDown('ctrl')
            time.sleep(0.05)
            pyautogui.keyUp('ctrl')
            print("Pressed Ctrl to prevent sleep.")
            
        except Exception as e:
            print("Failed to press Ctrl:", e)

        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("Program exited by user.")