from selenium import webdriver
import time
import unittest

class Test_Reg_Form(unittest.TestCase):

    def test_Reg_Form_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("Serg")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("Pomytkin")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("latarho@gmail.com")
        input4 = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]')
        input4.send_keys("89505471147")
        input5 = browser.find_element_by_css_selector('input[placeholder="Input your address:"]')
        input5.send_keys("MOTHER RUSSIA")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка")

    def test_Reg_Form_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("Serg")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("Pomytkin")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("latarho@gmail.com")
        input4 = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]')
        input4.send_keys("89505471147")
        input5 = browser.find_element_by_css_selector('input[placeholder="Input your address:"]')
        input5.send_keys("MOTHER RUSSIA")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка")

if __name__ == "__main__":
    unittest.main()



