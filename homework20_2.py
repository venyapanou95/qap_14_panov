
# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
# 2. Заполнить все поля
# 3. Нажать кнопку Submit
# 4. Проверить, что отображается правильно имя и фамилия
# Подсказка xpath ".//tr//table//font[3]”
# 5.Проверить, что отображается правильно username
# Подсказка xpath ".//tr//table//font[5]”g
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_2(driver):
    driver.get('http://demo.guru99.com/test/newtours/register.php')

    firstname_locator = '[name="firstName"]'
    lastname_locator = '[name="lastName"]'
    phone_locator = '[name="phone"]'
    email_locator = '[name="email"]'
    address_locator = '[name="address1"]'
    city_locator = '[name="city"]'
    state_province_locator = '[name="state"]'
    postal_code_locator = '[name="postalCode"]'
    country_select_locator = '[name="country"]'
    user_name_locator = '[name="email"]'
    password_locator = '[name="password"]'
    confirm_password_locator = '[name="confirmPassword"]'

    driver.find_element(By.CSS_SELECTOR, firstname_locator).send_keys('venya')
    driver.find_element(By.CSS_SELECTOR, lastname_locator).send_keys('panov')
    driver.find_element(By.CSS_SELECTOR, phone_locator).send_keys('375447129223')
    driver.find_element(By.CSS_SELECTOR, email_locator).send_keys('qwerttt@mail.ru')
    driver.find_element(By.CSS_SELECTOR, address_locator).send_keys('lidskaya 37')  
    driver.find_element(By.CSS_SELECTOR, city_locator).send_keys('grodno')
    driver.find_element(By.CSS_SELECTOR, state_province_locator).send_keys('belarus grodnenskiy reg')
    driver.find_element(By.CSS_SELECTOR, postal_code_locato).send_keys('230025')
   
    country_select = select(driver.find_element(By.NAME, 'country'))
    country_select.select_by_value('BELARUS')

    driver.find_element(By.CSS_SELECTOR, user_name_locato).send_keys('venya')
    driver.find_element(By.CSS_SELECTOR, password_locator).send_keys('1234asa')
    driver.find_element(By.CSS_SELECTOR, confirm_password_locator).send_keys('1234asa')

    send_locator = '[name="submit"]'
    driver.find_element(By.CSS_SELECTOR, send_locator).click()

