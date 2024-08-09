#Web Simulator tests run only on safari.
# main ingredients - platformName(ios always), platformVersion, deviceName

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace with your LambdaTest username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace with your LambdaTest access key

caps = {
		"lt:options": {
			"w3c": True,
			"platformName": "ios",
			"deviceName": "iPhone 14",
			"isRealMobile": False,
            "platformVersion": "17.0",
			"build": "buildName",
			"visual": True,
			"network": True,
			"video": True,
		},
}

def setup_driver_prod():
    try:
        username = "add here"
        access_key = "add here"
        driver = webdriver.Remote(
                    command_executor=f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub", desired_capabilities=caps )
        print("Driver created successfully")
    except Exception as e:
        print("Error creating driver")
        return None
    return driver

def setup_driver():
    try:
        username = "add here"
        access_key = "add here"
        driver = webdriver.Remote(
                    command_executor=f"http://{username}:{access_key}@hub-rishav001-dev.lambdatestinternal.com/wd/hub", desired_capabilities=caps)
    except Exception as e:
        print("Error creating driver")
        return None
    return driver


def test_demo_site(driver):
    print("Loading URL1")
    driver.implicitly_wait(10)
    print("Loading URL2")
    driver.set_page_load_timeout(30)
    # driver.set_window_size(1920, 1080)

    # Load the URL
    print("Loading URL")
    driver.get(
        "https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html"
    )

    # Click on the first list item
    driver.find_element(By.NAME, "li1").click()

    # Click on the second list item
    driver.find_element(By.NAME, "li2").click()
    print("Clicked on the second element")

    # Add a new todo item
    driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
    driver.find_element(By.ID, "addbutton").click()
    print("Added LambdaTest checkbox")

    # Check if the heading is displayed and print it
    search = driver.find_element(By.CSS_SELECTOR, ".container h2")
    if search.is_displayed():
        print(search.text)
        search.click()

    # Validate test status
    heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
    if heading.is_displayed():
        heading.click()
        driver.execute_script("lambda-status=passed")
        print("Tests are run successfully!")
    else:
        driver.execute_script("lambda-status=failed")

def teardown_driver(driver):
    driver.quit()

if __name__ == "__main__":
    # driver = setup_driver()
    driver = setup_driver_prod()
    try:
        test_demo_site(driver)
    finally:
        teardown_driver(driver)
