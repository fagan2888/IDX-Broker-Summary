# # 1. Import all library

from requests_html import HTMLSession
import datetime
import time
import xlwt 
from xlwt import Workbook 
from datetime import datetime
from datetime import datetime
datestring = datetime.strftime(datetime.now(), '%Y;%m;%d')
import xlwings as xw
from openpyxl import Workbook, load_workbook
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import autoit
# import xlsxwriter
# from openpyxl.formula.translate import Translator
# from dateutil.parser import parse
# import pandas as pd
# from selenium.webdriver.common.action_chains import ActionChains
# import autopy

DRIVER = 'chromedriver'
options = webdriver.ChromeOptions()
if os.name == "nt":

    options.add_argument("--start-maximized")
else:
    
    options.add_argument("--kiosk")


driver = webdriver.Chrome(DRIVER, options = options)
driver.get('https://www.idx.co.id/data-pasar/ringkasan-perdagangan/ringkasan-broker/')
time.sleep(10)
idx = 20
for x in range(1000):
    x = x+1
    print(x)
    #========================================================================================================================

    #START-UNTUK MEMASUKAN TANGGAL
    # y = "'18/09/2019'"
    
    f= open("tanggal.txt","r")
    bacaline = f.read().split()
    tanggal = "document.getElementById('dateFilter').value="+"'"+bacaline[idx]+"'"
    print(tanggal)
    time.sleep(1)
    driver.execute_script(tanggal)
    
    print('date selected')

    time.sleep(5)
    print("sleep")


    #END-UNTUK MEMASUKAN TANGGAL


    #========================================================================================================================


    #START - UNTUK KLIK TOMBOL SEARCH

    driver.find_element_by_css_selector("button[onclick='getBrokerSummary()']").click()

    print('button search has been clicked')
    time.sleep(1)
    #END - UNTUK KLIK TOMBOL SEARCH

    #========================================================================================================================


    #START - UNTUK KLIK TOMBOL UNDUH

    # testing = driver.find_element_by_css_selector("td[class='dataTables_empty']").text()
    try:
        content = driver.find_element_by_class_name('dataTables_empty').text
        bolehan = 1
    except:
        bolehan = 3
        content = 0
        pass
    
    # print(content)

    if bolehan == 3:
        driver.find_element_by_css_selector("A[onclick='downloadSummary()']").click()

    print('button UNDUH has been clicked')


    #END - UNTUK KLIK TOMBOL UNDUH

    time.sleep(5)

    # driver.close()

    idx = idx + 1
    bolehan = 0

    #acuan
    # acuan --------------------> # driver.execute_script("document.getElementById('dateFilter').value = '18/09/2019'")