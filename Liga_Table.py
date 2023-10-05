
#######################################################################
#######################La Liga Table###################################
#######################################################################

#Import libraries and functions
from bs4 import BeautifulSoup
import requests
import pandas as pd

#url web 
url="https://resultados.as.com/resultados/futbol/primera/clasificacion/"

#request url
page=requests.get(url)

#format html.parser
soup=BeautifulSoup(page.content,"html.parser")

#inspect items of teams on web(All teams), label->, name -> nombre-equipo

Data_Teams= soup.find_all("span",class_="nombre-equipo")


List_Team=list()

count=0
for i in Data_Teams:
    if count<20:
        List_Team.append(i.text)
    else:
        break
    count= count+1

print(List_Team)

print(len(List_Team))

#inspect items of teams on web(All Pouints), label->, name -> destacado

Points= soup.find_all("td",class_="destacado")

print(Points)

List_Points=list()

count=0
for i in Points:
    if count<20:
        List_Points.append(i.text)
    else:
        break
    count= count+1  

print(List_Points)


#Set of Teams and points

df=pd.DataFrame ({"Name":List_Team, "Points":List_Points}, index=list(range(1,21)))
print(df)

df.to_csv("Liga_Table.csv",index=False)  #csv
df.to_csv("Liga_Table",index=False)  #notebook



