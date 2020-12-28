from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

def getnum(name, upass):
    number = ["NULL", "NULL", "NULL"]
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("http://kimlik.ege.edu.tr")

    username = driver.find_element_by_id("username")
    username.send_keys(name)

    passwd = driver.find_element_by_id("password")
    passwd.send_keys(upass)

    driver.find_element_by_xpath("/html/body/section/div/div[2]/div[1]/table/tbody/tr[4]/td/div/div[1]/button").click()
    
    try:
        bilgilerim = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[15]/div[10]/a").get_attribute('href')
        driver.get(bilgilerim)
        number[0] = driver.find_element_by_id("grdIletisim_ctl00__0").text
        number[1] = driver.find_element_by_id("grdIletisim_ctl00__1").text
        number[2] = driver.find_element_by_id("grdIletisim_ctl00__2").text
        return number
    except:
        return number
