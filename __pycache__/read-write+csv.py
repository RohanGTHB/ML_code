#HOW TO READ AND WRITE TO A FILE

#f = open ('rohan.txt','r')
#print(f.name)
#f.close() #here its imp to close the file
#print(f.mode)

#opening files with context manager
#for a context manager, the file automatically gets close once we exit the block,although we would still
# have the access to the file(context) variable

with open ('rohan.txt','r') as f:
    #print(f.read())
    #fcont = f.read()
    #fcont2 =f.readlines()
    #fcont3 = f.readline #here we can use next , next(fcont) to get the next line

    #print(fcont)

    for x in f:
        print(x[0])

    #using while loop, looping in chunks
    #fcont = f.read(10) #if i dont put any(10) at the beginnig then first whole of file would be read then
    #while len(fcont) > 0:      #while loop would start and since there would be no values to iterate
    #    print(fcont,end = '*') #further,we would have * put and loop would end
    #    fcont = f.read(10)

    # f.read(100)
    #f.read(100) this means for the first command first 100 words would be returned and then for the 2 next
                   #100 would be returned , not that we will have the same 100 letters again
                   #but to do that


    #print(f.read(10))

    #f.seek(0) #this simply puts the cursor at position given in the index
    #print(f.read(10))


#print(f.closed) #since the file is closed u can access it but cant read the contents outside the block


#WRITING OF FILES
with open('roh.txt','w') as fw:
    fw.write('text')
    fw.write('sect')
    #seek #for write this is mostly used for overwriting
    fw.seek(0)
    fw.write('d')

#reading and writing both

#with open('rohan.txt','r') as fr1: #we might be writing in the read file coz for loop wont have lines to read
#    with open('rohan_copy.txt','w') as fw1: #in that case
#        for line in fr1:
#            fw1.write(line)

#-------------------------------------------------------------------------------------------------------->

#READING AND WRITING TO A CSV FILE

import csv #split can also be used but csv module makes parsing of files easier

with open('names.csv','r') as csv1:
    csv_read = csv.reader(csv1) #reader is a method that understands the csv files and iterates through the lines

    print(csv_read) #this is just an object in the memory

    next(csv_read) #lets you skip the first line coz we returned it here but did not print it.

    for line in csv_read:       #csv files should be seperated by comma's
        print(line[0:2])

#writing to files
#with open('names.csv','r') as csv1: #if i dont indent the write file in read file it will show me error
#    csv_read = csv.reader(csv1) # as i/o operation on closed file coz that would be out of scope of read file
#    with open('names_w.csv','w') as csv_w:
#        csv_write = csv.writer(csv_w,delimiter ='*')

#        for line in csv_read:
#            csv_write.writerow(line)


#reading/writitng csv using dictionary

#reader
with open('names.csv','r') as csv1:
    csv_read = csv.DictReader(csv1)

    for line in csv_read:
        print(line['email']) #more convieneient to parse out the info.

#writer

with open('names.csv','r') as csv1: #if i dont indent the write file in read file it will show me error
    csv_read = csv.DictReader(csv1) # as i/o operation on closed file coz that would be out of scope of read file


    with open('names_wd.csv','w') as csv_w:
        fiel_name = ['first_name','last_name'] #these field names should be same as headers passed in read file
        csv_write = csv.DictWriter(csv_w,fieldnames= fiel_name)

        csv_write.writeheader() #this is to print the headers(fieldnames) already passed in

        for line in csv_read:
            del line['email'] #this allows us to remove specified result in our write query
            csv_write.writerow(line)


#-------------------------------------------------------------------------------------------------------->
