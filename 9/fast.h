#ifndef FAST_H
#define FAST_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct marbel Marbel;

Marbel* create_marbel(unsigned long number, Marbel* left, Marbel* right);

unsigned long solve(int players, unsigned long marbels); 

#endif
