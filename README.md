# This Python project displays the web scraping method from a live web site. Web scraping is very useful for data collection and analysis .



### Technology used:
	
	1.Python
	2.mysql

### Library used :

1.Selenium
2.Database Module
3.Sql connector


## This project produce  the  jobs that are present in the live website and store it in a local database



#### NOTE : The current code and environment is path dependent and machine dependent , for windows or linux we need different chrome driver and path specification.

### How to use? 
1.open main.py and run it will ask for input and it will automatically save in local database
(as project is machine dependent so we need few modification to run on different machine)


### Description

We have given input as “python” for search in “naukri.com” and got a list of jobs and companies.
Using nested list and list data structure we pass the object to the database to store the values in the local database for further analysis of data.

 > input : python
<img width="1384" alt="Screenshot 2022-07-01 at 1 27 34 PM" src="https://user-images.githubusercontent.com/56749539/176851771-6df7a03e-1220-4edc-ac4d-45c14ec962d8.png">


 > fetching live data and printing the list of result
<img width="1384" alt="Screenshot 2022-07-01 at 1 28 56 PM" src="https://user-images.githubusercontent.com/56749539/176851810-7aed468e-97e8-4802-9285-76a1a12f23e5.png">

 > we have scrap out the list of job titels and company name from live and dynamic website.
<img width="1312" alt="Screenshot 2022-07-01 at 1 31 08 PM" src="https://user-images.githubusercontent.com/56749539/176851823-a95b416b-0cf7-4908-a458-6c3510da36fb.png">

 > The live data we have fetched are now stored in the local mysql database.
<img width="920" alt="Screenshot 2022-07-01 at 1 17 19 PM" src="https://user-images.githubusercontent.com/56749539/176851877-e62788f5-3865-4900-9ebc-d1331df96e9b.png">



### conclusion

1.We use the same web scraping technique to scrape out the information from the web and can do data analysis .
2.We also restore the web data in local as well as in the cloud .




