const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const grid = input.slice(1).map(line => line.split(' ').map(Number));

let answer = 0;

// Please Write your code here.
function countOneBlock(r, c) {
    const [dr, dc] = [[1, -1, 0, 0], [0, 0, 1, -1]];
    let count = 0;

    for (let i = 0; i < 4; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]];

        if (inRange(nr, nc) && grid[nr][nc] === 1) {
            count++;
        }
    }

    return count;
}

function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

function solution() {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (countOneBlock(i, j) >= 3) {
                answer++;
            }
        }
    }

    console.log(answer);
}

solution();