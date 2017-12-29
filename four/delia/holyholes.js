function solution(A) {
    n = A.length;
    B = [];
    for (i=0;i<n;i++) B[A[i]-1] = 1;
    for (i=0;i<B.length;i++) if(!B[i]) return i+1;
    return B.length+1;
}
