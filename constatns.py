import pyautogui as mouse 


def moveMouse(parameter):
    ammt = parameter

    while ammt > 0:
        mouse.moveRel(10)
        mouse.moveRel(None, 10)
        print('moving mouse')
        ammt = ammt - 1    

    print('finish')


def findItemsToClick():
    mouse.move(0 , 20)


