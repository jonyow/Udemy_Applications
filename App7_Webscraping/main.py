
from bs4 import BeautifulSoup

import requests
import pandas as pd

# r = requests.get("http://pythonhow.com/example.html")
#
# c = r.content
#
# soup  = BeautifulSoup(c, "html.parser")
#
# all = soup.find_all("div", {"class":"cities"})
#
# all_h2 = {x.find_all("h2")[0].text : x.find_all("p")[0].text   for x in all}

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c = r.content
soup  = BeautifulSoup(c, "html.parser")

#with open("test.txt", "w") as file:
#    file.write(soup.text)

all_props = soup.find_all("div", {"class":"propertyRow"})

all_prop_details = all_props[0].find("h4", {"class":"propPrice"} ).text.replace("\n", "").replace(" ", "")

def TryFind(x, name, class_name, index = 0):
    items = x.find_all(name, {"class": class_name})

    if len(items) > index:
        return(items[index].text)
    else:
        return("")

def ExtractPropDetails(x):
    dict = {}
    dict["Price"] = x.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
    dict["Address 1"] = x.find_all("span", {"class": "propAddressCollapse"})[0].text
    dict["Address 2"] = x.find_all("span", {"class": "propAddressCollapse"})[1].text
    dict["Beds"] = TryFind(x, "span",  "infoBed")

    for column_group in x.find_all("div", {"class": "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}),
                                               column_group.find_all("span", {"class": "featureName"})):
           # print(feature_group.text, feature_name.text)
            if feature_group.text == "Lot Size: ":
                dict["Lot Size"] = feature_name.text
                break

    return(dict)


x = all_props[4]

all_prop_details = [ExtractPropDetails(x) for x in all_props]

pd.DataFrame(all_prop_details)


ExtractPropDetails(all_props[0])

for column_group in x.find_all("div", {"class":"columnGroup"}):
    for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
        print(feature_group.text, feature_name.text)
        if feature_group.text == "Lot Size: ":
            #dict["Lot Size"] = feature_name.text
            print(feature_name.text)
            break

all_props[5].find_all("", {"class": "featureGroup"})