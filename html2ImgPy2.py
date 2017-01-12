# coding=utf-8
from selenium import webdriver
import os
import time
import sys

url = sys.argv[1]
execName = 'phantomjs';
print(os.name)

if os.name == 'nt':
    execName = execName + '.exe'

driver = webdriver.PhantomJS(executable_path='./phantomjs/' + os.name + '/bin/' + execName)
# 这里的executable_path填你phantomJS的路径

# 设置宽高
driver.set_window_size(1280, 720)

driver.get(url)

time.sleep(2)

driver.save_screenshot("shot.png")

driver.quit()
