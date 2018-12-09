#include "fast.h"

struct marbel {
    unsigned long number;
    Marbel* left;
    Marbel* right;
};

Marbel* create_root_marbel() {
    return create_marbel(0, NULL, NULL);
}

Marbel* create_marbel(unsigned long number, Marbel* left, Marbel* right) {
    // All properties are immediately set, no need to clear
    Marbel* marbel = malloc(sizeof(Marbel));

    marbel->number = number;
    marbel->left = left;
    marbel->right = right;

    // Set left and right to self if they're NULL
    if (!left)  { marbel->left = marbel; }
    if (!right) { marbel->right = marbel; }

    return marbel;
}

Marbel* add_marbel(Marbel* self, unsigned long number) {
    // Get the neighbours of the new marbel
    Marbel* toLeft = self->right;
    Marbel* toRight = toLeft->right;

    // Create the new marbel
    Marbel* newMarbel = create_marbel(number, toLeft, toRight);

    // Update the neighbours' left and right
    toLeft->right = newMarbel;
    toRight->left = newMarbel;

    return newMarbel;
}

Marbel* remove_marbel_7_left(Marbel* self, unsigned long* number) {
    // Find the marbel 7 to the left
    Marbel* toRemove = self->left->left->left->left->left->left->left;

    // Get the neighbours of the marbel to remove
    Marbel* toLeft  = toRemove->left;
    Marbel* toRight = toRemove->right;

    // Link the neighbours together
    toLeft->right = toRight;
    toRight->left = toLeft;

    // Set the number to that of the removed marbel
    *number = toRemove->number;

    // Deallocate the removed marbel
    free(toRemove);

    return toRight;
}

unsigned long solve(int players, unsigned long marbels) {
    return 0;
}

int main(int argc, char** argv) {
    unsigned long result = solve(5, 25);
    printf("Result is: %lu\n", result);
    return 0;
}
