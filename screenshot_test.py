from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.google.com")
    # Force a failure
    assert "Bing" in driver.title
    print("Test passed ✅")
except Exception as e:
    print("Test failed:", e)
    screenshot_path = os.path.expanduser("~/failure.png")
    if driver.save_screenshot(screenshot_path):
        print(f"Screenshot saved at: {screenshot_path}")
    else:
        print("Screenshot could not be saved")
finally:
    driver.quit()

