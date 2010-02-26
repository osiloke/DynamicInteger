'''
DynamInt.py

Dynamic Integer Class

This class handles storing and manipulation
of very large integers. 
It does this by storing the integer as a string.

It is essentially useful in cryptographic applications


Created on Feb 25, 2010

@author: Osiloke Harold Emoekpere
'''
class DynamInt:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.data = ''
    def set(self, str): 
        self.data = str
    
    ''' Arithmetic Operators '''
    def __add__(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
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
        if (len(self.data) > len(num.data)):
            top = self.data
            bottom = num.data
        else:
            top = num.data
            bottom = self.data
        '''
        Temporary Variables used in addition process
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
        
        return sum
    def __sub__(self, num):
        '''
            Overloaded minus function
            subtracts an existing DynamInt from this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
        
        '''
        Uses two's compliment on each element of both numbers
        '''
    def __mul__(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
        return '1'
    def __div__(self,num):
        '''
            Overloaded == function
            Checks if this DynamInt is equal to this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
        return '0'
    def mod(self, num):
        '''
            Overloaded add function
            Adds an existing DynamInt to this one
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
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
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
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
        if (len(self.data) > len(num.data)):
            return True
        elif (len(self.data) < len(num.data)):
            return False
        
        '''
        Temporary Variables used in addition process
        '''
        greater = False
        j = len(self.data)-1
        i = len(num.data)-1
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
        
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
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
        if (len(self.data) == len(num.data)): return False
        return not(self.__gt__(num))
    def __eq__(self,num):
        '''
            Overloaded == function
            Checks if this DynamInt is equal to this one
            
            @param  num reference to an existing DynamInt
            @return added DynamInt
        ''' 
        if not isinstance(num, DynamInt):
            raise TypeError, "num must be a DynamInt instance"
        return '0'
    
    def printme(self):
        print data
    def modmod(self,num,m):
        if  num > m:
            return num % m
        elif num == m:
            return 1
        else:
            return 0
            