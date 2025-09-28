from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open local file (file:// protocol)
file_path = f"file://{os.path.abspath('form.html')}"
driver.get(file_path)

try:
    driver.find_element(By.NAME, "firstname").send_keys("Aditi")
    driver.find_element(By.NAME, "lastname").send_keys("Raut")
    driver.find_element(By.ID, "sex-1").click()
    driver.find_element(By.ID, "exp-3").click()
    driver.find_element(By.ID, "submit").click()

    print("Form submitted successfully!")
except Exception as e:
    print("Test failed:", e)
finally:
    time.sleep(2)
    driver.quit()

