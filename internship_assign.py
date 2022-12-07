import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# I use brave browser so this is necessary if you also use brave uncomment the line below#
# options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://propertysearch.altusgroup.com/Property/Search/All/All/For-Sale-and-To-Let/All/All/All/All'
           '/recently-added-first/All')
driver.maximize_window()

more = driver.find_element(By.XPATH, '//*[@id="property-pagination-wrapper"]/button[1]')
time.sleep(10)

# the button doesnt load automatically so i used pyautogui to scroll down so the button loads on the webpage then i used selenium click feature #
for i in range(100):
    pyautogui.vscroll(-400)
for i in range(14):
    time.sleep(10)
    more.click()

# this gets links of all houses #
houses = []
for i in range(1, 171):
    houses.append(driver.find_element(By.XPATH, f'/html/body/main/div/div[5]/div/div[2]/div[{i}]/div/a ').
                  get_attribute("href"))

i = 1
# write the details of all houses #
with open(file="details.txt", mode="w") as file:
    for house in houses:
        driver.get(house)
        address = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div/div[2]/h2").text
        area = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div/div[2]/p[1]").text
        contact_name = driver.find_elements(By.CLASS_NAME, 'contact-name')
        contact_details = driver.find_elements(By.CLASS_NAME, 'agent-contact')
        a = 0
        dets = []
        cd = []
        file.writelines(f"{i}.{address}\n{area}")
        for names in contact_name:
            cd = contact_details[0 + a:2 + a]
            file.writelines("\n" + names.text)
            for d in cd:
                file.writelines("\n" + d.get_attribute("href"))
            a += 2
        file.writelines("\n\n")
        i += 1

driver.close()
