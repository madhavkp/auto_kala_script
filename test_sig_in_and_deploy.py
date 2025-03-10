from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    url = "https://kalaloka.com"  # Corrected URL

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    print(driver.title)  # Print page title to verify
    expected_title = driver.title  # Fixed variable name
    assert "KalaLoka" in expected_title, f"Expected 'Kalaloka' in title, but got '{expected_title}'"
    print("Page Is Loaded Successfully")
    driver.quit()

