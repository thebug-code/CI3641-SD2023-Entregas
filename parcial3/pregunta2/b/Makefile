# Compiler to use
CC = gcc
# Flags for the compiler
# -ansi: tells the compiler to implement the ANSI language option
#  -D_GNU_SOURCE: define GNU extensions
#  -Wall: turn on all warnings
#  -pedantic: turn on pendantic warnings
CFLAGS = -ansi -D_GNU_SOURCE -Wall -pedantic

# default target
all: countfiles

# target for final executable
countfiles: countfiles.o
	$(CC) $(CFLAGS) countfiles.o -o countfiles

# compile source files into object files
countfiles.o: countfiles.c
	$(CC) $(CFLAGS) -c countfiles.c

clean:
	rm -f *.o countfiles


