from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests

def getBrowser():
    chrome_options = webdriver.ChromeOptions()
    # proxy = "socks5://127.0.0.1:9050"
    # # chrome_options.add_argument('--proxy-server=%s' % proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = getBrowser()
browser.get('http://www.aicte-india.org/dashboard/pages/facultydetails.php?aicteid=1-2813663039&pid=1-482487061&year=2016-2017')

# soup = BeautifulSoup(browser.page_source, "lxml")


table_data = []
while(True):
    soup = BeautifulSoup(browser.page_source, "lxml")
    table = soup.find('table', {'class':'table table-striped table-bordered table-hover dataTable no-footer'})
    tbody = table.find('tbody')

    for tr in tbody.find_all('tr'):
        td = tr.find_all('td')
        row_data = {}
        i = 0
        for label in ['f_id', 'name', 'gender', 'designation', 'date_of_joining', 'area_of_specialisation', 'appointment_type']:
            row_data[label] = td[i].text
            i = i + 1
        table_data.append(row_data)


    if soup.find('li', {'class':'paginate_button next'}):
       browser.find_element_by_xpath('//*[@id="dataTables_next"]/a').click()
    else:
        break

print (table_data)
