const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

let [n, r, c] = input[0].split(' ').map(Number);
let grid = input.slice(1, n + 1).map(line => line.split(' ').map(Number));

// Please Write your code here.
[r, c] = [r - 1, c - 1];

const [dr, dc] = [[-1, 1, 0, 0], [0, 0, -1, 1]];

const answerArr = [grid[r][c]];

function solution() {
    let isMoved = true;

    while (isMoved) {
        isMoved = move();
    }

    answerArr.forEach((elem) => {
        process.stdout.write(`${elem} `);
    })
}

function move() {
    for (let dirNum = 0; dirNum < 4; dirNum++) {
        const [nr, nc] = [r + dr[dirNum], c + dc[dirNum]];

        if (inRange(nr, nc) && grid[nr][nc] > grid[r][c]) {
            [r, c] = [nr, nc];
            answerArr.push(grid[r][c]);
            return true;
        }
    }

    return false;
}

function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

solution();