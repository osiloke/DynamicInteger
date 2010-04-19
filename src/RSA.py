'''
Created on Mar 31, 2010

@author: oc
'''
from DynamInt import *
class RSA(object):
    '''
    classdocs
    '''


    def __init__(self, len):
        '''
        Constructor
        '''
        'number of bits for number'
        if len:
            self.len=len
        else:
            self.len=0; 
        'Initialization'
        self.p = DynamInt()
        self.q = DynamInt()
        self.d = DynamInt()
        self.e = DynamInt()
        self.phi=DynamInt()
        'Convineince numbers'
        self.zero=DynamInt()
        self.zero.data = "0"
        self.one=DynamInt()
        self.one.data = "1"
    '''
    Calculating RSA Parameters4
    '''    
    def createkeys(self,p,q):
        'check of we can p and q are prime'
        if self.millerRabin(p) == False or self.millerRabin(q) == False:
            'p or q is not prime, so choose another p or q'
            print "P or Q is not prime!"
            return False 
        'numbers are prime so lets save the data and continue generating keys'
        self.p = p
        self.q = q
        self.n = p*q        
        self.phi = self.createphi()
        'generate a random encrypt key of length len'
        e = DynamInt(len)
        while DynamInt(self.gcd(e,self.phi))> self.one:
            e.random(len)
        self.e = e
        return True
    def randomprime(self):
        '''
        randomprime
        generates a random prime by looping
        and testing each random number it creates
        '''
        print "Initial Prime"
        prime =  DynamInt(len)
        
        prime.printme()
        while self.isPrime(prime)!=True :
            print "Current Number "+prime.data          
            prime.random(len)
        return prime
    def getdecryptkey(self):
        self.d = self.extendedEuclid(self.phi, self.e)
        return False
    def messagetonum(self,m):
        '''
        converts message to numbers
        Accomplish this by looping through each element
        in message var and converting it int. 
        This int is added to a dynamint
        @param param m: message
        @return: dynamic integer with numbers representing message
        '''
        temp = DynamInt(len(m))
        for char in m:
            temp=temp+ord(char)
    def createphi(self):
        '''
        Create phi = (p-1)(q-1)
        '''
        self.phi=(self.p-self.one)*(self.q-self.one)
    def gcd(self, a, b):
        '''
        find the gcd between two numbers
        Uses the fact that 
        b = b%a*k + r next iteration b = r a = k, r = r%k*k2 + r2 
        example a = 10 b = 20
        on first loop
        while 10
            a = 20%10 = 0
            b = 10    
        hence returns 10    
        @param a, b for example e and phi
        '''

        while a>self.one:
                a, b = b%a, a
        
        
        return b
    def isPrime(self, num):
        '''
        checks if a number is prime using the
        selected method
        for now method is millerRabin
        '''
        return self.millerRabin(num)
    def millerRabin(self, num):
        '''
        @function millerRabin
        compute decryption key
        by using modular exponention
        @param num  number to test for primality
        @return: True or False for primality
        '''
        n = 0
        n = num
        return True
    def extendedEuclid(self, A, B):
        '''
        @function extendedEuclid
        finding the greatest common divisor 
        @param A, B, x, y 
        '''
        temp = DynamInt()

        return temp
    def powmod(self, a, r, n):
        return self.modularExp(a, r, n)
    def modularExp(self, a, r, n):
        '''
        function modularExp
        Calculates the modular exponentiation
        @param a,r,n
        '''
        return DynamInt()
    '''Doing Encryption'''
    def encrypt(self, m):
        '''
        Encrypt the message using the keys created
        @param m: message
        '''
        c = DynamInt()
        c = self.powmod(self.messagetonum(m),self.e,self.n)
        return m
    def decrypt(self, m):
        m_ret = DynamInt()
        m_ret = self.powmod(self.messagetonum(m),self.d,self.n)
        return m_ret