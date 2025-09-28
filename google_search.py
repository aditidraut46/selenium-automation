# google_search.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

print("Page title:", driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys("Python Selenium tutorial")
search.send_keys(Keys.RETURN)

time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR, "h3")

for i, r in enumerate(results[:5]):
    print(f"{i+1}. {r.text}")

driver.quit()

