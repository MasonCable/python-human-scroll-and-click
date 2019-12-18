from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as mouse
import time


def moveMouse(parameter):
    ammt = parameter

    while ammt > 0:
        mouse.moveRel(10)
        mouse.moveRel(None, 10)
        print('moving mouse')
        ammt = ammt - 1    

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

    def fillForm(self):
        browser = self.bot

        inputForm = browser.find_element_by_class_name('gLFyf')
        inputForm.send_keys('https://textbroker.com/')
        time.sleep(2)
        inputForm.send_keys(Keys.RETURN)
        time.sleep(3)

    def clickSuppliedLink(self):
        browser = self.bot
        moveMouse(10)
        firstLink = browser.find_element_by_class_name('LC20lb')
        firstLink.click()
    
    def scrollPageAndClick(self):
        browser = self.bot
        # clickSomewhere = browser.find_element_by_class_name('p-navigation__link-anchor')
        signUpButton = browser.find_element_by_class_name('btn-register')
        moveMouse(3)
        # clickSomewhere.click()
        moveMouse(15)
        signUpButton.click()


        

start = ExplorePage(5, 'https://google.com/')
start.openBrowser()
start.fillForm()
start.clickSuppliedLink()
# This is where we will want to scroll around the page in a "human link" manner
start.scrollPageAndClick()