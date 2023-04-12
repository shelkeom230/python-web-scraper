# scraping covid-19 data 
# grab the page 
import requests 

# make requests from webpage 
result=requests.get('https://www.worldometers.info/coronavirus/country/india/')

# extract data from website 
import bs4

# creating soup object 
soup=bs4.BeautifulSoup(result.text,'lxml')

# Searching div tags having maincounter-number class
cases = soup.find_all('div' ,class_= 'maincounter-number')

# sort the data 
# list to store number of cases 
data=[]

# find the span and get data from it 
for i in cases:
	span=i.find('span')
	data.append(span.string)
# display number of cases
print(data)

# processing the data 
# load the data into excel file 
import pandas as pd
df=pd.DataFrame({"coronaData":data}) 

# naming the columns 
df.index=['TotalCases','Deaths','Recovered']

# export into excel 
df.to_csv('Corona_data.csv')
