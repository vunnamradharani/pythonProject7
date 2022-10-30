from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


first_name = 'radha'
last_name = 'sirigiri'
nationality = "Indian"
married = "Married"


class SimpleTest(unittest.TestCase):

    def test_tc_login_01(self):
        driver = webdriver.Firefox()
        url = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "admin123"
        driver.get(url)
        time.sleep(3)
        el_username_name = "username"
        el_password_name = "password"
        el_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
        element_username = driver.find_element(by=By.NAME, value=el_username_name)
        element_password = driver.find_element(by=By.NAME, value=el_password_name)
        submit_button = driver.find_element(by=By.CLASS_NAME, value=el_submit_button_class)
        element_username.send_keys(user)
        element_password.send_keys(password)
        submit_button.click()
        time.sleep(3)
        try:
            el_p_user_name = driver.find_element(by=By.CLASS_NAME, value="oxd-userdropdown-name")
            self.assertIsNotNone(el_p_user_name, "Expected p tag with class oxd-userdropdown-name after successful login")
        except selenium.common.exceptions.NoSuchElementException:
            self.assertIsNotNone(el_p_user_name, "Expected p tag with class oxd-userdropdown-name after successful login")
        driver.close()

    def test_tc_login_02(self):
        driver = webdriver.Firefox()
        url = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "invalid password"
        driver.get(url)
        time.sleep(3)
        el_username_name = "username"
        el_password_name = "password"
        el_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
        element_username = driver.find_element(by=By.NAME, value=el_username_name)
        element_password = driver.find_element(by=By.NAME, value=el_password_name)
        submit_button = driver.find_element(by=By.CLASS_NAME, value=el_submit_button_class)
        element_username.send_keys(user)
        element_password.send_keys(password)
        submit_button.click()
        time.sleep(3)
        try:
            el_p_error_message = driver.find_element(by=By.CLASS_NAME, value="oxd-text.oxd-text--p.oxd-alert-content-text")
            self.assertIsNotNone(el_p_error_message, "Expected p tag with class oxd-text oxd-text--p oxd-alert-content-text for invalid login")
        except selenium.common.exceptions.NoSuchElementException:
            self.assertIsNotNone(el_p_error_message, "Expected p tag with class oxd-text oxd-text--p oxd-alert-content-text for invalid login")
        driver.close()

    def test_tc_pim_01(self):
       # Login with Admin/
        driver = webdriver.Firefox()
        url = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "admin123"
        driver.get(url)
        time.sleep(3)
        el_username_name = "username"
        el_password_name = "password"
        el_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
        element_username = driver.find_element(by=By.NAME, value=el_username_name)
        element_password = driver.find_element(by=By.NAME, value=el_password_name)
        submit_button = driver.find_element(by=By.CLASS_NAME, value=el_submit_button_class)
        element_username.send_keys(user)
        element_password.send_keys(password)
        submit_button.click()
        time.sleep(3)
        #Login end
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        time.sleep(2)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        time.sleep(2)
        element_first_name = driver.find_element(by=By.NAME, value='firstName')
        element_last_name = driver.find_element(by=By.NAME, value='lastName')
        element_first_name.send_keys(first_name)
        time.sleep(1)
        element_last_name.send_keys(last_name)
        time.sleep(1)
        el_form_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space'
        form_submit_button = driver.find_element(by=By.CLASS_NAME, value=el_form_submit_button_class)
        form_submit_button.click()
        time.sleep(1)
        el_select_icons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'oxd-select-text-input')))
        time.sleep(2)
        el_icons = driver.find_elements(by=By.CLASS_NAME, value='oxd-icon.bi-caret-down-fill.oxd-select-text--arrow')
        el_nationality_icon = el_icons[0]
        el_nationality_icon.click()
        time.sleep(2)

        elements = driver.find_elements(By.TAG_NAME, 'div')
        for el in elements:
            if el.text == nationality:
                el.click()
                break
        time.sleep(1)
        el_martialstatus_icon = el_icons[1]
        el_martialstatus_icon.click()
        time.sleep(4)
        elements_new = driver.find_elements(By.TAG_NAME, 'div')
        for el_new in elements_new:
            if el_new.text == married:
                el_new.click()
                break
        time.sleep(1)
        form_save_button = driver.find_elements(By.CLASS_NAME, 'oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')
        time.sleep(2)
        form_save_button[0].click()
        time.sleep(5)
        driver.close()

    def test_tc_pim_02(self):
        #Login with Admin/
        driver = webdriver.Firefox()
        url = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "admin123"
        driver.get(url)
        time.sleep(3)
        el_username_name = "username"
        el_password_name = "password"
        el_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
        element_username = driver.find_element(by=By.NAME, value=el_username_name)
        element_password = driver.find_element(by=By.NAME, value=el_password_name)
        submit_button = driver.find_element(by=By.CLASS_NAME, value=el_submit_button_class)
        element_username.send_keys(user)
        element_password.send_keys(password)
        submit_button.click()
        time.sleep(3)
        #Login end
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        time.sleep(2)
        records = driver.find_elements(by=By.CLASS_NAME, value='oxd-icon-button.oxd-table-cell-action-space')
        records[1].click()

        time.sleep(1)
        el_select_icons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'oxd-select-text-input')))
        time.sleep(2)
        el_icons = driver.find_elements(by=By.CLASS_NAME, value='oxd-icon.bi-caret-down-fill.oxd-select-text--arrow')
        el_nationality_icon = el_icons[0]
        el_nationality_icon.click()
        time.sleep(2)

        elements = driver.find_elements(By.TAG_NAME, 'div')
        for el in elements:
            if el.text == nationality:
                el.click()
                break
        time.sleep(1)
        el_martialstatus_icon = el_icons[1]
        el_martialstatus_icon.click()
        time.sleep(4)
        elements_new = driver.find_elements(By.TAG_NAME, 'div')
        for el_new in elements_new:
            if el_new.text == married:
                el_new.click()
                break
        time.sleep(1)
        form_save_button = driver.find_elements(By.CLASS_NAME, 'oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')
        time.sleep(2)
        form_save_button[0].click()
        time.sleep(5)
        driver.close()

    def test_tc_pim_03(self):
        #Login with Admin/
        driver = webdriver.Firefox()
        url = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "admin123"
        driver.get(url)
        time.sleep(3)
        el_username_name = "username"
        el_password_name = "password"
        el_submit_button_class = 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
        element_username = driver.find_element(by=By.NAME, value=el_username_name)
        element_password = driver.find_element(by=By.NAME, value=el_password_name)
        submit_button = driver.find_element(by=By.CLASS_NAME, value=el_submit_button_class)
        element_username.send_keys(user)
        element_password.send_keys(password)
        submit_button.click()
        time.sleep(3)
        #Login end
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        time.sleep(2)
        records = driver.find_elements(by=By.CLASS_NAME, value='oxd-icon-button.oxd-table-cell-action-space')
        records[0].click()
        time.sleep(3)
        button_delete = driver.find_element(By.CLASS_NAME, 'oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin')
        button_delete.click()
        time.sleep(5)
        driver.close()



if __name__ == '__main__':
    unittest.main()
