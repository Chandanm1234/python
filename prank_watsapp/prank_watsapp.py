import pyautogui as pg
import time
time.sleep(10)
txt=open('C://Users//Chandan.m//OneDrive//Desktop//python//basic_program//prank_watsapp//animals//animals.txt','r')
a = "nanda is a"

for i in txt:
    pg.write(a+ ' ' +i)
    pg.press('Enter')
    
