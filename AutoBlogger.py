#! python3
# AutoBlogger.py is a smart program that is going to be my claim to fame with auto uploading of nature shots
# Notes to run this program you need to install BeautifulSoup, Twill, lxml, cssselect, requests

import sys, urllib, os, signal, requests, re, time
from itertools import izip
from lxml import html
from pprint import pprint
from twill.commands import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    account = 0
    d = {}
    start=time.clock()
    driver = webdriver.Chrome() # Optional argument, if not specified will search path.

    driver.get('https://www.reddit.com/r/EarthPorn/top/?sort=top&t=day')

    newpath = r'BloggerFolder'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    path = os.getcwd() + '/' + newpath
    os.chdir(path)

    for dataRank in range(1,10):
        for i in driver.find_elements_by_xpath("//div[@data-rank="+str(dataRank)+"]"):
            src = i.get_attribute("data-url")
            print src
            resource = urllib.urlopen(src)
            filename = "file" + str(dataRank) + ".jpg"
            output = open(filename,"wb")
            output.write(resource.read())
            output.close()
        print "dataRank: " + str(dataRank)

    time.sleep(3)

    driver.get('https://www.tumblr.com/login')

    tumblrUser = driver.find_element_by_id("signup_determine_email").send_keys("USERNAME")
    driver.find_element_by_id("signup_forms_submit").click()
    time.sleep(3)
    driver.find_element_by_id("login-signin").click()
    time.sleep(3)
    password = driver.find_element_by_id('login-passwd')
    time.sleep(3)
    password.send_keys('PASSWORD')
    driver.find_element_by_id("login-signin").click()
    time.sleep(5)

    driver.find_element_by_id("new_post_label_photo").click()
    time.sleep(5)


    for imageCounter in range(1,10):
        driver.find_element_by_name("photo").send_keys(os.getcwd()+"/file"+str(imageCounter)+".jpg")
        time.sleep(4)

    time.sleep(10) #Long Delay needed
    driver.find_element_by_class_name('button-area').click()

    print "Now that all files are uploaded let's clear the files!"

    #for dataRank in range(1,10):
    #    os.remove("file" + str(dataRank) + ".jpg")

    #os.kill(driver, signal.SIGTERM)

    end=time.clock()
    maintime=end-start
    print ("Auto Blogger timing: "+str(maintime)) + " seconds."
    time.sleep(100) # Let the user actually see something!
    driver.quit()

main()
