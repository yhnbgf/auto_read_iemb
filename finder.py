with open('done.txt', 'r') as file:
        text1 = file.read()  #reads done.txt
read=text1.find('unread message  end') #"ctrl f" for unread message end in done.txt , to remove all read already messages
afterread = text1[read:] 

with open('done.txt', 'w') as file:
       filewrite=text1.replace(afterread,'')
       file.write(filewrite)  #deletes everything after unread message end


with open('final.txt', 'w') as file:  #Clears final.txt as i use append later on
    file.write("")

unread_number=int(input("How many unread messages do u have?")) #Prompts user for unread messages, to loop through number of times to find iemb "message number"
for i in range (unread_number):  #for number of messages u want to read
    
    with open('done.txt', 'r') as file:
        text = file.read()      #opens done.txt
    index = text.find('/Board/content/') + 13  #finds "/board/content", damn smart method, to get the message number after
    title = text[index:] #copies all text after board/content
    chin = title[0:8] #but only saves first 8, leave 2 here because i want to prevent my computer from ctrl f the same thing
    last= (title[2:8]) #saves 2nd to 8th number, 
    last_final= last.replace('?', '') #removes funny ? 
    write_last=last.replace(" ","")    #removes spaces 
    print(last_final) #prints the message number
    
    with open ('final.txt','a') as file:
        file.write(last_final)        #puts the message number into final.txt
        file.write("\n")
    with open('done.txt', 'w') as file:
       data= text.replace(chin,'')
       file.write(data)      # am so proud of myself, remove the last from content to become 'conten', so computer wont control f the same thing
