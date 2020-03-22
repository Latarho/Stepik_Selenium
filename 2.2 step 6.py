from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_tag_name("input")
    input.send_keys(y)

    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()

    input_rb = browser.find_element_by_id("robotsRule")
    browser.execute_script("window.scrollBy(0, 100);")
    input_rb.click()
    assert True

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла