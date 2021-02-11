from datetime import date, datetime
from time import daylight


class StartEndDate_and_BlockingRecipe:

    def time():
        
        today_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
        enddate = datetime(2021,2,11)
        
        return (today_date < enddate)

    
    file_location = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    website = ["www.facebook.com", "www.instagram.com"]


    

# add blocklist site in HOST file
class MainProcess(StartEndDate_and_BlockingRecipe):

    def mainfuntion(self):

        while True:      
            if StartEndDate_and_BlockingRecipe.time():
                with open(self.file_location, "r+") as file:
                    content = file.read()

                    for site in self.website:
                        if site not in content:
                            file.write(f'{self.redirect} {site}\n')
                        
                        else:
                            return 'already exits'
                
                break
        

obj = MainProcess()
print(obj.mainfuntion())

class DeleteBlockSite(StartEndDate_and_BlockingRecipe):

    def removesite(self):
        

        with open(self.file_location, "r+") as file:
            content = file.read()

            for site in self.website:
                if site in content:
                    content = content.replace(f'{self.redirect} {site}', "")
            return content


# obj = DeleteBlockSite()
# print(obj.removesite())