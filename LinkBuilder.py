import base64
from encodings.base64_codec import base64_decode

import hashlib
import urllib.parse

'''
  Copyright notice:
  (c) Copyright 2022 RocketGate
  All rights reserved.
 
  The copyright notice must not be removed without specific, prior
  written permission from RocketGate.
 
  This software is protected as an unpublished work under the U.S. copyright
  laws. The above copyright notice is not intended to effect a publication of
  this work.
  This software is the confidential and proprietary information of RocketGate.
  Neither the binaries nor the source code may be redistributed without prior
  written permission from RocketGate.
 
  The software is provided "as-is" and without warranty of any kind, express, implied
  or otherwise, including without limitation, any warranty of merchantability or fitness
  for a particular purpose.  In no event shall RocketGate be liable for any direct,
  special, incidental, indirect, consequential or other damages of any kind, or any damages
  whatsoever arising out of or in connection with the use or performance of this software,
  including, without limitation, damages resulting from loss of use, data or profits, and
  whether or not advised of the possibility of damage, regardless of the theory of liability.
 
  File name: LinkBuilder.py
  Purpose: The purpose of this py file is to be an Object that can
              build a link for passing a charge request to the
              RocketGate system.  This is meant to be used in production
              or as an example of how to accomplish encoded link
              building.
 
 
'''

class LinkBuilder:
    '''
        LinkBuilder() - constructor for the class
        input: shared key string
    '''
    def __init__(self, keyString):
        self.hashKey = keyString        # secret shared key for the hash function
        self.param = dict()             # array of key value pairs
    # end constructor    
    
    '''
        Set() - set a key value pair
        input: key and value to be stored as strings
        return : nothing returned
    '''
    def Set(self, key, value):
        # remove white space from beginning and end of incoming value
        valueTrim = value.strip()
        
        # unset the array value if it exists already
        self.Clear(key)
        
        # do some checking on the 'amount' variable if it is set
        # remove the '$' if it exists
        if key.lower() == "amount":
            valueTrim = valueTrim.replace('$', '').strip()
        
        self.param[key] = valueTrim
    # end Set
    
    '''
        Set() - set a key value pair
        input: key and value to be stored as strings
        return : nothing returned
    '''
    def SetNumber(self, key, value):
        self.param[key] = str(value)
    # end Set
    
    '''
        Return the key value 
    '''
    def GetKeyValue(self, key):
        return self.param[key]
    # end GetKeyValue
    
    '''
        Clear() - used for clearing values for the array of parameters
        input : name of key to be cleared
        return : nothing returned
    '''
    def Clear(self, key):
        if key in self.param:
            self.param.pop(key)
    # end Clear
    
    '''
        Encode() - this is the function that will produce the correct link portion
                   for connecting to the Rocket Gate system
        return: string
    '''        
    def Encode(self):
        unencodedRetStr = ""; # this string will be hashed
        encodedRetStr = "";   # this string is returned
        sha1Hash = "";        # this string will hold the hash output
        b64 = "";             # this string will hold the base64 encoding of the hash
        
        for key, value in self.param.items():
            if len(unencodedRetStr) > 0:
                unencodedRetStr += "&"
                
            unencodedRetStr += key + "=" + value
            
            if len(encodedRetStr) > 0:
                encodedRetStr += "&"
                
            encodedRetStr += key + "=" + urllib.parse.quote_plus(value)
        # end for    
        
        unencodedRetStr += "&secret=" + self.hashKey;
        unencodedRetStrSign = unencodedRetStr.encode('utf-8')

        sha1Hash = hashlib.sha1(unencodedRetStrSign)
        
        b64 = base64.encodestring(sha1Hash.digest())
        encodedRetStr += "&hash=" + urllib.parse.quote_plus(b64)[:-3]

        return encodedRetStr
    # end Encode
    
    '''
        getKeys() - this function produces a string of all the keys
        return : string
    '''
    def getKeys(self):
        retStr = ""

        for key, value in self.param.items():
            retStr += "'" + key + "' "
    
        return retStr
    #end getKeys
    
    '''
        getValues() - this function produces a string of all the values
        return : string
    '''
    def getValues(self):
        retStr = ""

        for key, value in self.param.items():
            retStr += "'" + value + "' "
    
        return retStr
    # end getValues

    '''
        getEncodedKeys() - this function produces a string of all the
                          keys encoded
        return : string
    '''
    def getEncodedKeys(self):
        retStr = ""
    
        for key, value in self.param.items():
            retStr += "'" + urllib.parse.quote_plus(key) + "' "
    
        return retStr
    # end getEncodedKeys
    
    '''
        getEncodedValues() - this function produces a string of all the
                            values encoded
        return : string
    '''
    def getEncodedValues(self):
        retStr = ""
    
        for key, value in self.param.items():
            retStr += "'" + urllib.parse.quote_plus(value) + "' "

        return retStr
    # end getEncodedValues
    
    '''
        debugPrint() - this function prints all the key value pairs from
                      the perameter array
        return : string
    '''    
    def debugPrint(self):
        i = 0

        print("Array\n{")
        
        for key, value in self.param.items():
            print("\t[%s] => %s" % (key, value))
        
        print("}\n")
    # end debugPrint
#end class LinkBuilder
