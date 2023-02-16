import time
with open('cookies.txt', 'r') as file:
        space_read = file.read()  #opens cookie file
    
with open('cookies.txt', 'w') as file:
    spaces=space_read.replace(" ", "")
    file.write(spaces)    #combines all the spaces in the file into no space lol, so can sort cookie easily



with open('cookies.txt', 'r') as file:
        text = file.read()
index = text.find('value') + 4  #same technique as finder.py, incredibly genius im so hapy wow
title = text[index:] 
chin = title[0:41]
auth_token= (title[4:40]) # using this to find previous auth token when using selenium



with open('cookies.txt', 'w') as file: 
    data= text.replace(chin,'') #removes e from value, so cannot ctrl f the same string after value again
    file.write(data)


with open('cookies.txt', 'r') as file:
        text1 = file.read()
index1 = text1.find('value') + 4
title1 = text1[index1:]   #same as for auth token
chin1 = title1[0:29]
sessionid= (title1[4:28])   #gets session id from just now selenium


with open('cookies.txt', 'w') as file:
    data1= text1.replace(chin1,'')
    file.write(data1) #also emoves e from value, so cannot ctrl f the same string after value again



with open('cookies.txt', 'r') as file:
        text2 = file.read()
index2 = text2.find('value') + 4
title2 = text2[index2:] 
chin2 = title2[0:150]   #same as for above
verif_token= (title2[4:112]) #save verif token
redo=int(input("How many reads u want:")) #using number of reads as a loop, to not waste time and program
board="1048" #noob student board number haiz.. sad
import requests # this request part is cool, if u read this, check out curlconverter.com


for i in range(redo):
        f = open('final.txt')  #opens message number file
        first = str(f.readline()) #reads message number of first line
        first1 = first.rstrip() #removes dead space from message number, eg. the space after the str
         #was stuck here for a while, but realised THERE WAS DEAD SPACE, SO I CLDNT USE IT AS A VARIABLE FOR JSON

        cookies = {
            '__RequestVerificationToken': verif_token,  #Normal json stuff
            'ASP.NET_SessionId': sessionid ,
            'AuthenticationToken': auth_token , 
        }

        headers = {
            'Host': 'iemb.hci.edu.sg',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://iemb.hci.edu.sg',
            'Referer': 'https://iemb.hci.edu.sg/Board/Detail/1048',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin', #this sec-fetch site is cringe. cant directly make post request, must do this cringe way, annoying it department
            'Connection': '102926',  
            #default headers
    
        }

        data = {
            'boardId': board,
            'topicIDs': first1, #finds the message number
        }

        response = requests.post('https://iemb.hci.edu.sg/Board/MarkReadMessage', cookies=cookies, headers=headers, data=data, verify=False) #sends post request to iemb server to mark as read
        time.sleep(3) #delay for lag, and iemb wont think im bot
        with open("final.txt", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:]) #delets first line, to allow loop to next line, wow im genius thanks everybody
        
   


        
        