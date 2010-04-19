#ifndef __RSA_HPP
#define __RSA_HPP

#include "builtin.hpp"
#include "DynamInt.hpp"

using namespace __shedskin__;
namespace __RSA__ {

extern str *const_0, *const_1, *const_2;

using __DynamInt__::DynamInt;

class RSA;

typedef void *(*lambda2)(void *, void *, void *, void *, void *);
typedef void *(*lambda3)(void *, void *, void *, void *, void *);
typedef void *(*lambda0)(void *, void *, void *, void *, void *);
typedef void *(*lambda1)(void *, void *, void *, void *, void *);

extern str *__name__;

extern class_ *cl_RSA;
class RSA : public object {
/**
classdocs
*/
public:
    DynamInt *one;
    DynamInt *zero;
    DynamInt *phi;
    int len;
    DynamInt *e;
    DynamInt *d;
    DynamInt *q;
    DynamInt *p;

    RSA() {}
    RSA(int len) {
        this->__class__ = cl_RSA;
        __init__(len);
    }
    DynamInt *powmod(DynamInt *a, DynamInt *r, DynamInt *n);
    void *messagetonum(str *m);
    __ss_bool millerRabin(DynamInt *num);
    DynamInt *gcd(DynamInt *a, str *b);
    DynamInt *decrypt(str *m);
    DynamInt *modularExp(DynamInt *a, DynamInt *r, DynamInt *n);
    __ss_bool getdecryptkey();
    DynamInt *encrypt(str *m);
    __ss_bool createkeys(DynamInt *p, DynamInt *q);
    void *createphi();
    void *__init__(int len);
    DynamInt *extendedEuclid(DynamInt *A, DynamInt *B);
};

void __init();

} // module namespace
#endif
