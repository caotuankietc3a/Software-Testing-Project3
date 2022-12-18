from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
from TestUtils import Utils
class CreateCourseUtils:
    URLCREATECOURSE = "http://localhost/course/edit.php?category=0"

    @staticmethod
    def test(fName, sName, startDate, endDate, id):
        Utils.driver.get(CreateCourseUtils.URLCREATECOURSE)
        # Course FullName
        CreateCourseUtils.textFieldHandler(fName, "id_fullname")

        # Course ShortName
        CreateCourseUtils.textFieldHandler(sName, "id_shortname")

        # Check for StartDate
        CreateCourseUtils.selectOptionsHandler(startDate.day, "id_startdate_day")
        CreateCourseUtils.selectOptionsHandler(startDate.month, "id_startdate_month")
        CreateCourseUtils.selectOptionsHandler(startDate.year, "id_startdate_year")
        CreateCourseUtils.selectOptionsHandler(startDate.hour, "id_startdate_hour")
        CreateCourseUtils.selectOptionsHandler(startDate.minute, "id_startdate_minute")

        # Check for EndDate
        CreateCourseUtils.selectOptionsHandler(endDate.day, "id_enddate_day")
        CreateCourseUtils.selectOptionsHandler(endDate.month, "id_enddate_month")
        CreateCourseUtils.selectOptionsHandler(endDate.year, "id_enddate_year")
        CreateCourseUtils.selectOptionsHandler(endDate.hour, "id_enddate_hour")
        CreateCourseUtils.selectOptionsHandler(endDate.minute, "id_enddate_minute")

        # Check for Course Id 
        courseId = Utils.driver.find_element(By.ID, "id_idnumber");
        courseId.clear()
        courseId.send_keys(str(id))
        time.sleep(3)

        # Check SaveAndDisplay Btn 
        btnSaveAndDisplay = Utils.driver.find_element(By.ID, "id_saveanddisplay")
        btnSaveAndDisplay.click()

        try:
            """Failly Add Course"""
            if Utils.driver.find_element(By.ID, "id_saveanddisplay").is_displayed():
                return False
        except NoSuchElementException:
            """Successfully Add Course"""
            return True 


    @staticmethod
    def selectOptionsHandler(value, fieldId):
        selectEl = Utils.driver.find_element(By.ID, fieldId);
        options = selectEl.find_elements(By.TAG_NAME, "option")
        # print(Select(selectEl).first_selected_option.text)
        for option in options:
            if option.get_attribute("value") == str(value):
                option.click()

    @staticmethod
    def textFieldHandler(value, fieldId):
        textEl = Utils.driver.find_element(By.ID, fieldId);
        textEl.clear()
        textEl.send_keys(str(value))

class RemoveCourseUtils:
    URLREMOVECOURSE = "http://localhost/moodle/course/management.php"
    REMOVECOURSE_ICON_XPATH= "//a[starts-with(@href, 'http://localhost/moodle/course/delete.php')]" 
    DELETECOURSE_BTN_XPATH= "//form[@method='post']//button[@type='submit']" 

    @staticmethod
    def test():
        Utils.driver.get(RemoveCourseUtils.URLREMOVECOURSE)

        try:
            icon = Utils.driver.find_element(By.XPATH, RemoveCourseUtils.REMOVECOURSE_ICON_XPATH)
            if icon.is_displayed():
                time.sleep(0.5)
                icon.click()
                time.sleep(0.5)
                Utils.driver.find_element(By.XPATH, RemoveCourseUtils.DELETECOURSE_BTN_XPATH).click()
                Utils.driver.get(RemoveCourseUtils.URLREMOVECOURSE)
                return True
        except NoSuchElementException:
            return False
