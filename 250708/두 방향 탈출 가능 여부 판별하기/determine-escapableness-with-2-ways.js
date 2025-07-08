const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const snakeGrid = input.slice(1, n + 1).map(row => row.split(' ').map(Number));

// Please Write your code here.
const visitedGrid = Array.from({ length: n }, () => Array(m).fill(0));

function dfs(r, c) {
    const [dr, dc] = [[1, 0], [0, 1]];

    for (let i = 0; i < 2; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]];

        if (canGo(nr, nc)) {
            visitedGrid[nr][nc] = 1;
            dfs(nr, nc);
        }
    }
}

function canGo(r, c) {
    if (!inRange(r, c)) {
        return false;
    }
    if (visitedGrid[r][c]) {
        return false;
    }
    if (!snakeGrid[r][c]) {
        return false;
    }
    return true;
}

function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < m;
}

function canEscape(r, c) {
    dfs(0, 0);

    if (visitedGrid[r - 1][c - 1] === 1) {
        return 1;
    }
    return 0;
}

console.log(canEscape(n, m));
