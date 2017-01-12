#! python3
# coding=utf-8
# 中文为方框的话需要安装字体
# 在centos中执行：yum install bitmap-fonts bitmap-fonts-cjk
# 在ubuntu中执行：sudo apt-get install
# 如果要截取 html 文件需要使用 file:///D:/WebstormProjects/ZuiBlog/index.html 类似这样的方式
# platform Windows-10-10.0.15002-SP0  Linux-3.10.104-1.el6.elrepo.i686-i686-with-centos-6.8-Final  Darwin

from selenium import webdriver
import os
import time
import sys

url = sys.argv[1]
execName = 'phantomjs'

if os.name == 'nt':
    execName = execName + '.exe'

driver = webdriver.PhantomJS(executable_path='./phantomjs/' + os.name + '/bin/' + execName)
# 设置宽高
driver.set_window_size(1280, 720)
# 这里的executable_path填你phantomJS的路径

driver.get(url)

time.sleep(2)

driver.save_screenshot("shot.png")

driver.quit()
