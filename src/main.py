'''
Created on Feb 25, 2010

@author: oc
'''
from DynamInt import *
def main():
    test = DynamInt(1)
    test.printme()
    b = DynamInt(2)
    b.printme()
    print "b.data "+b.data
    print "b.data "+b.data
    temp = DynamInt()
    temp = test+b
    print "Adding test to b "+temp.data
    temp = test-b
    print temp.data
    print b>test
    print b<test  
    print b == test
if __name__ == '__main__':
    main()