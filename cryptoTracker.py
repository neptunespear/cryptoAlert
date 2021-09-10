import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
import smtplib
import getpass


def send_email():
    # create message object instance
    msg = MIMEMultipart()

    # the parameters of the message
    password = your_password
    msg['From'] = your_email
    msg['To'] = send_email_to
    msg['Subject'] = "Bitcoin price, ACT FAST"

    # your message
    message = "Dear " + your_name + "\nBitcoin prices are now " + str(
        bitcoin_price) + ". Better buy quick.\nRegards,\n" + your_name

    # adds in the message from the above variable
    msg.attach(MIMEText(message, 'plain'))

    # create the gmail server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Creds for sending the email
    server.login(msg['From'], password)

    # sends the message
    server.sendmail(msg['From'], msg['To'], message)

    server.quit()

    # prints to your console
    print("successfully sent email to %s:" % (msg['To']))
    print("Price of your entered bitcoin is at " + str(bitcoin_price))


# user inputs
your_name = input('Enter your name: ')
your_email = input('Enter your email address (gmail only): ')
your_password = getpass.getpass()
send_email_to = input('Enter email address to send to: ')
enter_bitcoin_name=input('Enter the bitcoin name you have to get alert: ')
alert_amount = input('Alert if this Bitcoin price equals to the alert price: ')


while True:
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
    )
    data = response.json()

    for i in range(len(data)):
        current_id=i['id'];
        if current_id==name:
            bitcoin_name = i['name'];
            bitcoin_image = i['image'];
            bitcoin_price = int(i['current_price']);
            while bitcoin_price < int(alert_amount):
                print(bitcoin_name)
                image=Image.open(bitcoin_image)
                image.show()
                print(bitcoin_price)
                time.sleep(120)        #again get the price in 2 minutes
            else:
                send_email()
                print(bitcoin_name)
                image=Image.open(bitcoin_image)
                image.show()
                print('Reached your alert price .Now you should go and puchase your favourite bitcoin. Ctrl + C to quit.')
                time.sleep(180)
