from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import settings
import mylib

##Set options
options = settings.getOpt()
chromedriver = "bin/chromedriver"

##Login with id and pw
def login(id, pw):
    contact = ["NULL", "NULL", "NULL"]
    driver = webdriver.Chrome(executable_path= chromedriver, chrome_options=options)
    driver.get("http://kimlik.ege.edu.tr")

    username = driver.find_element_by_id("username")
    username.send_keys(id)

    password = driver.find_element_by_id("password")
    password.send_keys(pw)

    driver.find_element_by_xpath("/html/body/section/div/div[2]/div[1]/table/tbody/tr[4]/td/div/div[1]/button").click()
    
    ##if following element exists it means we logged in and keeps going process of getting informations of user
    ##else returns NULL number array
    try:
        bilgilerim = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[15]/div[10]/a").get_attribute('href')
        driver.get(bilgilerim)
    except NoSuchElementException:
        print("could not login this account: ", id)
        return contact
    
    getnum(driver,contact)
    driver.close()

    return mylib.edit(contact)

##Try-Catch block for testing if contact value exists for number1, numbee2 and e-mail
def getnum(driver, contact):
    try:
        contact[0] = driver.find_element_by_id("grdIletisim_ctl00__0").text
    except NoSuchElementException:
        pass
    try:
        contact[1] = driver.find_element_by_id("grdIletisim_ctl00__1").text
    except NoSuchElementException:
        pass
    try:
        contact[2] = driver.find_element_by_id("grdIletisim_ctl00__2").text
    except NoSuchElementException:
        pass