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

def CheckUserInput(userstring):
    PosResoonses = ('Yes','yes','Y','y','yep')
    if userstring in PosResoonses : return True
    else: return False

def Retryfunction(filename, fhand):
    retrysamefile = raw_input('\nRetry another RegEx on the same file?: ')
    if CheckUserInput(retrysamefile) : SearchInputfunction(filename,fhand)
    else : 
        retrydifffile =raw_input('\nRetry new file?')
        if CheckUserInput(retrydifffile): Openfile()
        else: 
            print 'Thank you, shutting down'
            raw_input()
            quit()


def Resultfunction(foundMatches2, inputtext, filename, fhand):                         #code to output to text file to be added later
    if foundMatches2 == []: 
        print 'No matches were found for %s in %s' % (inputtext, filename)
        Retryfunction(filename,fhand)
    else:
        print "Result: " + str(foundMatches2)
        Retryfunction(filename,fhand)

def SearchInputfunction(filename,fhand):
    print '\n\nThe file we are searching is %s' % filename
    print '\nRemember you can check your Regular Expression at https://regex101.com/#python'
    inputtext = raw_input('\n\nEnter regex search term: ')
    if inputtext == 'new file' : Openfile()
    else:    
        foundMatches2 = []
        fhand.seek(0)
        for line in fhand:
            foundMatches1 = re.findall(inputtext,line)
            if foundMatches1 == []: continue
            else:
                foundMatches2.append(foundMatches1)
        Resultfunction(foundMatches2, inputtext, filename, fhand)


def main():
    fhand = None
    Openfile()

main()
