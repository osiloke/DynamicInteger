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
        'Convenience numbers'
        self.zero=DynamInt()
        self.zero.setData("0")
        self.one=DynamInt()
        self.one.setData("1")
        self.two = DynamInt()
        self.two.setData("2")
        self.three = DynamInt()
        self.three.setData("3")
    '''
    Calculating RSA Parameters4
    '''    
    def createkeys(self,p,q):
        '''
        while self.millerRabin(p) == False or self.millerRabin(q) == False:
            'p or q is not prime, so choose another p or q'
            print "P or Q is not prime!"
            p+=self.one
            q+=self.one
        '''
        #p = self.randomprime()
        #q = self.randomprime()   
        p.setData("821089628001493")
        q.setData("1872967539195764008553239")    
        print "Found Primes"
        print "p = "
        p.printme()
        print "q = "
        q.printme()
        'numbers are prime so lets save the data and continue generating keys'
        self.p = p
        self.q = q
        self.n = p*q        
        self.createphi()
        print " n "+self.n.data
        'generate a random encrypt key of length len'
        print "creating e"
        e = DynamInt(self.len)
        e.setData("197")
        temp = self.gcd(e,self.phi)
        while not  (temp == self.one):
            #e.random(len)
            e = e+self.one
            #e.printme()
            temp =self.gcd(e,self.phi)
        self.e = e
        self.d = self.multiplicativeInverse(self.e, self.phi)
        print " e "
        e.printme()
        print " d "
        self.d.printme()
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
                print tr.data +" = " + tt.data + "*"+t.data+"+"+a.data
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
            
                s=s+self.zero
                p=p/self.two
            
            r = p
            #r = p/pow(2,s); //this may not work with BigInt but should
            i = self.one
            while i < s or i == s:
            
                #generate random a where 2<=a<=n-2 here
                #while >n-2 or <2 keep generating random numbers
                a = self.zero;
                while (a > (n-2) or a < 2):
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
        result = self.one;

        while (r > self.zero):
        
            if (r & 1):
            
                result = (result * a) % n;
            
    
            r = r >> self.one;
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
        c = self.powmod(self.messagetonum(m),self.e,self.n)
        return m
    def decrypt(self, m):
        m_ret = self.powmod(self.messagetonum(m),self.d,self.n)
        return m_ret
    def disguise(self,text):
        '''
        converts message to numbers
        Accomplish this by looping through each element
        in message var and converting it int. 
        This int is added to a dynamint
        @param param m: message
        @return: dynamic integer with numbers representing message
        '''
        
        guise =0 
        for i in text:
            'convert to ascii base 10'
            guise = ord(i)+guise*10
        return guise
    def reveal(self,num):
        g = []
        while num >0:
            r , num = num % 10, num / 10
            temp = r-self.one
            g.append(string.lowercase[int(temp.data)])
        g.reverse()
    