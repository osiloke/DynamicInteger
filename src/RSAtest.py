'''
Created on Apr 1, 2010

@author: oc
'''
from RSA import RSA, DynamInt
def main():
    print "random prime" 
    rsa = RSA(2)   
    print "Created RSA" 
    one = DynamInt(2)
    two = DynamInt(2)
    rsa.createkeys(one, two)
if __name__ == '__main__':
    main()