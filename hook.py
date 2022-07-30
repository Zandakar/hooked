# https://pynput.readthedocs.io/en/latest/keyboard.html


#  todo
# only on caps
#
#




from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
global listener
global caps

caps = False


keyActionMap =  {
    'w': Key.up,
    'a': Key.left,
    'd': Key.right,
    's': Key.down
}

def on_press(key):
    global caps
    try:
        print(key)

        if key == Key.caps_lock:    
            caps = True

        if caps == True:
            print('if caps true')
            if keyActionMap.get(key.char):
                print('if char')
                listener._suppress = False
                keyboard.press(keyActionMap.get(key.char))
                listener._suppress = True
        
            

    except AttributeError as e:
        # print(e)
        if key == Key.esc:
            exit()

def on_release(key):
    global caps
    if key == Key.caps_lock:
        # print("is caps release"  )
        caps = False
    if key == Key.esc:
        exit()



# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True) as listener:
    listener.join()


