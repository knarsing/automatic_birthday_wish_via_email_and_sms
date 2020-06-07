import pandas as pd
import datetime
import smtplib

import urllib.request
import urllib.parse

'''
def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': 'writ your third party sms sending gateway api key', 'numbers': mobile_number, 'message': 'hi', 'sender': 'senders name'}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)
'''



def sendSMS(apikey, numbers, sender, message):
    try:

        data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
            'message' : message, 'sender': sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        return(fr)
    except Exception as e:
        print("try run in between 9am to 9 pm")





#Email User Details
Gmail_ID='test@gmail.com'
Gmail_PSWD='your mail passowrd'

def sendEmail(to,sub,msg,name):
    print(f"Email to {to} sent with subject: {sub} and message: {msg}{name} :)")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(Gmail_ID,Gmail_PSWD)

    s.sendmail(Gmail_ID,to,f"Subject:{sub}\n\n {msg}")
    s.quit()

if __name__=="__main__":
    #for testing only
    #sendEmail(Gmail_ID,"subject","test message")
    #exit()
    resp=sendSMS('API','sender mobile number','TXTLCL','Hi Guruji,This is SMS API integration and send a auto sms')
    print(resp)
    exit()
    df=pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%Y")


    writeind=[]
    for index,item in df.iterrows():

        bday= item['Birthday'].strftime("%d-%m")

        if (today==bday) and yearnow not in str(item['Year']):
            sendEmail(item['Email'],"Happy Birthday",item['Dialog'],item['Name'])
            resp=sendSMS(API_Key, item['Mobile_No'], Sender, item['Dialog'])
            print(resp)
            writeind.append(index)
    for i in writeind:
        yr=df.loc[i,'Year']
        if yr is None:
           df.loc[i,'Year']= str(yearnow)

        else:
            df.loc[i,'Year'] = str(yr) + ',' + str(yearnow)


    df.to_excel('data.xlsx',index=False)

