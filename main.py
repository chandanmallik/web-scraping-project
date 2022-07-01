

"""

web scraping project module to find the top list of job with company
1,python module needed selenium
databasemodule

"""





from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import databasemoduel




class Web_scaping:


    def __init__(self):
        self._search_parameter = None
        self._list_of_jobs_with_name = []
        
    

    def set_search_parameter(self,user_input : str):
        """
        function set the search parmater        
        param: user_input takes string,
        return: None
        """
        self._search_parameter =  user_input
    
    def web_find_jobs(self) -> list:
        """
        function will return the list of jobs and also display
        return : list of jobs
        """
        
        drive = Chrome(executable_path="/Volumes/Macintosh HD - Data/python/udemy/web_scaping_project/chromedriver")
        url = "https://www.naukri.com/"+ self._search_parameter+"-jobs"
        print(url)
        drive.get(url)
        time.sleep(10)

        # list of  jobs 

        list_of_job = drive.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
        list_of_job_company = drive.find_elements(by=By.CLASS_NAME, value="subTitle.ellipsis.fleft")
        #************************************************
        # testing
        # print("* * * "*10)
        # list_of_job
        # print("a length of list of job ",len(list_of_job))
        # print("b length of list of company ",len(list_of_job_company))

        print("* * * "*10)

        for i in list_of_job:
            print(i.text)
        
        print("* * * "*10)

        for i in list_of_job_company:
            print(i.text)

        #************************************************
        if len(list_of_job) != len(list_of_job_company):
            print("some thing went wrong")
            drive.quit()
        else:
            for i in range(len(list_of_job)):
                job = list_of_job[i].text
                company = list_of_job_company[i].text
                # print(job,company)
                self._list_of_jobs_with_name.append([job,company])
            
        
        drive.quit()
        


    def store_in_database_local(self):
        # data base , my sql
        
       
        print(self._list_of_jobs_with_name)
        databasemoduel.insert_data(self._list_of_jobs_with_name)
        




    def print_test(self):
       for i in self._list_of_jobs_with_name:
           print(f"JOB NAME: {i[0]} , COMPANY : {i[1]}")



base = Web_scaping()
search_keyword = input("Enter The Job related key word : ")
base.set_search_parameter(search_keyword)  
base.web_find_jobs() 
base.print_test()
base.store_in_database_local()
