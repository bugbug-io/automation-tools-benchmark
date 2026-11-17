import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()


def test_add_todo(driver):
    driver.get("https://demo.playwright.dev/todomvc/")
    wait = WebDriverWait(driver, 10)
    box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-todo")))
    box.send_keys("Write the regression suite", Keys.ENTER)
    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="todo-title"]')))
    assert title.text == "Write the regression suite"
    count = driver.find_element(By.CSS_SELECTOR, '[data-testid="todo-count"]')
    assert count.text == "1 item left"
