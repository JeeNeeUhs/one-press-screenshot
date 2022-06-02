from pynput import keyboard
import pyautogui as pg

x = 1
def on_press(key):
    global x
    try:
        k = key.char 
    except:
        k = key.name
    if k == 'esc':  #exit button
        exit()
    elif k == 'q':  #this is ScreenShot button
                    #can change another button
        pg.screenshot(str(x)+'.png') 
        x += 1

if __name__ == '__main__':
    lstnr = keyboard.Listener(on_press=on_press)
    lstnr.start()
    lstnr.join()