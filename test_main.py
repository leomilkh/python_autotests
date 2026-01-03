import requests
import pytest

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"

def test_positive_login(browser):
    """
    TRP-0. Positive test case: login to the website and verify the presence of an item
    """
    browser.get(URL)

    username_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Username"]')
    username_input.click()
    username_input.send_keys('standard_user')

    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Password"]')
    password_input.click()
    password_input.send_keys('secret_sauce')

    button = browser.find_element(by=By.CSS_SELECTOR, value='[class="submit-button btn_action"]')
    button.click()

    good_looking_for = browser.find_element(by=By.XPATH, value="//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
    assert good_looking_for is not None

CASES = [
    ('1', 'standard_user', 'secret_sauce1', 'Epic sadface: Username and password do not match any user in this service'),
    ('2', ' ', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
    ('3', 'standard_user', ' ', 'Epic sadface: Username and password do not match any user in this service'),
]


@pytest.mark.parametrize('case_number, username, password, error_message', CASES)
def test_negative_wrong_password(browser, case_number, username, password, error_message):
    """
    TRP-1. Negtive test case: login to the website with invalid password and verify error message
    """
    logger.info(f'CASE : {case_number} | username: {username} | password: {password} | error_message: {error_message} ')
    browser.get(URL)

    username_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Username"]')
    username_input.click()
    username_input.send_keys(username)

    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Password"]')
    password_input.click()
    password_input.send_keys(password)

    button = browser.find_element(by=By.CSS_SELECTOR, value='[class="submit-button btn_action"]')
    button.click()

    error_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f'//h3[@data-test="error" and text()="{error_message}"]'))
    )
    assert error_element is not None, f"Expected error message not displayed: {error_message}"

@pytest.mark.parametrize('case_number, username, password, error_message', CASES)
def test_negative_no_username(browser, case_number, username, password, error_message):
    """
    TRP-2. Negtive test case: login to the website with no username and verify error message
    """
    logger.info(f'CASE : {case_number} | username: {username} | password: {password} | error_message: {error_message} ')
    browser.get(URL)

    username_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Username"]')
    username_input.click()
    username_input.send_keys(username)

    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Password"]')
    password_input.click()
    password_input.send_keys(password)

    button = browser.find_element(by=By.CSS_SELECTOR, value='[class="submit-button btn_action"]')
    button.click()

    error_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f'//h3[@data-test="error" and text()="{error_message}"]'))
    )
    assert error_element is not None, f"Expected error message not displayed: {error_message}"

@pytest.mark.parametrize('case_number, username, password, error_message', CASES)
def test_negative_no_password(browser, case_number, username, password, error_message):
    """
    TRP-3. Negtive test case: login to the website with no password and verify error message
    """
    logger.info(f'CASE : {case_number} | username: {username} | password: {password} | error_message: {error_message} ')
    browser.get(URL)

    username_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Username"]')
    username_input.click()
    username_input.send_keys(username)

    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[placeholder="Password"]')
    password_input.click()
    password_input.send_keys(password)

    button = browser.find_element(by=By.CSS_SELECTOR, value='[class="submit-button btn_action"]')
    button.click()

    error_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f'//h3[@data-test="error" and text()="{error_message}"]'))
    )
    assert error_element is not None, f"Expected error message not displayed: {error_message}"