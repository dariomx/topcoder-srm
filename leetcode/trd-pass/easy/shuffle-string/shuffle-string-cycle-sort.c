// my code but not my idea, saw in phorum that one can use cycle sort for
// O(n^2), so we trace space for time.

void swapChar(char * s, int i, int j) {
    char tmp = s[i];
    s[i] = s[j];
    s[j] = tmp;
}

void swapInt(int * ix, int i, int j) {
    int tmp = ix[i];
    ix[i] = ix[j];
    ix[j] = tmp;
}

char * restoreString(char * s, int* indices, int n){
    int i = 0;
    while (i < n) {
        int j = indices[i];
        if (i == j) {
            i++;
        } else {
            swapChar(s, i, j);
            swapInt(indices, i, j);
        }
    }
    return s;
}