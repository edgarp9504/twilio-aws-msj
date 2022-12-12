#own library
from utils import twilio_msj, api, table





if __name__ == '__main__':
    ##llamado al API
    response = api()
    
    table = table(response)
    
    send_msg = twilio_msj(table)
    
    





