#!/usr/bin/python

import sys

'''
 *
 * Copyright notice:
 * (c) Copyright 2022 RocketGate
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
from LinkBuilder import LinkBuilder

myKey = rg_config.RG_HASH_SECRET()
time = rg_config.uniqueTimeStamp()

urlStuff = LinkBuilder(myKey)

urlStuff.Set("id", time + ".PythonTest")
urlStuff.SetNumber("merch", rg_config.RG_MERCHANT_ID())
urlStuff.SetNumber("amount", 1.00)
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

urlStuff.Set("avs", "YES")
urlStuff.Set("scrub", "NO")
urlStuff.Set("time", time)

link = urlStuff.Encode()

url = rg_config.RG_LINK() + link

print('Cache-Control: no-cache')
print('Location:', url, '\n')

urlStuff.debugPrint()
