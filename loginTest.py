from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginAutomation:
    """
   This class is used to login into the https://www.saucedemo.com/ webpage using the username and password


   url = https://www.saucedemo.com/
   username = standard_user
   password = secret_sauce
   """
    #driver = webdriver.chrome

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
       This method is to open up the chrome browser with the URL and makes the browser to go fullscreen. Then waits for 3 seconds
       :return:
       """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        """
       This method is used to close the webbrowser
       :return:
       """
        self.driver.quit()

    def login(self):
        self.boot()

        # This is to fill the username and the password
        self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
        sleep(3)
        self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
        sleep(3)
        # find the login button and click on it
        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(3)

        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successfully")
        else:
            print("Error")

        self.quit()

    def get_page_title(url):
        # Initialize the webdriver
        driver = webdriver.Chrome()  # You can use any other webdriver here as per your preference

        # Open the webpage
        driver.get(url)

        try:
            driver.get(url)

            # Get the title of the webpage
            page_title = driver.title

            return page_title

        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the webdriver
            driver.quit()

    # Example usage:
    url = "https://www.saucedemo.com/"
    title = get_page_title(url)
    print("Page title:", title)
    def get_pageContent(url):
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            page_content=driver.page_source
            return page_content
        except Exception as e:
            print("Error")
        finally:
            driver.quit()
        # Example usage:
    url = "https://www.saucedemo.com/"
    pageContent = get_pageContent(url)
    #print("Page content:", pageContent)
    #opening text file and writing into it
    with open("C:/Users/HP/Documents/Webpage_task_11.txt", "w") as textfile:
        textfile.write(pageContent)
    print("Page content copied to text file")
#creatig object for LoginAutomation class
obj = LoginAutomation()
#calling login method
obj.login()
#calling get title method
obj.get_page_title()
#calling pageContent method
obj.get_pageContent()