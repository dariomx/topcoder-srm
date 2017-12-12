#include <stdlib.h>

int subarraySum(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n == 0)
        return 0;
    int * psum = (int *) malloc(sizeof(int)*n);
    psum[0] = nums[0];
    for(int i=1; i<n; i++)
        psum[i] = psum[i-1] + nums[i];
    int cnt = 0;
    for(int i=0; i<n; i++)
        for(int j=i; j<n; j++)
            if (psum[j] - (i>0? psum[i-1] : 0) == k)
                cnt += 1;
    return cnt;
}