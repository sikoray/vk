# -*- encoding: utf-8 -*-

import vk
import time
import datetime
import re


session = vk.AuthSession(access_token='e00703792743bd5c2db6f98bf911c08f2b23ce80042e0d022f920a13bc5ba14bd265f2113f2d64528fdc9')
vkapi = vk.API(session)


iduser=input('Enter your id: ')
friends=vkapi.friends.get(user_id='%s' %(iduser))
FileFriends=open('friends.txt','w+')
FileFriends.write(str(friends))
FileFriends.close()




nowDate=datetime.date.today()
sendDate=input('When sending: ')
#friends=vkapi.users.get(fields='bdate')

now=(str(nowDate))
now=now.replace('-','')

friendList=[55650611,16442881,231318830,10415747,21449646,27287131,5729931]  

giftLink1=input('Enter links to gift#1: ')
giftLink2=input('Enter links to gift#2: ')
giftLink3=input('Enter links to gift#3: ')
allGift=giftLink1,giftLink2,giftLink3
FileGifts=open('gifts.txt','w+')
FileGifts.write(str(allGift))

text=('sorry..')
text1=('!')

if now == sendDate:
    for i in friendList:
        f=(str(i))        
        print (i)
        text=text+text1
        print (text)
        try:
            friends=vkapi.messages.send (user_id=i,message=text)
            time.sleep(20)        
        except vk.exceptions.VkAPIError:
            print ('ERROR SENDING')
if now != sendDate:
	print ('im sleep')
	 

#FileFriends=open('friends.txt','r')
#FileFriends.read()


FileGifts.close()
print ('WishList send')
