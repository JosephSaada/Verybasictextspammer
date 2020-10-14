import pyautogui, time
time.sleep(5)
f = open("Spamtextp2", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.750)





