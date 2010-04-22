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
        self.n=DynamInt()
        'Convenience numbers'
        self.zero=DynamInt()
        self.zero.setData("0")
        self.one=DynamInt()
        self.one.setData("1")
        self.two = DynamInt()
        self.two.setData("2")
        self.three = DynamInt()
        self.three.setData("3")
        self.base = DynamInt()
        self.base.setData("20")
    '''
    Calculating RSA Parameters4
    '''    
    def createkeys(self,p,q):
        
        while self.millerRabin(p) == False:
            'p or q is not prime, so choose another p or q'
            print "P is not prime  :  "+p.data
            p+=self.three
        while self.millerRabin(q) == False:
            print "Q is not prime  :  "+q.data
            q+=self.three
        
        #p = self.randomprime()
        #q = self.randomprime()   
         
        
        'numbers are prime so lets save the data and continue generating keys'
        self.p = p
        self.q = q
        self.n = p*q        
        self.createphi()
        print " Prime P        :   "+ p.data
        print " Prime Q        :   "+ q.data
        print " Modulus n      :   "+self.n.data
        e = DynamInt(1)
        '''
        Lets get a prime 1 < e < phi
        '''
        while not  (self.gcd(e,self.phi) == self.one):
            #e.random(len)
            e = e+self.one
            if e > self.phi: e = self.one
            #e.printme()
            #temp =self.gcd(e,self.phi)
        self.e = e
        '''
        constraint, 1 < d < phi
                    d = 1/e mod phi
        '''
        self.d = self.multiplicativeInverse(self.e, self.phi)
           
        print " encryption key :  "+ self.e.data
        print " decryption key :  "+ self.d.data
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
    def messageToNum(self,m):
        '''
        converts message to numbers
        
        @param param m: message
        @return: dynamic integer with numbers representing message
        '''
        coded=self.disguise(m)
        return coded
    def numToMessage(self,m):
        '''
        converts numbers to message
        
        @param param m: message
        @return: dynamic integer with numbers representing message
        '''
        
        text=self.guise(m)
        
        return text
    def createphi(self):
        '''
        Create phi = (p-1)(q-1)
        '''
        self.phi=(self.p-self.one)*(self.q-self.one)
    def gcd(self,a,b):
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
        t =  DynamInt()
        while not a == self.zero:
                t = a
                tr = b
                
                a, b = b%a, a
                tt = b/a
                #print tr.data +" = " + tt.data + "*"+t.data+"+"+a.data
        return b

    def isPrime(self, num):
        '''
        checks if a number is prime using the
        selected method
        for now method is millerRabin
        '''
        return self.millerRabin(num)
    def millerRabin(self, n):
        '''
        @function millerRabin
        encrypt
        by using modular exponention
        @param num  number to test for primality
        @return: True or False for primality
        '''
        isPrime = False

        if n%self.two == self.zero and n != self.two:
            return isPrime
        elif (n == self.zero or n == self.one or n == self.two or n == self.three):
            isPrime = True
            return isPrime
        else:
            p = n-self.one;
            s = self.zero;
            r = self.zero;
            
            while (p%self.two == self.zero):
            
                s+=self.zero
                p=p/self.two
            
            r = p
            #r = p/pow(2,s); //this may not work with BigInt but should
            i = self.one
            while i < s or i == s:
            
                #generate random a where 2<=a<=n-2 here
                #while >n-2 or <2 keep generating random numbers
                a = self.zero;
                while (a > (n-self.two) or a < self.two):
                    tt = DynamInt()
                    tt.random(n.size)
                    a = tt % n
                
                y = self.powmod(a, r, n)
                if not y == self.one and not y == n-self.one:
                
                    j=self.one;
                    while j < s-self.one or j == s-self.one and not y == n-self.one :
                    
                        y = (y*y)%n;
                        if (y == self.one):
                        
                            isPrime = False
                            return isPrime
                        
                        j+=self.one
                    
                    if (not y == n-self.one):
                    
                        isPrime = False;
                        return isPrime;
            isPrime = True;
            return isPrime;
    def powmod(self, a, r, n):
        return self.modularExp(a, r, n)
    def modularExp(self, a, r, n):
        '''
        function modularExp
        Calculates the modular exponentiation
        @param a,r,n
        '''
        'self.one is a dynamic integer of one, 1'
        result = self.one;

        while (r > self.zero):
        
            if not (r%self.two == self.zero):
            
                result = (result * a) % n;
            
    
            r = r/self.two;
            a = (a * a) % n;
        
        
        return result;
    def egcd(self,a, b):
        
        x, Xprev = self.zero, self.one
        y, Yprev = self.one, self.zero
     
        while (b>self.zero):
            quotient = a / b
            a, b = b, a % b
            x, Xprev = Xprev - quotient*x, x
            y, Yprev = Yprev - quotient*y, y
     
        return (Xprev, Yprev, a)
    def multiplicativeInverse(self,a, m):
        x, q, gcd = self.egcd(a, m)
     
        if gcd == self.one:
            return (x + m) % m
        else:
            return None
    '''Doing Encryption'''
    def encrypt(self, m):
        '''
        Encrypt the message using the keys created
        @param m: message
        '''
        c = self.powmod(self.messageToNum(m),self.e,self.n)
        return c
    def decrypt(self, m):
        m_ret = self.powmod(m,self.d,self.n)
        return self.reveal(m_ret)
    def disguise(self,text):
        '''
        converts message to numbers
        Accomplish this by looping through each element
        in message var and converting it int. 
        This int is added to a dynamint
        @param param m: message
        @return: dynamic integer with numbers representing message
        '''
        
        guise =self.zero 
        for i in text:
            'convert to ascii base 10'
            ascii = DynamInt()
            ascii.setData(str(ord(i)))
            guise = ascii+(guise*self.base)
        return guise
    def reveal(self,num):
        '''
        @summary: Converts from base 10 to readable string
        @param num: number to reveal by converting from base 10 to string (8 bit data) 
        '''
        g = []
        
        while num >self.zero:
            r , num = num % self.base, num / self.base
            temp = r-self.one
            g.append(string.lowercase[int(temp.data)])
        g.reverse()
        return g
    