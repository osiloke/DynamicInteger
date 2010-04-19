#include "RSAtest.hpp"

/**
Created on Apr 1, 2010

@author: oc
*/

namespace __RSAtest__ {

str *const_0, *const_1, *const_2, *const_3;

str *__name__;


void *__ss_main() {
    RSA *rsa;
    str *m;
    int __0, __1, a, b;
    DynamInt *one;

    print(1, const_0);
    rsa = (new RSA(3));
    print(1, const_1);
    /**
    one = DynamInt(2)
    two = DynamInt(2)
    */
    /**
    rsa.gcd(one, two)
    */
    m = const_2;
    one = (new DynamInt(0));
    rsa->decrypt(m);
    rsa->encrypt(m);
    rsa->powmod(one, one, one);
    rsa->messagetonum(m);
    rsa->getdecryptkey();
    rsa->createkeys(one, one);
    a = 533573;
    b = 15;

    while ((a>0)) {
        __0 = __mods(b, a);
        __1 = a;
        a = __0;
        b = __1;
    }
    print(1, __str(b));
    /**
    temp = rsa.randomprime()
    */
    /**
    temp.printme()
    */
    return NULL;
}

void __init() {
    const_0 = new str("random prime");
    const_1 = new str("Created RSA");
    const_2 = new str("");
    const_3 = new str("__main__");

    __name__ = new str("__main__");

    if (__eq(__name__, const_3)) {
        __ss_main();
    }
}

} // module namespace

int main(int, char **) {
    __shedskin__::__init();
    __math__::__init();
    __time__::__init();
    __random__::__init();
    __DynamInt__::__init();
    __RSA__::__init();
    __shedskin__::__start(__RSAtest__::__init);
}
