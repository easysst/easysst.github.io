from selenium import webdriver
from config import getConfig
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.core.utils import read_version_from_cmd
from webdriver_manager.core.os_manager import PATTERN
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def loadDriver(browserLaunchOptions):    
    # Load driver service
    driver_version = read_version_from_cmd('/usr/bin/chromium --version', PATTERN[ChromeType.CHROMIUM])
    print("Loading driver, version: " + driver_version)
    driver_service = Service(ChromeDriverManager(driver_version=driver_version, chrome_type=ChromeType.CHROMIUM).install())

    # Load driver options
    print("Loading driver options...")
    driver_options = Options()
    for option in browserLaunchOptions:
        driver_options.add_argument(option)

    # Finally load driver with options
    return webdriver.Chrome(service=driver_service, options=driver_options)


if __name__ == "__main__":
    loadDriver(getConfig("main"))