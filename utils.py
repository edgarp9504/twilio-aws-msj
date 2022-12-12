from twilio_config import API_KEY_WAPI,TWILIO_AUTH_TOKEN,PHONE_NUMBER,TWILIO_ACCOUNT_SID
from twilio.rest import Client
import pandas as pd

import requests
    



def twilio_msj(mensaje):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body='\n\n' + str(mensaje),
            from_=PHONE_NUMBER,
            to='+529983253195'
        )

    return message.sid
    
def api():
    
    url = "https://api.apilayer.com/exchangerates_data/convert?to=MXN&from=USD&amount=1"
    headers= {
    "apikey": "cbCFAZrYCiPvoXEt3HDb4uX278tKG6hn"
    }

    response = requests.get(url, headers=headers).json()
    print(response)
    
    return response 

def table(response):
        

    exchange = int(response['info']['rate'])
    date = response['date']
    from_exchange = response['query']['from']
    to_exchange = response['query']['to']
    
    
    data = {'Tipo de cambio' : [exchange],'Fecha': [date], 'Moneda Extrangera': [from_exchange], 'Moneda Local': [to_exchange]}
    table = pd.DataFrame(data)
    print(table)
    
    return table
    