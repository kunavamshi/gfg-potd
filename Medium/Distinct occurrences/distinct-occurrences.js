//{ Driver Code Starts
//Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}


function main() {
  let t = parseInt(readLine());
  let i = 0;
  for (; i < t; i++) {
   let input_line = readLine().split(" ");
   let [S,T] = input_line;
   let obj = new Solution();
   let res = obj.subsequenceCount(S,T);
   console.log(res);
    
  }
}
// } Driver Code Ends


//User function Template for javascript

/**
 * @param {string} S
 * @param {string} T
 * @returns {number}
*/

class Solution {
  subsequenceCount(S, T) {
    const mod = 10**9 + 7;
    const n = S.length;
    const m = T.length;

    // Initialize a 2D array to store the counts
    const dp = new Array(n + 1).fill(0).map(() => new Array(m + 1).fill(0));

    // Initialize the base case
    for (let i = 0; i <= n; i++) {
      dp[i][0] = 1;
    }

    // Dynamic Programming to compute the counts
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= m; j++) {
        if (S[i - 1] !== T[j - 1]) {
          dp[i][j] = dp[i - 1][j];
        } else {
          dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod;
        }
      }
    }

    // Return the count of sub-sequences modulo 10^9 + 7
    return dp[n][m];
  }
}

// Example usage
let obj = new Solution();
let res = obj.subsequenceCount("banana", "ban");
