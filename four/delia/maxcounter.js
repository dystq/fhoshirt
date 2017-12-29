function solution(N, A) {
    counters = [];
    for(i=0;i<N;i++) counters[i] = 0;  
    maxCounter = 0;
    maxBernardy = 0; 
    for(j=0;j<A.length;j++){
        if(A[j]==N+1) maxBernardy = maxCounter; 
        else if (A[j] < N+1) { 
            counters[A[j]-1] = 1 + Math.max(counters[A[j]-1],maxBernardy);
            maxCounter = Math.max(maxCounter, counters[A[j]-1]);
        }
    }
    for(k=0;k<N;k++) counters[k] = Math.max(maxBernardy,counters[k]);
    return counters;
}
