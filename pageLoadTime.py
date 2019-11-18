from selenium import webdriver
from selenium.webdriver.common import keys
import  time
import  stopwatch

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
url = driver.get('http://mmaplus.rtdtradetracker.com/')
driver.maximize_window()

# def pageLoad :
#             # pageLoad.start();
#             #
#             # driver.get("url");
#             #
#             # WebDriverWait wait = new WebDriverWait(driver, 10);
#             # wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("body")));
#             #
#             # pageLoad.stop();
#             #
#             #  pageLoadTime_ms = pageLoad.getTime();
#             long pageLoadTime_Seconds = pageLoadTime_ms / 1000;
#             System.out.println("Total Page Load Time: " + pageLoadTime_ms + " milliseconds");