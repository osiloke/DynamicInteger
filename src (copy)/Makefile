CC=g++
CCFLAGS=-O2 -pipe -Wno-deprecated $(CPPFLAGS) -I. -IC:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib
LFLAGS=-lgc -lpcre $(LDFLAGS)

.PHONY: all run full clean

all:	main

run:	all
	./main

full:
	shedskin main; $(MAKE) run

CPPFILES=C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/builtin.cpp main.cpp C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/math.cpp DynamInt.cpp C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/re.cpp
HPPFILES=C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/builtin.hpp main.hpp C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/math.hpp DynamInt.hpp C:/Users/oc/Documents/Downloads/shedskin-0.3/shedskin/shedskin/lib/re.hpp

main:	$(CPPFILES) $(HPPFILES)
	$(CC) $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o main

clean:
	rm main.exe
