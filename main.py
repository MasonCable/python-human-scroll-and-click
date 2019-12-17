from selenium import webdriver
import pyautogui as mouse
import time



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
        mouse.moveTo(50, 50)
        
        time.sleep(scrollTime)
        print('This worked')

start = ExplorePage(5, 'https://ubuntu.com/')
start.openBrowser()