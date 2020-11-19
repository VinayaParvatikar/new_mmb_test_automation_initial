import time

from pageobjects.base import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class MainMenu(PageObject):
    def close_help(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()

    def add_project(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/a[1]/i').click()
        new_proj_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/span')
        time.sleep(1)
        new_proj_field.click()
        #assert new_proj_field.text == 'PROJECT'

    def edit_project_name(self):
        edit_proj_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/i')
        edit_proj_field.click()
        #edit_new_proj_name = self.driver.find_element_by_xpath(
        #    '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/input')
        input_proj_name = self.driver.find_element_by_class_name('grid-input-cell')
        input_proj_name.click()
        time.sleep(1)
        input_proj_name.clear()
        assign_proj_name = 'PROJECT'
        input_proj_name.send_keys(assign_proj_name)
        time.sleep(2)
        proj_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]')
        #proj_field.send_keys(Keys.RETURN)
        #time.sleep(2)
        proj_field.send_keys(Keys.RETURN, Keys.UP)
        #proj_field.send_keys(Keys.DOWN)

    def create_new_blank_budget(self):
        new_budget_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/div[1]/span/i')
        new_budget_field.click()
        new_blank_budget_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/div[1]/div/div[1]/span')
        new_blank_budget_field.click()
        time.sleep(2)
        new_untitled_budget = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div/div[2]/div[1]')
        action = ActionChains(self.driver)
        action.double_click(new_untitled_budget)
        action.perform()
        time.sleep(2)
        input_budget_name = self.driver.find_element_by_class_name('grid-input-cell')
        input_budget_name.clear()
        assign_budget_name = 'budget_auto'
        input_budget_name.send_keys(assign_budget_name)
        time.sleep(2)
        open_budget = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div/div[2]/div/div[1]')
        action.double_click(open_budget)
        action.perform()
        time.sleep(2)
        budget_window = self.driver.window_handles[0]
        self.driver.switch_to.window(budget_window)
        opened_budget_name = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/a/div[1]/span')
        assert opened_budget_name.text == assign_budget_name

    def edit_account(self, acct_no, desc):
        account_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]')
        action = ActionChains(self.driver)
        action.double_click(account_field)
        action.perform()
        edit_account_field = self.driver.find_element_by_class_name('grid-input-cell')
        edit_account_field.send_keys(acct_no)
        time.sleep(1)
        edit_account_field.send_keys(Keys.TAB)
        desc_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[3]')
        action = ActionChains(self.driver)
        action.double_click(desc_field)
        action.perform()
        edit_desc_field = self.driver.find_element_by_class_name('grid-input-cell')
        edit_desc_field.send_keys(desc)
        time.sleep(1)

    def add_category_topsheet(self):
        self.edit_account('1101', 'desc1')

    def add_account_level(self):
        select_topsheet_row = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]')
        action = ActionChains(self.driver)
        action.double_click(select_topsheet_row)
        action.perform()
        time.sleep(1)
        self.edit_account('110101', 'acct1')

    def add_detail(self):
        select_account = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]')
        action = ActionChains(self.driver)
        action.double_click(select_account)
        action.perform()
        time.sleep(1)

    def enable_setups_detail_line(self):
        ellipsis = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[10]/i')
        ellipsis.click()
        time.sleep(2)









    def delete_project(self):
        delete_proj = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/a[2]/i')
        delete_proj.click()
        time.sleep(2)


    '''
    def __menu_button(self): return self.driver.find_element_by_css_selector('#menuButton')

    def __logout_button(self): return self.driver.find_element_by_css_selector(
            '#contentWrapper > paper-material > paper-menu > div > a:nth-child(3)')

    def __quit_button(self): return self.driver.find_element_by_css_selector(
            '#contentWrapper > paper-material > paper-menu > div > a:nth-child(4)')

    def __open_menu(self):
        self.__menu_button().click()
        time.sleep(1)  # slide-in animation time

    def logout(self):
        """Only available if user is already logged in."""
        self.__open_menu()
        self.__logout_button().click()

    def quit(self):
        self.__open_menu()
        self.__quit_button().click()
    
    
    '''