import keyboard

def onRelease(e):
    print("Released: " + e.name)

def onPress(e):
    if (e.name == 'E'):
        keyboard.send('b+l+a')
        print('captured E')

keyboard.on_press(onPress)
keyboard.on_release(onRelease)

while True:
    import time
    time.sleep(1000)
