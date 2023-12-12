# Compiler to use
CC = gcc
# Flags for the compiler
# -ansi: tells the compiler to implement the ANSI language option
#  -Wall: turn on all warnings
#  -pedantic: turn on pendantic warnings
CFLAGS = -ansi -Wall -pedantic

# default target
all: dotproduct

# target for final executable
dotproduct: producto_punto.o
	$(CC) $(CFLAGS) producto_punto.o -o dotproduct

# compile source files into object files
producto_punto.o: producto_punto.c
	$(CC) $(CFLAGS) -c producto_punto.c

clean:
	rm -f *.o dotproduct

