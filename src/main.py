'''
Created on Feb 25, 2010

@author: oc
'''
from DynamInt import *
def main():
    test = DynamInt('8')
    b = DynamInt('5')
    print "Adding test to b "+(test+b)
    print (test-b)
    print b>test
    print b<test
    print b == test
if __name__ == '__main__':
    main() 
