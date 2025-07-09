const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const moves = [];
for (let i = 1; i <= m; i++) {
    moves.push(input[i].split(" ").map(Number));
}

// Please Write your code here.
const grid = Array.from({ length: n }, () => Array(n).fill(0));

const [dr, dc] = [[1, -1, 0, 0], [0, 0, 1, -1]];


function paintAndCheck(r, c) {
    grid[r][c] = 1;
    let checkPaint = 0;

    for (let i = 0; i < 4; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]];

        if (inRange(nr, nc)) {
            checkPaint += grid[nr][nc];
        }
    }

    if (checkPaint >= 3) {
        // 편안한 상태
        return 1;
    } else {
        // 편안한 상태 아님
        return 0;
    }
}

function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

function solution() {
    moves.forEach((elem) => {
        const [r, c] = elem;
        console.log(paintAndCheck(r - 1, c - 1));
    })
}

solution();
