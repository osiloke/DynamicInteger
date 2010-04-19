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
    DynamInt(lambda0 num) {
        this->__class__ = cl_DynamInt;
        __init__(num);
    }
    str *__mod__(DynamInt *num);
    void *random(lambda1 length);
    DynamInt *__add__(int num);
    __ss_bool __gt__(DynamInt *num);
    DynamInt *__sub__(DynamInt *num);
    __ss_bool __eq__(DynamInt *num);
    void *__init__(lambda0 num);
    void *setData(str *stri);
};

void __init();

} // module namespace
#endif
