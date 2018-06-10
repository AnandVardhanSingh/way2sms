import requests
import sys
print('connecting...')

# init
username = 'a valid 10 digit phone number'
password = 'a validassword'
message = 'some text message'
number = 'a valid 10 digit phone number'

# session
session = requests.session()

# try to get homepage to chack connectivity
s = session.get('http://www.way2sms.com/content/index.html?')

if s.status_code is 200:
    print('connect ok, logging in...')
else:
    print('connect error, exit')
    sys.exit(0)

# login form
s = session.post('http://www.way2sms.com/Login1.action',

                 {'username': username, 'password': password})


# get JSESSION from url This is used in post request to send message...
try:
    JSESSION = (s.url.split('jsessionid=')[1].split('?')[0])
except:
    print('error logging in, exiting...')
    sys.exit(0)

# check if we are exceeding the daily sms limit, exit if greater than 100
print('checking daily sms limit...')
url = str('http://www.way2sms.com/sentSMS?Token='+JSESSION)

s = session.get(url, cookies=s.cookies)
sc = s.text.split('Sent SMS (')[1].split(')')[0]

if int(sc) > 100:
    print('daily limit reached, exit...')
    sys.exit(0)

# send sms
session.post('http://www.way2sms.com/smstoss.action', {
    'ssaction': 'ss',
    'Token': JSESSION,
    'mobile': number,
    'message': message,
    'msgLen': '135'
})
