from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as mouse
import time


def moveMouse():
    parameter = 5
    while parameter > 0:
        mouse.moveRel(10)
        mouse.moveRel(None, 10)
        print('hello')
        parameter = parameter - 1    

class ExplorePage:
    def __init__(self, scrollTime, link):
        self.scrollTime = scrollTime
        self.link = link
        self.bot = webdriver.Firefox()


    def openBrowser(self):
        link = self.link
        scrollTime = self.scrollTime
        browser = self.bot

        browser.get(link)
        time.sleep(scrollTime)
        # mouse.moveRel(20)
        # mouse.moveRel(30)
        
        #This function works, jsut removing it for rn 
        # moveMouse()
        # time.sleep(scrollTime)
        # print('This worked')

    def fillForm(self):
        browser = self.bot

        inputForm = browser.find_element_by_class_name('gLFyf')
        inputForm.send_keys('https://ubuntu.com/')
        time.sleep(2)
        inputForm.send_keys(Keys.RETURN)
        time.sleep(3)

    def clickSuppliedLink(self):
        browser = self.bot

        firstLink = browser.find_element_by_class_name('LC20lb')
        firstLink.click()
      


        

start = ExplorePage(5, 'https://google.com/')
start.openBrowser()
start.fillForm()
start.clickSuppliedLink()