data = open('ok.txt').read().replace('\n', '') #Finds all spaces in ok.txt and combines all into one line

lucas=open('done.txt' , 'w')
lucas.write(data) #Saves file

lucas.close() #closes file, so ur pc doesnt explode haha