function solution(A) {
    n = A.length;
    B = [];
    for(i=0;i<n;i++) {
        if (A[i] > n+1 || A[i] < 1 || B[A[i]-1]) return 0;
        else B[A[i]-1] = 1;
    }
    for(i=0;i<n;i++) if (!B[i]) return 0;
    return 1;
}
