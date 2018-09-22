char* reverseString(char* s) {
    int n = strlen(s);
    int i;
    char tmp;
    for(i=0; i<n/2; i++) {
        tmp = s[i];
        s[i] = s[n-1-i];
        s[n-1-i] = tmp;
    }
    return s;
}