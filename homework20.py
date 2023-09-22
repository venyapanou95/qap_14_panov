# Задание 1:
# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# open site
def test_1(driver):
    driver.get("http://thedemosite.co.uk/login.php")

username_locator = '[name="username"]'
password_locator = '[type="password"]'
login_locator = '//*[@id="saveform"]/div/center/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/p/input'
driver.find_element(By.CSS_SELECTOR, username_locator).send_keys('Ben')

driver.find_element(By.CSS_SELECTOR, password_locator).send_keys('123qwe')

driver.find_element(By.XPATH, login_locator).click()

# 5. Проверить, что Successful Login отображаются не понял как сделать

