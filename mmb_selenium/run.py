import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageobjects.login import LoginPage
from pageobjects.menu import MainMenu

chromedriver_path = "C:\\Users\\vp094039\\Downloads\\chromedriver-v3.1.6-win32-ia32\\chromedriver"
electron_path = "C:\\Users\\vp094039\\AppData\\Local\\Programs\\mmb-ui\\Movie Magic Budgeting.exe"

opts = Options()
opts.binary_location = electron_path
driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)
driver.implicitly_wait(15)  # seconds

time.sleep(3)  # wait for application to start

login_page = LoginPage(driver)
login_page.login('vinaya.parvatikar@accionlabs.com', 'Welcome123$')

time.sleep(5)  # wait for sign in

main_menu = MainMenu(driver)
main_menu.close_help()
main_menu.add_project()
main_menu.edit_project_name()
main_menu.create_new_blank_budget()
main_menu.add_category_topsheet()
main_menu.add_account_level()
main_menu.add_detail()
main_menu.enable_setups_detail_line()

#main_menu.delete_project()

#main_menu.logout()

time.sleep(3)  # wait for logout

#main_menu.quit()

driver.quit()