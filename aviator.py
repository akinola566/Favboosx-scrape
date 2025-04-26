# aviator.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import creds
import vars

class Aviator:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run without opening browser window
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://22bet-b.com")
        time.sleep(3)

        # Click "Login"
        login_button = self.driver.find_element(By.LINK_TEXT, "LOG IN")
        login_button.click()
        time.sleep(2)

        # Fill username and password
        self.driver.find_element(By.NAME, "userLogin").send_keys(creds.username)
        self.driver.find_element(By.NAME, "userPassword").send_keys(creds.password)
        time.sleep(1)

        # Submit login
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'LOG IN')]").click()
        time.sleep(5)

    def go_to_aviator(self):
        self.driver.get(vars.aviator_url)
        time.sleep(5)

    def get_multipliers(self):
        multipliers = []

        for i in range(1, 31):
            try:
                xpath = vars.last_game_result_xpath.replace("1", str(i))
                element = self.driver.find_element(By.XPATH, xpath)
                multiplier_text = element.text.strip().replace("x", "")
                multipliers.append(multiplier_text)
            except Exception:
                continue

        return multipliers

    def close(self):
        self.driver.quit()
