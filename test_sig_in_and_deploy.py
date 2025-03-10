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
    assert "Kalaloka" in driver.title  # Example assertion to check if title contains expected text

    driver.quit()

    
