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
    // Initialization of player scores
    int currentPlayer = 1;
    int scores[players];
    for (int i = 0; i < players; i++) {
        scores[i] = 0;
    }

    // The current marbel
    Marbel* currentMarbel = create_root_marbel();

    // Iterate over all the marbels that should be added
    for (unsigned long marbel = 1; marbel <= marbels; marbel++) {
        // Are we at the special 23-case?
        if (marbel % 23 == 0) {
            // Add the current marbel as score
            scores[currentPlayer - 1] += marbel;

            // Remove the marbel 7 to the left
            unsigned long number = 0;
            currentMarbel = remove_marbel_7_left(currentMarbel, &number);

            // Add the number of the removed marbel to the score as well
            scores[currentPlayer - 1] += number;
        } else {
            // Default is just to add the marbel
            currentMarbel = add_marbel(currentMarbel, marbel);
        }

        // Go to the next player
        currentPlayer++;
        if (currentPlayer > players) {
            currentPlayer = 1;
        }
    }

    // Find the highest score
    unsigned long maxScore = scores[0];
    for (int i = 1; i < players; i++) {
        if (scores[i] > maxScore) {
            maxScore = scores[i];
        }
    }

    return maxScore;
}

int main(int argc, char** argv) {
    unsigned long result = solve(5, 25);
    printf("Result is: %lu\n", result);
    return 0;
}
