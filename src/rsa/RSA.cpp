#include "RSA.hpp"

/**
Created on Mar 31, 2010

@author: oc
*/

namespace __RSA__ {

str *const_0, *const_1, *const_2;

str *__name__;


/**
class RSA
*/

class_ *cl_RSA;

DynamInt *RSA::powmod(DynamInt *a, DynamInt *r, DynamInt *n) {
    
    return this->modularExp(a, r, n);
}

void *RSA::messagetonum(str *m) {
    /**
    converts message to numbers
    Accomplish this by looping through each element
    in message var and converting it int. 
    This int is added to a dynamint
    @param param m: message
    @return: dynamic integer with numbers representing message
    */
    __iter<str *> *__3;
    str *__2, *__ss_char;
    int __4;
    DynamInt *temp;

    temp = (new DynamInt(len(m)));

    FOR_IN(__ss_char,m,3)
        temp = temp->__add__(ord(__ss_char));
    END_FOR

    return NULL;
}

__ss_bool RSA::millerRabin(DynamInt *num) {
    /**
    @function millerRabin
    compute decryption key
    by using modular exponention
    @param num  number to test for primality
    @return: True or False for primality
    */
    DynamInt *n;

    n = 0;
    n = num;
    return True;
}

DynamInt *RSA::gcd(DynamInt *a, DynamInt *b) {
    /**
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
    */
	DynamInt *__5;
    DynamInt *__6;


    while (__gt(a, this->one)) {
        __5 = b->__mod__(a);
        __6 = a;
        a = __5;
        b = __6;
    }
    return b;
}

DynamInt *RSA::decrypt(str *m) {
    DynamInt *m_ret;

    m_ret = (new DynamInt(((lambda0 )(0))));
    m_ret = ((DynamInt *)(this->powmod(((DynamInt *)(this->messagetonum(m))), this->d, ((DynamInt *)(this->n)))));
    return m_ret;
}

DynamInt *RSA::modularExp(DynamInt *a, DynamInt *r, DynamInt *n) {
    /**
    function modularExp
    Calculates the modular exponentiation
    @param a,r,n
    */
    
    return (new DynamInt(((lambda0 )(0))));
}

__ss_bool RSA::getdecryptkey() {
    
    this->d = this->extendedEuclid(this->phi, this->e);
    return False;
}

str *RSA::encrypt(str *m) {
    /**
    Encrypt the message using the keys created
    @param m: message
    */
    DynamInt *c;

    c = (new DynamInt(((lambda0 )(0))));
    c = ((DynamInt *)(this->powmod(((DynamInt *)(this->messagetonum(m))), this->e, ((DynamInt *)(this->n)))));
    return c;
}

__ss_bool RSA::createkeys(DynamInt *p, DynamInt *q) {
    /**
    check of we can p and q are prime
    */
    __ss_bool __0, __1;
    DynamInt *e;

    if (((this->millerRabin(p)==False) or (this->millerRabin(q)==False))) {
        /**
        p or q is not prime, so choose another p or q
        */
        print(1, const_0);
        return False;
    }
    /**
    numbers are prime so lets save the data and continue generating keys
    */
    this->p = p;
    this->q = q;
    this->n = p->__mul__(q);
    this->phi = ((DynamInt *)(this->createphi()));
    /**
    generate a random encrypt key of length len
    */
    e = (new DynamInt(((lambda0 )(__lambda0__))));

    while (__gt((new DynamInt(this->gcd(e, this->phi))), this->one)) {
        e->random(((lambda1 )(__lambda1__)));
    }
    this->e = e;
    return True;
}

void *RSA::createphi() {
    /**
    Create phi = (p-1)(q-1)
    */
    
    this->phi = ((DynamInt *)(((this->p)->__sub__(this->one))->__mul__((this->q)->__sub__(this->one))));
    return NULL;
}

void *RSA::__init__(int len) {
    /**
    Constructor
    */
    
    /**
    number of bits for number
    */
    if (len) {
        this->len = len;
    }
    else {
        this->len = 0;
    }
    /**
    Initialization
    */
    this->p = (new DynamInt(((lambda0 )(0))));
    this->q = (new DynamInt(((lambda0 )(0))));
    this->d = (new DynamInt(((lambda0 )(0))));
    this->e = (new DynamInt(((lambda0 )(0))));
    this->phi = (new DynamInt(((lambda0 )(0))));
    /**
    Convineince numbers
    */
    this->zero = (new DynamInt(((lambda0 )(0))));
    this->zero->data = const_1;
    this->one = (new DynamInt(((lambda0 )(0))));
    this->one->data = const_2;
    return NULL;
}

DynamInt *RSA::extendedEuclid(DynamInt *A, DynamInt *B) {
    /**
    @function extendedEuclid
    finding the greatest common divisor 
    @param A, B, x, y 
    */
    DynamInt *temp;

    temp = (new DynamInt(((lambda0 )(0))));
    return temp;
}

void __init() {
    const_0 = new str("P or Q is not prime!");
    const_1 = new str("0");
    const_2 = new str("1");

    __name__ = new str("RSA");

    cl_RSA = new class_("RSA", 33, 33);
}

} // module namespace

