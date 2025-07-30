const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, k] = input[0].trim().split(' ').map(Number);
const grid = input.slice(1, 1 + n).map(line => line.trim().split(' ').map(Number));

// Please Write your code here.
const prefixSum = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
const maxGrid = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
let ans = 0;

// 초기화
prefixSum[1][1] = grid[0][0]

for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + grid[i - 1][j - 1];
    }
}

for (let i = k; i <= n; i++) {
    for (let j = k; j <= n; j++) {
        maxGrid[i][j] = prefixSum[i][j] - prefixSum[i - k][j] - prefixSum[i][j - k] + prefixSum[i - k][j - k] 
    }
}

for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= n; j++) {
        ans = Math.max(ans, maxGrid[i][j])
    }
}

console.log(ans);