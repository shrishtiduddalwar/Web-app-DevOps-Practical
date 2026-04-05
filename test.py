from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time


def main():
    # Update this path if your ChromeDriver binary is located elsewhere
    chromedriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

    # Build local file URL for index.html
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, "index.html")
    file_url = f"file:///{html_path.replace('\\', '/')}"

    chrome_options = Options()
    # Uncomment to run without opening a visible browser window
    # chrome_options.add_argument("--headless=new")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(file_url)
        time.sleep(1)

        name_input = driver.find_element(By.ID, "name")
        feedback_input = driver.find_element(By.ID, "feedback")
        submit_button = driver.find_element(By.TAG_NAME, "button")

        name_input.send_keys("Test User")
        feedback_input.send_keys("This is a Selenium test feedback.")
        submit_button.click()

        alert = Alert(driver)
        alert_text = alert.text
        print("Alert text:", alert_text)

        assert alert_text == "Feedback submitted successfully!", "Unexpected alert message"

        alert.accept()
        print("Test passed.")
    finally:
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    main()
