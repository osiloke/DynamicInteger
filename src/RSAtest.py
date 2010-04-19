'''
Created on Apr 1, 2010

@author: oc
'''
from RSA import*
from DynamInt import *
def main():
    print "random prime" 
    rsa = RSA(3)   
    print "Created RSA" 
    '''
    one = DynamInt(2)
    two = DynamInt(2)
    '''
    '''rsa.gcd(one, two)'''
    m = ''
    one = DynamInt()
    rsa.decrypt(m)
    rsa.encrypt(m)
    rsa.powmod(one, one, one)
    rsa.messagetonum(m)
    rsa.getdecryptkey()
    rsa.createkeys(one, one)
    a = 533573
    b = 15
    while a>0:
                a, b = b%a, a
    print str(b)
    '''temp = rsa.randomprime()'''
    
    '''temp.printme()'''
if __name__ == '__main__':
    main()