class Solution {
    countSetBits(N) {
        let ans = 0;

        while (N > 0) {
            // find highest power of 2 <= N (fast integer trick)
            let p = highestPowerOf2(N);

            // x = log2(p)
            let x = powerIndex(p);

            // bits from 1 to p-1 : x * 2^(x-1)
            ans += x * (p >> 1);

            // MSB bits from p..N : (N - p + 1)
            ans += (N - p + 1);

            // reduce N
            N -= p;
        }

        return ans;
    }
}

// returns largest power of 2 <= n
function highestPowerOf2(n) {
    n |= (n >> 1);
    n |= (n >> 2);
    n |= (n >> 4);
    n |= (n >> 8);
    n |= (n >> 16);
    return (n + 1) >> 1;
}

// returns index of bit (log2) WITHOUT floating point
function powerIndex(p) {
    let x = 0;
    while (p > 1) {
        p >>= 1;
        x++;
    }
    return x;
}