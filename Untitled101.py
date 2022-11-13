#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By ## this is work on driver.find_by_element


driver = webdriver.Chrome(executable_path = "chromedriver.exe")

driver.implicitly_wait(10)  # it is similar to the time sleep method

driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element(By.NAME,"q").send_keys("http://orangehrm.qedgetech.com/")
#driver.find_element("name",'btnK').click()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)

driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()


driver.close()
driver.quit()

print("Test Completed")


# In[ ]:




