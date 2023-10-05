
#######################################################################
###################Premier League Table################################
#######################################################################


from bs4 import BeautifulSoup
import requests
import pandas as pd

#url web 
url="https://www.theguardian.com/football/premierleague/table"

#request url
page=requests.get(url)

#format html.parser
soup=BeautifulSoup(page.content,"html.parser")

#inspect items of teams on web(All teams), label->span, name -> team-name

Data_Teams= soup.find_all("a",class_="team-name__long")
   

#List of teams
List_Team=list()

#Loop for finding just Teams without repeating and appending in List_Team
# just counting 20 teams

count=0

for i in Data_Teams:
    if count<20:
        
        ##filtering information##
        import re
        i=i.text
        i=re.sub("[^A-Za-z]","",i)
        
        List_Team.append(i)
    else:
        break
    count= count+1

print(List_Team)
print(len(List_Team))

#df[List_Team].str.replace(r"\W","")

Point_Team= soup.find_all("b")


Point_Team_list=list()

#Loop for finding just Teams without repeating and appending in List_Team
# just counting 20 teams
count=0
for i in Point_Team:
    if count<20:
        Point_Team_list.append(i.text)
    else:
        break
    count= count+1

print(Point_Team)

#Data Frame#
df=pd.DataFrame ({"Name":List_Team, "Points":Point_Team_list}, index=list(range(1,21)))
print(df)

df.to_csv("Premier_Table.csv")  #csv
df.to_csv("Premier_Table")  #notebook