import pyautogui as pg
import time
time.sleep(10)
txt=open('C://Users//Chandan.m//OneDrive//Desktop//python//basic_program//prank_watsapp//i love u.bib','r')
a = "daddy"

for i in txt:
    pg.write(i+ ' ' +a)
    pg.press('Enter')