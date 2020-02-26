import mcpi.minecraft
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()

rawMessage = ''
length = 0
isStarted = False
#This somehow detects key presses, I don't know how.
def on_press(key):
    #This used to print something.
    
def on_release(key):
    global rawMessage, isStarted
    if key != Key.enter:
        if isStarted == True:
            rawMessage = rawMessage + '{0}'.format(key)
    else:
        if isStarted == False:
            isStarted = True
            print('Recording started')
        else:
            isStarted = False
            print('Recording stopped, message sent')
            i = 0
            messagelist = list(rawMessage)
            for char in messagelist:
                if char in "'":
                    messagelist[i] = ''
                i += 1
            rawMessage = ''.join(messagelist)
            filteredMessage = rawMessage.replace('Key.space', ' ')
            print(filteredMessage)
            mc.postToChat(filteredMessage)
            rawMessage = ''
    

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()