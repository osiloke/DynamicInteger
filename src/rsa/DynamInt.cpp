#include "DynamInt.hpp"

/**
DynamInt.py

Dynamic Integer Class

This class handles storing and manipulation
of very large integers. 
It does this by storing the integer as a string.

It is essentially useful in cryptographic applications


Created on Feb 25, 2010

@author: Harold Osiloke Emoekpere, Kermen Deol

*/

namespace __DynamInt__ {

str *const_0, *const_1, *const_2;

str *__name__;


/**
class DynamInt
*/

class_ *cl_DynamInt;

str *DynamInt::__mod__(DynamInt *num) {
    /**
    Overloaded add function
    Adds an existing DynamInt to this one
    @param  num reference to an existing DynamInt
    @return added DynamInt
    */
    
    return const_0;
}

void *DynamInt::random(lambda1 length) {
    int n;

    n = 0;

    while (__lt(n, ((int )(length)))) {
        this->data = __str((__str(__random__::randint(0, 9)))->__add__(this->data));
        n = (n+1);
    }
    this->size = len(this->data);
    return NULL;
}

DynamInt *DynamInt::__add__(int num) {
    /**
    Overloaded add function
    Adds an existing DynamInt to this one
    @param  num reference to an existing DynamInt
    @return added DynamInt
    */
    str *bottom, *sum, *top;
    int carryover, i, j, tempSum;
    DynamInt *ret_val;

    /**
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
    */
    if (__gt(this, ((DynamInt *)(num)))) {
        top = this->data;
        bottom = ((str *)(num->data));
    }
    else {
        top = ((str *)(num->data));
        bottom = this->data;
    }
    /**
    Temporary Variables used in addition process
    tempSum     ----- Stores partial subtraction
    j           ----- Stores length of bottom number
    i           ----- Stores length of top number
    sum         ----- Stores final sum string
    carryover   ----- A flag that determines if there is a carryover to the next digit
    */
    tempSum = 0;
    j = (len(bottom)-1);
    i = (len(top)-1);
    sum = const_1;
    carryover = 0;

    while ((i>=0)) {
        /**
         Have we run out of bottom digits ? 
        */
        if ((j>=0)) {
            tempSum = ((__int(top->__getitem__(i))+__int(bottom->__getitem__(j)))+carryover);
            j = (j-1);
        }
        else {
            /**
             No more bottom digits, add any leftover carryover
            */
            tempSum = (__int(top->__getitem__(i))+carryover);
        }
        if ((tempSum>=10)) {
            /**
             do we have a remainder to carryover ? 
            */
            tempSum = __mods(tempSum, 10);
            carryover = 1;
        }
        else {
            carryover = 0;
        }
        /**
         lets concatenate the main sum outputed 
        */
        sum = (__str(tempSum))->__add__(sum);
        i = (i-1);
    }
    if ((carryover==1)) {
        sum = (__str(carryover))->__add__(sum);
    }
    ret_val = (new DynamInt(((lambda0 )(0))));
    ret_val->setData(sum);
    return ret_val;
}

__ss_bool DynamInt::__gt__(DynamInt *num) {
    /**
    Overloaded > function
    Checks if this DynamInt is greater than existing DynamInt
    
    @param  num reference to an existing DynamInt
    @return added DynamInt
    */
    str *lhs, *rhs;
    __ss_bool greater;
    int i, j;

    /**
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
    */
    if (__eq(this, num)) {
        return False;
    }
    if ((this->size>num->size)) {
        return True;
    }
    else if ((this->size<num->size)) {
        return False;
    }
    /**
    Temporary Variables used in addition process
    */
    greater = False;
    j = (this->size-1);
    i = (num->size-1);
    lhs = this->data;
    rhs = num->data;

    while ((i>=0)) {
        /**
         Have we run out of bottom digits ? 
        */
        if ((j>=0)) {
            greater = ___bool(__gt(lhs->__getitem__(i), rhs->__getitem__(i)));
            j = (j-1);
        }
        else {
            /**
             No more bottom digits, add any leftover carryover
            */
            greater = True;
        }
        i = (i-1);
    }
    return greater;
}

DynamInt *DynamInt::__sub__(DynamInt *num) {
    /**
    Overloaded Subtraction function
    subtracts an existing DynamInt from this one
    
    @param  num reference to an existing DynamInt
    @return added DynamInt
    */
    str *bottom, *sub, *sum, *top;
    int borrow, i, j, tempSub;
    DynamInt *ret_val, *temp;

    /**
    Uses two's compliment on each element of both numbers
    */
    temp = (new DynamInt(((lambda0 )(0))));
    temp->setData(const_0);
    if (__eq(this, num)) {
        return temp;
    }
    if (__gt(this, num)) {
        top = this->data;
        bottom = num->data;
    }
    else if (__gt(num, this)) {
        top = num->data;
        bottom = this->data;
    }
    /**
    Temporary Variables used in addition process
    tempSub     ----- Stores partial subtraction
    j           ----- Stores length of bottom number
    i           ----- Stores length of top number
    sub         ----- Stores final sub string
    borrow      ----- A flag that determines if it would need to borrow from next digit
    */
    tempSub = 0;
    j = (len(bottom)-1);
    i = (len(top)-1);
    borrow = 0;
    sub = const_1;

    while ((i>=0)) {
        /**
         Have we run out of bottom digits ? 
        */
        if ((j>=0)) {
            tempSub = ((__int(top->__getitem__(i))-__int(bottom->__getitem__(j)))-borrow);
            if ((tempSub<0)) {
                borrow = 1;
                tempSub = (tempSub+10);
            }
            else {
                borrow = 0;
            }
            j = (j-1);
        }
        else {
            /**
             No more bottom digits, subtract any leftover borrow out
            */
            tempSub = (__int(top->__getitem__(i))-borrow);
            if ((tempSub<0)) {
                borrow = 1;
                tempSub = (tempSub+10);
            }
            else {
                borrow = 0;
            }
        }
        /**
         lets concatenate the main sum outputed 
        */
        sub = (__str(tempSub))->__add__(sub);
        i = (i-1);
    }
    if ((borrow==1)) {
        sum = (const_2)->__add__(sub);
    }
    ret_val = (new DynamInt(((lambda0 )(0))));
    ret_val->setData(sub);
    return ret_val;
}

__ss_bool DynamInt::__eq__(DynamInt *num) {
    /**
    Overloaded == function
    Checks if this DynamInt is equal to this one
    
    @param  num reference to an existing DynamInt
    @return added DynamInt
    */
    str *lhs, *rhs;
    __ss_bool compare;
    int i, j;

    if ((this->size>num->size)) {
        return False;
    }
    else if ((this->size<num->size)) {
        return False;
    }
    j = (this->size-1);
    i = (num->size-1);
    lhs = this->data;
    rhs = num->data;

    while ((i>=0)) {
        /**
         Have we run out of bottom digits ? 
        */
        if ((j>=0)) {
            compare = ___bool(__ne(lhs->__getitem__(i), rhs->__getitem__(i)));
            if (compare) {
                return False;
            }
            j = (j-1);
        }
        else {
            /**
             No more bottom digits, add any leftover carryover
            */
            return False;
        }
        i = (i-1);
    }
    return True;
}

void *DynamInt::__init__(lambda0 num) {
    /**
    Constructor
    */
    
    this->neg = False;
    if ((num==NULL)) {
        this->data = const_1;
        this->size = 0;
    }
    else {
        this->data = const_1;
        this->random(num);
    }
    return NULL;
}

void *DynamInt::setData(str *stri) {
    
    this->data = stri;
    this->size = len(stri);
    return NULL;
}

void __init() {
    const_0 = new str("0");
    const_1 = new str("");
    const_2 = new str("-");

    __name__ = new str("DynamInt");

    cl_DynamInt = new class_("DynamInt", 3, 3);
}

} // module namespace

