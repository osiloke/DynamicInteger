'''
DynamInt.py

Dynamic Integer Class

This class handles storing and manipulation
of very large integers. 
It does this by storing the integer as a string.

It is essentially useful in cryptographic applications


Created on Feb 25, 2010

@author: Harold Osiloke Emoekpere
'''
import math
import random
class DynamInt:
    '''
    classdocs
    '''


    def __init__(self, num = None):
        '''
        Constructor
        '''
        self.neg = False
        if num is None:
            self.data = ''
            self.size  = 0
        else:
            self.data = ''
            self.random(num)
    '''def assign(self, str): 
        self.data = str
        self.size = len(str)'''
    ''' Arithmetic Operators '''
    def __add__(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
         
        '''
        Basically, this selects what should be added to what
        it is based on primary school addition techniques
        i.e
        to add 1234 to 12345, the code makes a configuration similar to
        
                1  2  3  4  5
                +  1  2  3  4
                -------------
                1  3  5  7  9
                -------------
        The larger number goes on top while the smaller goes below
        '''
        if (self  > num ):
            top = self.data
            bottom = num.data
        else:
            top = num.data
            bottom = self.data
        '''
        Temporary Variables used in addition process
        tempSum     ----- Stores partial subtraction
        j           ----- Stores length of bottom number
        i           ----- Stores length of top number
        sum         ----- Stores final sum string
        carryover   ----- A flag that determines if there is a carryover to the next digit
        '''
        tempSum = 0
        j = len(bottom)-1
        i = len(top)-1
        sum = ''
        carryover = 0
        while i >= 0:
            
            ''' Have we run out of bottom digits ? '''
            if (j >= 0):  
                tempSum = int(top[i])+int(bottom[j])+carryover       
                j-=1
            else:
                ''' No more bottom digits, add any leftover carryover'''
                tempSum = int(top[i])+carryover
            
            if tempSum >= 10:
                ''' do we have a remainder to carryover ? '''
                tempSum = tempSum % 10
                carryover = 1  
            else:
                carryover = 0
            ''' lets concatenate the main sum outputed '''
            sum = str(tempSum)+sum
            i-=1
        if carryover == 1: sum = str(carryover)+sum
        return sum
    def __sub__(self, num):
        '''
            Overloaded Subtraction function
            subtracts an existing DynamInt from this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        
        '''
        Uses two's compliment on each element of both numbers
        '''
        if self == num: return '0'
        if (self  > num):
            top = self.data
            bottom = num.data
        elif (num > self):
            top = num.data
            bottom = self.data
        '''
        Temporary Variables used in addition process
        tempSub     ----- Stores partial subtraction
        j           ----- Stores length of bottom number
        i           ----- Stores length of top number
        sub         ----- Stores final sub string
        borrow      ----- A flag that determines if it would need to borrow from next digit
        '''
        tempSub = 0
        j = len(bottom)-1
        i = len(top)-1
        borrow = 0
        sub = ''
        while i >= 0:
            
            ''' Have we run out of bottom digits ? '''
            if (j >= 0):  
                tempSub = (int(top[i])-int(bottom[j]))-borrow 
                if tempSub < 0: 
                    borrow = 1
                    tempSub = tempSub+10  
                else: borrow=0
                
                j-=1
            else:
                ''' No more bottom digits, subtract any leftover borrow out'''
                tempSub = int(top[i])-borrow
                if tempSub < 0: 
                    borrow = 1
                    tempSub = tempSub+10  
                else: borrow=0
            
            ''' lets concatenate the main sum outputed '''
            sub = str(tempSub)+sub
            i-=1
        if borrow == 1: sum = '-'+sub
        return sub
        
   
    def __div__(self,num):
        '''
            Overloaded == function
            Checks if this DynamInt is equal to this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
         
       
        j = 0;
        result = "";
        xString = "";
        remainderString = "";
        temp = DynamInt ()
        n= 0
        while n < len(self.data):
        
            result = result+'0'
            xString=xString+'0'
            n+=1
        m=0
        while m < len(num.data):        
            remainderString = remainderString +'0'        
    
        cur=DynamInt()
        cur.setData( (self.data[0]))
        remainder = DynamInt ()
        remainder.setData( remainderString )
    
        while j< len(self.data):
        
            x = DynamInt ()
            x.setData( xString )
            for i in range(0,len(num.data)-1):
            
                
                temp.setData(x.data)
                x.setData( x + num)
    
                if x > cur:
                
                    result = result[:j+1]+str(i)+result[j+2:]
                    break
            
            
            j+=1
            remainder.setData(cur - temp)
            if j == len(self.data):
            
                cur.setData(str(remainder))
            
            cur.setData( remainder.data + self.data[j])
        
        return result
    
    def __mod__(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        
           
        return '0'
    
    ''' 
        Logical Operations
    '''
    def __gt__(self,num):
        '''
            Overloaded > function
            Checks if this DynamInt is greater than existing DynamInt
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
         
        '''
        Performs greater than function by applying > function on each pair of integers 
        i.e
        to find which is 12345 is greater than 1234, the code makes a configuration similar to
        
                1  0  3  4  5
              >    1  2  3  4
                -------------
                T  F  T  T  T
                -------------
        Where T refers to True, F to False
        It uses the last compare value, in this case, T which means 10345 is greater than 1234
        Another example,
                 1  0  3  4  5
            >    9  2  3  4  0
                 -------------
                 F  F  T  T  T
                 -------------
        In this case it uses False, since 10345 is less than 92340
        '''
        if (self == num): return False
        if (self.size > num.size):
            return True
        elif (self.size < num.size):
            return False
        
        '''
        Temporary Variables used in addition process
        '''
        greater = False
        j = self.size-1
        i = num.size-1
        lhs  = self.data
        rhs = num.data
        while i >= 0:
            
            ''' Have we run out of bottom digits ? '''
            if (j >= 0):  
                greater = lhs[i] > rhs[i]       
                j-=1
            else:
                ''' No more bottom digits, add any leftover carryover'''
                greater = True         
           
            i-=1
        
        return greater
    
    def __lt__(self,num):
        '''
            Overloaded < function
            Checks if this DynamInt is less than existing DynamInt
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        
         
        '''
        The exact opposite of greater than above
        
                1  0  3  4  5
              <    1  2  3  4
                -------------
                F  T  F  F  F
                -------------
        Where T refers to True, F to False
        It uses the last compare value, in this case, T which means 10345 is less than 1234
        Another example,
                 1  0  3  4  5
            <    9  2  3  4  0
                 -------------
                 T  T  F  F  F
                 -------------
        In this case it uses False, since 10345 is less than 92340
        '''
        if (self == num): return False
        return not(self.__gt__(num))
    def __eq__(self,num):
        '''
            Overloaded == function
            Checks if this DynamInt is equal to this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
         
        if (self.size > num.size):
            return False
        elif (self.size < num.size):
            return False
        

        j = self.size-1
        i = num.size-1
        lhs  = self.data
        rhs = num.data
        while i >= 0:
            
            ''' Have we run out of bottom digits ? '''
            if (j >= 0):  
                compare = lhs[i] != rhs[i] 
                if compare: return False      
                j-=1
            else:
                ''' No more bottom digits, add any leftover carryover'''
                return False       
           
            i-=1
        
        return True
    def __mul__(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
        if (self > num):
            top = self.data
            bottom = num.data
        
        else:
            top = num.data
            bottom = self.data
            
        tempProduct = 0
        product = ""
        resultSize = self.size+num.size
        for n in range(0,resultSize):    
            product = "0"+product
            
        i = len(bottom)-1
        while i >= 0:
        
            carry = 0
            j = len(top) -1
            
            while j>=0: 
                k = i + j   
                tempProduct = int((int(top[j]) * int(bottom[i])) + int(product[k]) + carry)
                product = product[:k+1] + str(tempProduct % 10) + product[k+2:]
                carry = int(tempProduct/10);
                j-=1    
    
            if (carry != 0):            
                product = product[:i] + str(carry) + product[i+1:]
            i-=1
        
        return product;
    def printme(self):
        print self.data
    def random(self,length):
        
        for n in range(0,length):
            self.data = str(random.randint(0,9))+self.data
        self.size = len(self.data)
    def setData(self,stri):
        self.data=stri
        self.size = len (stri)
    def modmod(self,num,m):
        if  num > m:
            return num % m
        elif num == m:
            return 1
        else:
            return 0