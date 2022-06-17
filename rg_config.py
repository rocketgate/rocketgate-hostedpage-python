'''
Created on Apr 18, 2019
Revised on June 17, 2022

Language: Python

@author: cdltorre
'''
import time
import math

# MERCHANT TODO: Configure these key variables.

def RG_MERCHANT_URL():
    return 'http://example.com/index.html'
    
def RG_MERCHANT_LOGIN_URL():
    return 'http://example.com/login/'
    
def RG_MERCHANT_ID():
    return 1

def RG_GW_PASSWORD():
    return 'CHANGETHISVALUE'

def RG_HASH_SECRET():
    return 'hashsecret'

'''
Salt used for protecting password, don't change after install or you will have different salts used on passwords in the database.
Modify this to your own value
'''

def RG_MERCHANT_PASSWORD_SALT():
    return 'CHANGETHISVALUE'

# Local Database Configs

def RG_DB_SERVER():
    return 'localhost'

def RG_DB_NAME():
    return 'demo'

def RG_DB_USERNAME():
    return 'rg_demouser'

def RG_DB_PASSWORD():
    return '3mpGsdfljsfjslf2r8'

# Set to FALSE for production, TRUE for Testing/Dev.
def RG_TEST_MODE():
    return True

if RG_TEST_MODE():
    def RG_LINK():
        return 'https://dev-secure.rocketgate.com/hostedpage/servlet/HostedPagePurchase?'
else:
    def RG_LINK():
        return 'https://secure.rocketgate.com/hostedpage/servlet/HostedPagePurchase?'


'''

RocketGate requires a response to this postback.  
This function provides a properly formatted response message.

'results' indicates success or failure. A value of 0 indicates the server has received, parsed and processed the postback. A non-zero value indicates that an error occurred.
'message' is an optional value that could be used to pass an error description which can be used in debugging the error.

'''
def postback_response(results, message):
    print("Content-Type: text/xml")
    print("Cache-Control: no-cache")
    
    retStr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    retStr += "<Response>"
    retStr += "<results>" + results + "</results>"

    if (message != ''):
        retStr += "<message>" + message + "</message>"

    retStr += "</Response>\n"

    return retStr;             # Send to RocketGate
# end postback_response

'''
Use Timestamp for Customer ID Generators
'''
def uniqueTimeStamp():
    milliseconds = microtime()
    timestring = milliseconds.split(" ")
    sg = timestring[1]
    mlsg = (timestring[0])[2:6]
    
    timestamp = sg + mlsg
  
    return timestamp
# end uniqueTimeStamp

'''
Return current Unix timestamp with microseconds
'''
def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())
# end microtime
