CC=g++
CCFLAGS=-O2 -pipe -Wno-deprecated $(CPPFLAGS) -I. -I/usr/local/lib/python2.6/dist-packages/shedskin/lib
LFLAGS=-lgc -lpcre $(LDFLAGS)

.PHONY: all run full clean

all:	RSAtest

run:	all
	./RSAtest

full:
	shedskin RSAtest; $(MAKE) run

CPPFILES=/usr/local/lib/python2.6/dist-packages/shedskin/lib/random.cpp RSA.cpp DynamInt.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/builtin.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/time.cpp RSAtest.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/math.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/re.cpp
HPPFILES=/usr/local/lib/python2.6/dist-packages/shedskin/lib/random.hpp RSA.hpp DynamInt.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/builtin.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/time.hpp RSAtest.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/math.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/re.hpp

RSAtest:	$(CPPFILES) $(HPPFILES)
	$(CC) $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o RSAtest

clean:
	rm RSAtest
