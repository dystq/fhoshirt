function solution(A) {
    collisions = 0;
    n = A.length;
    onesSeen = 0;
    lastTimeISawOne = -1;
    for(i=0;i<n;i++) {
        if(A[i] == 1) {
            lastTimeISawOne = i;
            collisions += (i+1)- ++onesSeen;
        }
    }
    zeroesSeen = 0;
    lastTimeISawZero = -1;
    for(j=0;j<n;j++) {
        if(A[n-j-1] == 0) {
            lastTimeISawZero = j;
            collisions += (j+1)- ++zeroesSeen;
        }
    }
    if (collisions > 2000000000) return -1;
    else return collisions/2;
}
