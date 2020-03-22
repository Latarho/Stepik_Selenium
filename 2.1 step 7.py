from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x1_element = x_element.get_attribute('valuex')
    x = x1_element
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()

    input_rb = browser.find_element_by_id("robotsRule")
    input_rb.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
