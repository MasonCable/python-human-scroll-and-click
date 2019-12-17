from selenium import webdriver
import pyautogui as mouse
import time

def humanMouse():
    move = 40

    for i in move:
        mouse.moveTo(10, 20)

class ExplorePage:
    def __init__(self, scrollTime, link):
        self.scrollTime = scrollTime
        self.link = link
    
    def openBrowser(self):
        link = self.link
        scrollTime = self.scrollTime

        browser = webdriver.Firefox()
        browser.get(link)
        time.sleep(scrollTime)
        # mouse.moveTo(100, 200)
        humanMouse()
        time.sleep(scrollTime)
        print('This worked')

start = ExplorePage(5, 'https://ubuntu.com/')
start.openBrowser()