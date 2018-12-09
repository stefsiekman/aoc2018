#include "fast.h"

struct marbel {
    unsigned long number;
    Marbel* left;
    Marbel* right;
};

Marbel* create_marbel(unsigned long number, Marbel* left, Marbel* right) {
    // All properties are immediately set, no need to clear
    Marbel* marbel = malloc(sizeof(Marbel));

    marbel->number = number;
    marbel->left = left;
    marbel->right = right;

    // Set left and right to self if they're NULL
    if (!left) { marbel->left = marbel; }
    if (!right) { marbel->right = marbel; }

    return marbel;
}

unsigned long solve(int players, unsigned long marbels) {
    return 0;
}

int main(int argc, char** argv) {
    unsigned long result = solve(5, 25);
    printf("Result is: %lu\n", result);
    return 0;
}
