import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
from PIL import Image


class DinosaurGame():
    def __init__(self):
        self.service = Service("C:\Development\chromedriver.exe")
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.keys = Keys()
        self.gui = pyautogui

    def bounce(self):
        self.gui.press('up')

    def start(self):
        self.driver.get("https://elgoog.im/dinosaur-game/")
        time.sleep(5)
        self.gui.press('up')

    def checker(self):
        if self.gui.pixelMatchesColor(263, 663, (83, 83, 83), tolerance=100):
            self.bounce()
        elif self.gui.pixelMatchesColor(223, 696, (83, 83, 83), tolerance=100):
            self.bounce()
        elif self.gui.pixelMatchesColor(235, 680, (83, 83, 83), tolerance=100):
            self.bounce()
        elif self.gui.pixelMatchesColor(235, 699, (83, 83, 83), tolerance=100):
            self.bounce()
        elif self.gui.pixelMatchesColor(243, 650, (83, 83, 83), tolerance=100):
            self.bounce()
        elif self.gui.pixelMatchesColor(235, 662, (83, 83, 83), tolerance=100):
            self.bounce()



dino_game = DinosaurGame()
dino_game.start()
game_on = True
while game_on:
    dino_game.checker()
    if pyautogui.pixelMatchesColor(1068, 463, (83, 83, 83), tolerance=100):
        game_on = False
