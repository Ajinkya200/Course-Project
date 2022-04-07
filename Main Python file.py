import random
import pandas as pd
import pip
from pretty_html_table import build_table
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import bs4
from bs4 import BeautifulSoup as bs
import requests


link= input("paste the link ")
page = requests.get(link)
page.content
soup = bs(page.content, 'html.parser')
#it gives us the visual representation of data
#print(soup.prettify())
name=soup.find('div',class_="_4rR01T")

#get other details and specifications of the product
specification=soup.find('div',class_="fMghEO")
#print(specification)
specification.text
for each in specification:
    spec=each.find_all('li',class_='rgWa7D')

print("connecting to server")
#get price of the product
price=soup.find('div',class_='_30jeq3 _1_WHN1')
#print(price.text)
price.text
products=[]              #List to store the name of the product
prices=[]          #List to store price of the productratings=[]               #List to store rating of the product
specification1s = []                #List to store supported apps
ratings = []
specification2s = []                  #List to store operating system

for data in soup.findAll('div', class_='_3pLy-c row'):
    names = data.find('div', attrs={'class': '_4rR01T'})
    price = data.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = data.find('div', attrs={'class': '_1lRcqv'})
    specification = data.find('div', attrs={'class': 'fMghEO'})

    for each in specification:
        col = each.find_all('li', attrs={'class': 'rgWa7D'})
        specification1= col[0].text
        specification2 = col[1].text
        #sound_ = col[3].text
        rating = col[3].text
        products.append(names.text) # Add product name to list
        prices.append(price.text)# Add price to list
        ratings.append(rating)
        specification1s.append(specification1)# Add supported apps specifications to list
        specification2s.append(specification2) # Add operating system specifications to list


print("collecting  information about the products")
import pandas as pd
df=pd.DataFrame({'Product Name':products,'Supported_apps':specification1s,'os': specification2s , 'rating': ratings, 'Price': prices})
#df.head(10)
#print(df1)
df2 =  pd.DataFrame(df)
#print('DataFrame:\n', df2)

result = df.to_string(na_rep = 'Missing')
#print(result)
result1 = result.encode('ascii', 'ignore').decode('ascii')

print("information collected succesfully")

import smtplib, ssl
background = ("green_light","blue_light")
output = build_table(df, random.choice(background))

def send_mail(body):
  message = MIMEMultipart()
  message['Subject'] = 'Product description'
  message['From'] = "forprojectpython@gmail.com"
  message['To'] = input("type your email ")

  body_content = body
  message.attach(MIMEText(body_content, "html"))
  msg_body = message.as_string()

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login("forprojectpython@gmail.com","webscrapping")
  server.sendmail(message['From'], message['To'], msg_body)
  server.quit()
  print("email sent")


  print("Thank you for using our services   :)")
send_mail(output)


