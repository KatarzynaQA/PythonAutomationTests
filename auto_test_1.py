from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")
driver.get("https://autodemo.testoneo.com/en/")
title = driver.title
print(title)
driver.quit()