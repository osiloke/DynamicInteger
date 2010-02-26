'''
Created on Feb 25, 2010

@author: oc
'''
from DynamInt import *
def main():
    test = DynamInt()
    b = DynamInt()
    test.set(str(2**1024))
    b.set(str(2**1024))
    '''test.printme()'''
    print "Adding test to b "+(test+b)
    print b>test
    print b<test
if __name__ == '__main__':
    main() 
