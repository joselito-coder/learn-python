import notify2
from bs4 import BeautifulSoup,Comment
import requests
import time
import os

# Function to send notification
def notifyMe(title,message):
    notify2.init("Covid notify")

    # Absolute path of the icon
    ICON_PATH =  os.path.join(os.path.abspath('.'),"icon.ico")

    n = notify2.Notification(title, message=message, icon=ICON_PATH)
    n.set_urgency(notify2.URGENCY_NORMAL)
    # set the timeout
    n.set_timeout(1000)
    n.show()


# function that  returns html of any url provided
def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    print(os.path.join(os.path.abspath('.'),"icon.ico"))
    while True:
        # get html data and parse it
        myHtmlData = getData('https://www.mohfw.gov.in')
        soup = BeautifulSoup(myHtmlData,'html.parser')
        table = soup.find('table')

        # The tbody is commented so do this inorder to extract the data
        comments = table.findAll(text=lambda text:isinstance(text, Comment))
        data_table = str(comments[0])
        table_parser = BeautifulSoup(data_table,'html.parser')


        item_list = []
        for data in table_parser.find_all('tr'):
            item_list.append(data.get_text().split("\n")[1:])

        # Send notification
        states = ["Goa","Maharashtra","Chandigarh"]
        for item in item_list[:35]:
            if item[1] in states:
                nTitle = "Cases of Covid-19"
                nText = f"State:\t{item[1]}\n Active Cases: {item[2]}\nCured Cases:{item[3]}\nDeaths: {item[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        # sleep for 1 hour
        time.sleep(60 * 60)
