# https://pynput.readthedocs.io/en/latest/keyboard.html

# https://github.com/moses-palmer/pynput/issues/105


#  todo
# how to stop endless loop?
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
    's': Key.down,
    'e': Key.enter,
    'q': Key.backspace
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
                print(key)
                listener._suppress = False
                keyboard.tap(keyActionMap.get(key.char))
                listener._suppress = True
        # else:
        #     print('else')
        #     listener._suppress = False
        #     keyboard.release(key.char)  
        #     listener._suppress = True
    
        

    except AttributeError as e:
        print('err')
        print(e)
        if key == Key.esc:
            exit()

def on_release(key):
    global caps
    print("on release: ", key)
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
    listener.joinw()

