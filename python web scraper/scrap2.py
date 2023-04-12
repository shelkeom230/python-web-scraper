# scrapping IPL auction 2019-2020 season data 
# import libraries 
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

# requesting and parsing URL 
url='https://www.cricbuzz.com/cricket-series/ipl-2020/auction/completed'
get_url=rq.get(url)
soup=BeautifulSoup(get_url.text,"html.parser")

# getting web elements 
Name= [i.text for i in soup.findAll('div',{'class':'cb-font-18'})]
Sold_Unsold= [i.text for i in soup.findAll('div',{'class':'cb-col cb-col-20 cb-lst-itm-sm'})]

# Just a little tweaking here and there like replacing ‘\xa0\xa0’ with blank in the Price columns and Sold_To columns.
Base_Price= [i.text for i in soup.findAll('div',{'class':'cb-col cb-col-33 cb-lst-itm-sm text-left','class':'cb-font-16'})]
Base_Price=Base_Price[0:len(Base_Price)-3:3]
Base_Price=[i.replace('\xa0\xa0',' ') for i in Base_Price]
Final_Price= [i.text for i in soup.findAll('div',{'class':'cb-col cb-col-33 cb-lst-itm-sm text-left','class':'cb-font-16'})]
Final_Price=Final_Price[1:len(Final_Price)-3:3]
Final_Price=[i.replace('\xa0\xa0',' ') for i in Final_Price]
Sold_To= [i.text for i in soup.findAll('div',{'class':'cb-col cb-col-33 cb-lst-itm-sm text-left','class':'cb-font-16'})]
Sold_To=Sold_To[2:len(Sold_To)-3:3]
Sold_To=[i.replace('\xa0\xa0',' ') for i in Sold_To]
Role= [i.text for i in soup.findAll('div',{'class':'cb-col cb-col-80','class':'cb-font-12 text-gray'})]
Role=Role[0::4]
Role=[i.split(' • ')[0] for i in Role]

# store in csv 
Table=pd.DataFrame({
    "Name":Name,
    "Role": Role,
    "Status":Sold_Unsold,
    "Base Price": Base_Price,
    "Final Price": Final_Price,
    "Team": Sold_To })
Table.replace("-","",inplace=True)
Table.to_csv("IPLAuction2019.csv")