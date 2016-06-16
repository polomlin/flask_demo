# -*- coding:utf8 -*-

'''
Created on Jun 16, 2016

@author: sam
'''
"""
curl -X PUT -d '{ "Ozgur Vatansever1":{"whatever1": "data1" }}' \
  'https://first-firebase-86ab8.firebaseio.com/strings/.json'

curl -X PATCH -d '{ "Ozgur Vatansever2":{"whatever2": "data2" }}' \
  'https://first-firebase-86ab8.firebaseio.com/strings/.json'

curl -X PUT -d '{ "Ozgur Vatansever3":{"whatever3": "data3" }}' \
  'https://first-firebase-86ab8.firebaseio.com/strings/.json'
"""
from firebase import firebase
import time
fb = firebase.FirebaseApplication('https://first-firebase-86ab8.firebaseio.com/', None)
new_user = 'Ozgur Vatansever'

result = fb.post('strings',  new_user+"2", data={"whatever3":"data3"}, params={'print': 'silent'})
print result

time.sleep(5)
result = fb.put('strings', new_user, data={"whatever1":"data1"}, params={'print': 'silent'})
print result

time.sleep(5)
result = fb.put('strings', new_user+"1", data={"whatever2":"data2"}, params={'print': 'silent'})
print result

time.sleep(5)
result = fb.put('strings',  new_user+"2", data={"whatever3":"data3"}, params={'print': 'silent'})
print result



