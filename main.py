from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
import time
import os
from selenium.webdriver.common.alert import Alert 

def test_print_data_table(driver):
     try:
          table = driver.find_element(By.XPATH,'/html/body/table')
          tbody = table.find_element(By.TAG_NAME,'tbody')
          trs = tbody.find_elements(By.TAG_NAME,'tr')
          for tr in trs:
               print(tr.text)
               tds = tr.find_elements(By.TAG_NAME,'tr')
               for td in tds:
                    print(td.text)
     except Exception as e:
          print(f'Can not read the table with error {e}')

def test_fill_details_on_myself(driver):
     try:
          first_name = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[1]')
          first_name.clear()
          first_name.send_keys('Daniel')

          last_name = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[2]')
          last_name.clear()
          last_name.send_keys('Razal')

          city = Select(driver.find_element(By.XPATH, '/html/body/form/fieldset/select[1]'))
          city.select_by_index(1)

          email = driver.find_element(By.XPATH, '//*[@id="email"]')
          email.clear()
          email.send_keys('mr.danielrazal@gmail.com')

          prefix_phone = Select(driver.find_element(By.XPATH, '/html/body/form/fieldset/select[2]'))
          prefix_phone.select_by_index(0)


          phone_number = driver.find_element(By.XPATH, '//*[@id="phone"]')
          phone_number.clear()
          phone_number.send_keys('2242268')

          sex = driver.find_element(By.ID, 'm')
          sex.click()

          checkBoxes_xpath = [
               '//*[@id="m"]',
               '//*[@id="b"]'
          ]

          for xpath in checkBoxes_xpath:
               checkboxs = driver.find_elements(By.XPATH, xpath)
               for checkbox in checkboxs:
                    checkbox.click()

          time.sleep(4)

          clear_button = driver.find_element(By.XPATH,'//*[@id="CB"]')
          clear_button.click()
     except Exception as e:
          print(f'Can not fill the details with error {e}')

def test_alert(driver):
     try:
          set_text = driver.find_element(By.XPATH,'/html/body/fieldset[1]/button[1]')
          set_text.click()

          alert = Alert(driver)
          alert.send_keys('QA Automation Project')
          time.sleep(5)
          alert.accept()
     except Exception as e:
          print(f'Can not read the text {e}')

def test_change_title(driver):
     try:
          start_loading = driver.find_element(By.XPATH,'/html/body/fieldset[1]/button[2]')
          start_loading.click()
          time.sleep(5)
          
          text_finish = driver.find_element(By.ID,'startLoad')
          compare_finish = 'Finish'

          assert compare_finish == text_finish.text

     except AssertionError as e:
          print('The values are not equals')

def test_check_titles(driver):
     try:
          next_page = driver.find_element(By.LINK_TEXT,'Next Page')
          next_page.click()

          change_title = driver.find_element(By.XPATH,'/html/body/button')
          change_title.click()
          
          title_next_page_element = driver.find_element(By.TAG_NAME, 'title')

          # print (driver.title)

          title_next_page = title_next_page_element.get_attribute('textContent')
          print(title_next_page)
          title_name = 'Finish'

          assert title_next_page == title_name

          time.sleep(10)
          driver.back()


          windy = driver.find_element(By.LINK_TEXT,'Windy')
          windy.click()

          title_windy_element = driver.find_element(By.TAG_NAME, 'title')

          title_windy = title_windy_element.get_attribute('textContent')
          print(title_windy)

          windy_title_name = 'Windy: Wind map & weather forecast'          

          assert title_windy == windy_title_name

          time.sleep(10)
          driver.back()


          tera_santa = driver.find_element(By.LINK_TEXT,'Tera Santa')
          tera_santa.click()

          title_tera_santa_element = driver.find_element(By.TAG_NAME, 'title')

          title_tera_santa = title_tera_santa_element.get_attribute('textContent')
          print(title_tera_santa)

          tera_santa_title_name = 'TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS'          

          assert title_tera_santa == tera_santa_title_name
          time.sleep(10)
          driver.back()

          java_book = driver.find_element(By.LINK_TEXT,'Java Book')
          java_book.click()

          title_java_book_element = driver.find_element(By.TAG_NAME, 'title')

          title_java_book = title_java_book_element.get_attribute('textContent')
          print(title_java_book)

          java_book_title_name = 'ivbs-white-logo.png (108×63)'          

          assert title_java_book == java_book_title_name
          time.sleep(10)
          driver.back()

          youtube = driver.find_element(By.LINK_TEXT,'YouTube')
          youtube.click()

          title_youtube_element = driver.find_element(By.TAG_NAME, 'title')

          title_youtube = title_youtube_element.get_attribute('textContent')
          print(title_youtube)

          youtube_title_name = 'YouTube'          

          assert title_youtube == youtube_title_name
          time.sleep(10)
          driver.back()
          
     except AssertionError as e:
          print(f'blabla')

if __name__ == '__main__':
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('http://127.0.0.1:5500/HTML_Project.html')
    driver.maximize_window()
    time.sleep(5)
    test_print_data_table(driver)
    time.sleep(5)

    test_fill_details_on_myself(driver)
    time.sleep(5)
    test_alert(driver)
    time.sleep(5)
    test_change_title(driver)
    time.sleep(5)
    test_check_titles(driver)

    time.sleep(5)
    driver.close()