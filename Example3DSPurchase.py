#!/usr/bin/python

import sys

'''
 *
 * Copyright notice:
 * (c) Copyright 2018 RocketGate
 * All rights reserved.
 *
 * The copyright notice must not be removed without specific, prior
 * written permission from RocketGate.
 *
 * This software is protected as an unpublished work under the U.S. copyright
 * laws. The above copyright notice is not intended to effect a publication of
 * this work.
 * This software is the confidential and proprietary information of RocketGate.
 * Neither the binaries nor the source code may be redistributed without prior
 * written permission from RocketGate.
 *
 * The software is provided "as-is" and without warranty of any kind, express, implied
 * or otherwise, including without limitation, any warranty of merchantability or fitness
 * for a particular purpose.  In no event shall RocketGate be liable for any direct,
 * special, incidental, indirect, consequential or other damages of any kind, or any damages
 * whatsoever arising out of or in connection with the use or performance of this software,
 * including, without limitation, damages resulting from loss of use, data or profits, and
 * whether or not advised of the possibility of damage, regardless of the theory of liability.
 *
 * Purpose: This page uses the LinkBuilder util to build links to RG join pages
 *             
 *
'''

import rg_config
from rg_config import RG_MERCHANT_URL
from rg_config import RG_MERCHANT_LOGIN_URL
from rg_config import RG_MERCHANT_ID
from rg_config import RG_GW_PASSWORD
from rg_config import RG_HASH_SECRET
from rg_config import RG_MERCHANT_PASSWORD_SALT
from rg_config import RG_DB_SERVER
from rg_config import RG_DB_NAME
from rg_config import RG_DB_USERNAME
from rg_config import RG_DB_PASSWORD

import LinkBuilder
from LinkBuilder import *

myKey = "hashsecret"
time = rg_config.uniqueTimeStamp()

urlStuff = LinkBuilder(myKey)

urlStuff.Set("id", time + ".PythonTest")
urlStuff.SetNumber("merch", "1")
urlStuff.SetNumber("amount", 1.05)
urlStuff.Set("invoice", time + ".SaleTest")

urlStuff.Set("purchase", "TRUE")
urlStuff.Set("method", "CC")

urlStuff.Set("fname", "Joe")
urlStuff.Set("lname", "Ortiz")
urlStuff.Set("address", "123 Main St")
urlStuff.Set("city", "Las Vegas")
urlStuff.Set("state", "NV")
urlStuff.Set("zip", "89141")
urlStuff.Set("country", "US")
urlStuff.Set("currency", "USD")
urlStuff.Set("3DS", "true")

str = urlStuff.Encode()

link = rg_config.RG_LINK() + str

print('Cache-Control: no-cache')
print('Location:', link, '\n')

urlStuff.debugPrint()

