#python regex searcher, for m-box.txt
import re

def Openfile():
    filename = raw_input('Enter filename:')                                        
    if len(filename) < 2:
        fhand = open('C:\\users\\902618\\documents\\python\\homework\\text\\mbox-short.txt')
    else :
        Openfile()                                                                      #code to make it more flexibe, to be added later
    print 'If you need a new file, enter \"new file\" when asked for a regex searh term'
    #ftext = fhand.read()
    SearchInputfunction(filename, fhand)
    
def SearchInputfunction(filename, fhand):
    print '\n\nThe file we are searching is %s' % filename
    inputtext = raw_input('\n\nEnter regex search term: ')
    #print '\n\nWe are searching for %s in %s, located at %s' % (inputstring,filename,fhand)
    i = 0
    for line in fhand:
        if i <20:
            #print line
            wordlist = line.split(" ")
            print wordlist
            i +=1
        else: break
        #print line
        #inputwordlist = line.split()
        #print inputwordlist
        #delimiter = " "
        #teststring = delimiter.join(inputwordlist)
        #print teststring
        # foundRegex = re.search(inputtext,teststring)
        # if foundRegex != None:
            # foundRegex = re.findall(inputtext,teststring)
            # print "Result: " + str(foundRegex)
        # else: 
            # print '\n\nteststring\n\ninputtext'
            # print "Search did not have any results."
            
def main():
    fhand = None
    Openfile()

main()