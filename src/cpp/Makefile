CC=g++
CCFLAGS=-O2 -pipe -Wno-deprecated $(CPPFLAGS) -I. -I/usr/local/lib/python2.6/dist-packages/shedskin/lib
LFLAGS=-lgc -lpcre $(LDFLAGS)

.PHONY: all run full clean

all:	main

run:	all
	./main

full:
	shedskin main; $(MAKE) run

CPPFILES=/usr/local/lib/python2.6/dist-packages/shedskin/lib/random.cpp DynamInt.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/builtin.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/time.cpp main.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/math.cpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/re.cpp
HPPFILES=/usr/local/lib/python2.6/dist-packages/shedskin/lib/random.hpp DynamInt.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/builtin.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/time.hpp main.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/math.hpp /usr/local/lib/python2.6/dist-packages/shedskin/lib/re.hpp

main:	$(CPPFILES) $(HPPFILES)
	$(CC) $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o main

clean:
	rm main
