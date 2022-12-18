from selenium.webdriver.common.by import By
import time
from TestUtils import Utils


class LoginSite:
    USERNAME = "user"
    PASSWORD = "bitnami"
    URLLOGINPAGE = "http://localhost/"
    LOGOUT_BUTTON_XPATH = "//a[starts-with(@href, 'http://localhost/login/logout.php')]"
    LOGIN_BUTTON_XPATH = "//a[starts-with(@href, 'http://localhost/login/index.php')]"

    @staticmethod
    def logIn():
        Utils.driver.get(LoginSite.URLLOGINPAGE)
        Utils.driver.find_element(By.XPATH, LoginSite.LOGIN_BUTTON_XPATH).click()
        username = Utils.driver.find_element(By.ID, "username")
        password = Utils.driver.find_element(By.ID, "password")
        loginBtn = Utils.driver.find_element(By.ID, "loginbtn")
        username.clear()
        password.clear()
        username.send_keys(LoginSite.USERNAME)
        password.send_keys(LoginSite.PASSWORD)
        loginBtn.click()

    @staticmethod
    def logOut():
        powermenu_btn = Utils.driver.find_element(By.ID, "user-menu-toggle")
        if powermenu_btn.is_displayed():
            time.sleep(0.5)
            powermenu_btn.click()
            Utils.driver.find_element(By.XPATH, LoginSite.LOGOUT_BUTTON_XPATH).click()
            return
