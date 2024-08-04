import time
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

from utils.driver import load_driver
from utils.config import get_config

# Example
def fn_scrape():
    # Get config
    config = get_config("main")

    # Load driver
    # driver = load_driver(config['browserLaunchOptions'], True) # Used only in local machine for easier testing
    driver = load_driver(config['browserLaunchOptions']) 

    # Let's go to epic games server statuses and wait until page loads
    #TODO: instead of waiting for time, let code only continue if page loaded for e.g.
    driver.get("https://status.epicgames.com/")
    time.sleep(1)

    # Let's grab fortnite's status using xpath
    fn_status_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[2]")
    
    # Print the results
    print("Fortnite server status: "+fn_status_element.text)

if __name__ == "__main__":
    fn_scrape()