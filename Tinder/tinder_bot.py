from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(10)
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')

        fb_btn.click()

        # Switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('')
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('')

        btn_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        btn_login.click()

        self.driver.switch_to.window(base_window)

        sleep(5)

        btn_enable_geo_location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        btn_enable_geo_location.click()

        sleep(2)
        
        btn_enable_notification_match = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        btn_enable_notification_match.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()
    
    def deslike(self):
        deslike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        deslike_btn.click()
    
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_match_popup()
                except Exception:
                    self.close_popup()

    def close_match_popup():
        close_mach_popup = bot.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        close_mach_popup.click()

    def close_popup():
        


bot = TinderBot()
bot.login()



