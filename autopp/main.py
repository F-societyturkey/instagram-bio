from genericpath import samestat
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import kulanicibilgisi as kb
from time import *
from datetime import *
import time
import datetime
from os import name, system
from time import sleep
import pyautogui

def zaman():
    driver = webdriver.Firefox()
    a = driver.get('https://www.instagram.com/')
    input("devam etmek için enter")
    print("giriliyor..")

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys(kb.Username)
    password.send_keys(kb.Password)
    time.sleep(3)
    login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
    login.click()
    time.sleep(13)

    profill = driver.find_element_by_xpath(
    "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img")
    profill.click()
    time.sleep(8)

    profil = driver.find_element_by_xpath(
    "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
    profil.click()
    time.sleep(7)

    bio = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/a')
    bio.click()
    time.sleep(4)
    
    
    while True:
        pepbio = driver.find_element_by_xpath('//*[@id="pepBio"]')
        pepbio.click()
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('backspace')
        pyautogui.keyUp('backspace')
        time.sleep(2)
        saat = strftime('%H:%M')
        pepbio.send_keys(saat)
        time.sleep(1)
        gonder = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button")
        gonder.click()
        time.sleep(58)

zaman()


"""
ppklik = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/div/div/div/button/img")
ppklik.click()
time.sleep(5)
"""
# ada5V
