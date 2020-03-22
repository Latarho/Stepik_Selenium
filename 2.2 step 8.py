from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Serg")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Pomytkin")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("latarho@gmail.com")

    current_dir = os.path.abspath(os.path.dirname("C:/Users/latar/PycharmProjects/Stepik Selenium"))
    file_path = os.path.join(current_dir, "Serg.txt")
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла