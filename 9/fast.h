#ifndef FAST_H
#define FAST_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct marbel Marbel;

Marbel* create_marbel(unsigned long number, Marbel* left, Marbel* right);
Marbel* create_root_marbel();
Marbel* add_marbel(Marbel* self, unsigned long number);
Marbel* remove_marbel_7_left(Marbel* self, unsigned long* number);

unsigned long solve(int players, unsigned long marbels); 

#endif
