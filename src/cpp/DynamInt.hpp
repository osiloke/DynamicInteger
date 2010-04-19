#ifndef __DYNAMINT_HPP
#define __DYNAMINT_HPP

#include "builtin.hpp"
#include "random.hpp"
#include "math.hpp"

using namespace __shedskin__;
namespace __DynamInt__ {

extern str *const_0, *const_1, *const_2;


class DynamInt;


extern str *__name__;

extern class_ *cl_DynamInt;
class DynamInt : public pyobj {
/**
classdocs
*/
public:
    __ss_bool neg;
    str *data;
    int size;

    DynamInt() {}
    DynamInt(int num) {
        this->__class__ = cl_DynamInt;
        __init__(num);
    }
    void *random(int length);
    void *printme();
    str *__div__(DynamInt *num);
    str *__mul__(DynamInt *num);
    str *__add__(DynamInt *num);
    __ss_bool __gt__(DynamInt *num);
    str *__sub__(DynamInt *num);
    __ss_bool __lt__(DynamInt *num);
    __ss_bool __eq__(DynamInt *num);
    void *__init__(int num);
    void *setData(str *stri);
};

void __init();

} // module namespace
#endif
