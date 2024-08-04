from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.core.utils import read_version_from_cmd
from webdriver_manager.core.os_manager import PATTERN
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

EXECUTABLE_PATTERN = {
    ChromeType.GOOGLE: "google-chrome",
    ChromeType.CHROMIUM: "chromium"
}

def load_driver(browser_launch_options, skip_driver_installation = False, chrome_type = ChromeType.GOOGLE):    
    # Load driver options
    driver_options = Options()
    for option in browser_launch_options:
        driver_options.add_argument(option)

    if skip_driver_installation:
        print("Loading driver...")
        return webdriver.Chrome(options=driver_options)

    # Load driver service
    driver_version = read_version_from_cmd(f'/usr/bin/{EXECUTABLE_PATTERN[chrome_type]} --version', PATTERN[chrome_type])
    print("Loading driver service, version: " + driver_version)
    driver_service = Service(ChromeDriverManager(driver_version=driver_version, chrome_type=chrome_type).install())

    # Finally load driver with options
    print("Loading driver...")
    return webdriver.Chrome(service=driver_service, options=driver_options)