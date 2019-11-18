class HomePage():

    def __init__(self, drive):

        self.driver = drive
        self.logout_button = "logo"


    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button).click()
