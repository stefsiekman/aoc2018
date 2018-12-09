.PHONY: all clean cleaner run

all: run clean

run: fast
	@./fast

fast: fast.o
	@$(CC) $(CFLAGS) $< -o $@

fast.o: fast.c fast.h
	@$(CC) $(CFLAGS) -c $< -o $@

clean:
	@rm -f fast.o

cleaner: clean
	@rm -f fast
