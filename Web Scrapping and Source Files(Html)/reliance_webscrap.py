from bs4 import BeautifulSoup

with open("ht.html", "r+") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
# print(soup)

tbody = soup.find("tbody")
# print(tbody)

rows = tbody.find_all("tr")
print(len(rows))  # no of records

for row in rows:

    file = open("reliance_stock_data.csv", "a+")
    columns = row.find_all("td")
    file.write("\n")
    for i in range(len(columns)):
        file.write(str(columns[i].text))
        file.write(",")
