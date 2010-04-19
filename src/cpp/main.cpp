#include "main.hpp"

/**
Created on Feb 25, 2010

@author: oc
*/

namespace __main__ {

str *const_0, *const_1, *const_2;

str *__name__;


void *__ss_main() {
    DynamInt *b, *temp, *test;

    test = (new DynamInt(1));
    test->printme();
    b = (new DynamInt(2));
    b->printme();
    print(1, (const_0)->__add__(b->data));
    print(1, (const_0)->__add__(b->data));
    temp = (new DynamInt(0));
    temp = test->__add__(b);
    print(1, (const_1)->__add__(temp->data));
    temp = test->__sub__(b);
    print(1, temp->data);
    print(1, __box(___bool(__gt(b, test))));
    print(1, __box(___bool(__lt(b, test))));
    print(1, __box(___bool(__eq(b, test))));
    temp = b->__mul__(test);
    print(1, temp->data);
    temp = b->__div__(test);
    print(1, temp->data);
    return NULL;
}

void __init() {
    const_0 = new str("b.data ");
    const_1 = new str("Adding test to b ");
    const_2 = new str("__main__");

    __name__ = new str("__main__");

    if (__eq(__name__, const_2)) {
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
    __shedskin__::__start(__main__::__init);
}
