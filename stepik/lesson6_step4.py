from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "div .trollface").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text

    res = str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(res)

    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()