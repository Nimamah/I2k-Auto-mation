from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
x=datetime.datetime.today()
y=x-datetime.timedelta(days = 1)
date = y.strftime("%Y-%m-%d")
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\py\chromedriver.exe")
driver.maximize_window()
driver.get("""https://10.15.33.232:31943/pm/themes/default/pm/app/history_pm_alone.html?curMenuId=com.iemp.app.pm.historypm&
indexs=16090%2C16090%2C16090%2C16090%2C16090%2C16090%2C16090%
2C16090&monitorPortletID=CustomPortlet1443451951661&timeRange=24""")
user = driver.find_element_by_id("txf_username")
user.send_keys("username")
pas = driver.find_element_by_id("txf_imtinfo")
pas.send_keys("password")
login = driver.find_element_by_css_selector("#btn_submit")
login.click()
sleep(15)
time_range = driver.find_element_by_css_selector("#timerange_7")
time_range.click()
sleep(3)
time_set = driver.find_element_by_css_selector("#cusStartTime_value")
time_set.click()
sleep(1)
time_set.send_keys("%s 00:00 DST" % (date))
time_set = driver.find_element_by_css_selector("#cusEndTime_value")
time_set.click()
sleep(1)
time_set.send_keys("%s 23:59 DST" % (date))
refresh = driver.find_element_by_css_selector("""#btnSearch_button > span.eviewButton_buttonCenterText.eviewButton_buttonCenterTextFont""")
refresh.click()
sleep(10)
body = driver.find_element_by_css_selector("#pm_main_body")
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
sleep(10)
#selection for screen shot 


def city11scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    rahahan2 = driver.find_element_by_css_selector(rah2)
    rahahan2.click()
    sleep(2)
    city41 = driver.find_element_by_css_selector(sh1)
    city41.click()
    sleep(2)
    city42 = driver.find_element_by_css_selector(sh2)
    city42.click()
    sleep(2)
    city31 = driver.find_element_by_css_selector(m1) 
    city31.click()
    sleep(2)
    city32 = driver.find_element_by_css_selector(m2) 
    city32.click()
    sleep(2)
    body.send_keys(Keys.ARROW_DOWN)
    body.send_keys(Keys.ARROW_UP)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city11.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city12scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    rahahan1 = driver.find_element_by_css_selector(rah1)
    rahahan1.click()
    sleep(2)
    rahahan2 = driver.find_element_by_css_selector(rah2)
    rahahan2.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city12.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city41scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    rahahan2 = driver.find_element_by_css_selector(rah2)
    rahahan2.click()
    sleep(2)
    city41 = driver.find_element_by_css_selector(sh1)
    city41.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city41.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city42scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    city41 = driver.find_element_by_css_selector(sh1)
    city41.click()
    sleep(2)
    city42 = driver.find_element_by_css_selector(sh2)
    city42.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city42.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city31scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    city42 = driver.find_element_by_css_selector(sh2)
    city42.click()
    sleep(2)
    city31 = driver.find_element_by_css_selector(m1) 
    city31.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city31.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city32scsh ():
    rah1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div" 
    rah2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div" 
    sh1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div" 
    sh2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div" 
    m1 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div" 
    m2 = "#iemp_real_time_pm_chart_0 > div > div.dygraph-legend > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > div"
    city31 = driver.find_element_by_css_selector(m1) 
    city31.click()
    sleep(2)
    city32 = driver.find_element_by_css_selector(m2) 
    city32.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city32.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city2ss1 ():
    t1="#iemp_real_time_pm_chart_1 > div > div.dygraph-legend > div > table > tbody > tr > td:nth-child(1) > div"
    t2="#iemp_real_time_pm_chart_1 > div > div.dygraph-legend > div > table > tbody > tr > td:nth-child(2) > div"
    city22 = driver.find_element_by_css_selector(t2)
    city22.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city21.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
def city2ss2 ():
    t1="#iemp_real_time_pm_chart_1 > div > div.dygraph-legend > div > table > tbody > tr > td:nth-child(1) > div"
    t2="#iemp_real_time_pm_chart_1 > div > div.dygraph-legend > div > table > tbody > tr > td:nth-child(2) > div"
    city21 = driver.find_element_by_css_selector(t1)
    city21.click()
    sleep(2)
    city22 = driver.find_element_by_css_selector(t2)
    city22.click()
    sleep(2)
    driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\py\gprs\city22.png")
    import winsound
    winsound.Beep(2500,500)
    body.click()
    sleep(1)
city11scsh ()
city12scsh ()
city41scsh ()
city42scsh ()
city31scsh ()
city32scsh ()
body.send_keys(Keys.END)
body.click()
city2ss1 ()
city2ss2 ()
export = driver.find_element_by_css_selector("#btnExportData_button > span.eviewButton_buttonCenterText.eviewButton_buttonCenterTextFont")
export.click()
import winsound
winsound.Beep(2500,1000)
logout = driver.find_element_by_css_selector("#login_logoutIcon")
logout.click()
yes = driver.find_element_by_css_selector("#fw_btn_ok > div")
yes.click()
sleep(5)
driver.close()
from PIL import Image
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
if __name__ == '__main__':
    image = 'city12.png'
    crop(image, (30, 120,1344,600 ), 'city12crop.png')
if __name__ == '__main__':
    image = 'city11.png'
    crop(image, (30, 120,1344,600 ), 'city11crop.png')
if __name__ == '__main__':
    image = 'city31.png'
    crop(image, (30, 120,1344,600 ), 'city31crop.png')   
if __name__ == '__main__':
    image = 'city32.png'
    crop(image, (30, 120,1344,600 ), 'city32crop.png')
if __name__ == '__main__':
    image = 'city21.png'
    crop(image, (30, 180,1344,610 ), 'city21crop.png')
if __name__ == '__main__':
    image = 'city22.png'
    crop(image, (30, 180,1344,610 ), 'city22crop.png')
if __name__ == '__main__':
    image = 'city41.png'
    crop(image, (30, 120,1344,600 ), 'city41crop.png')
if __name__ == '__main__':
    image = 'city42.png'
    crop(image, (30, 120,1344,600 ), 'city42crop.png')
