function solution(X, A) {
    n = A.length;
    if (n < X) return -1;
    numMissingLeaves = X;
    B = [];
    for (i=0; i<n; i++) {
        if (A[i]<=n && !B[A[i]-1]) {
            if (numMissingLeaves==1) return i;
            B[A[i]-1] = 1;
            numMissingLeaves--;
        }
    }
    return -1;
}
