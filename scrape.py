import sys
import time
from selenium.webdriver.common.by import By

from utils.driver import load_driver
from utils.config import get_config, save_config

template = {}
driver = None

def setup():
    global template
    global driver
    
    # Load configs
    main_config = get_config("main")
    template = get_config("template")

    # Check if we skip driver installation
    skip_driver_installation = True
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            skip_driver_installation = False

    # Load Driver
    driver = load_driver(main_config['browserLaunchOptions'], skip_driver_installation)


def scrape_epic():
    eg = template['epicgames']
    targets = eg['targets']

    driver.get(eg['url'])
    time.sleep(1) # Wait until loaded!
    
    for target in targets:
        el = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div[1]/div[{targets[target]['row-level']}]/div[1]/span[2]")
        targets[target]['status'] = el.text == "Operational"


def scrape():
    scrape_epic()

    # Get save time
    template['last-updated'] = int(time.time())

    # Save to out file
    save_config("out", template)

if __name__ == "__main__":
    setup()
    scrape()