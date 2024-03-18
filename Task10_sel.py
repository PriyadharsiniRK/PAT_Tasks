from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_followers_following_count(username):
    # Initialize Chrome WebDriver (you need to have chromedriver installed and its location in PATH)
    driver = webdriver.Chrome()

    # Navigate to the Instagram profile
    driver.get(f"https://www.instagram.com/{username}/")

    try:
        # Wait for the followers count element to be loaded
        followers_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'followers')]/span"))
        )
        sleep(10)
        # Extract the text of the followers count element
        followers_count_text = followers_count_element.text

        # Wait for the followers count element to be loaded
        following_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'following')]/span"))
        )
        sleep(10)
        # Extract the text of the followers count element
        following_count_text = following_count_element.text

        return followers_count_text,following_count_text

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the WebDriver session
        driver.quit()




# Example usage
username = "guviofficial"
#calling method get_followers_following_count and assigned to followers_following_count variable
followers_following_count = get_followers_following_count(username)
#printing followers and following count
print(f"The followers and following count of {username} is: {followers_following_count}")
