const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const inputGrid = input.slice(1, n + 1).map(line => line.split(' ').map(Number));

// Please Write your code here.
const [dr, dc] = [[1, -1, 0, 0], [0, 0, 1, -1]];
const visitedGrid = Array.from({length: n}, () => new Array(n).fill(0));
const peopleArr = [];

function dfs(r, c) {
    let cnt = 1;
    visitedGrid[r][c] = 1;

    for (let i = 0; i < 4; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]];

        if (canGo(nr, nc)) {
            cnt += dfs(nr, nc);
        }
    }

    return cnt;
}

function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

function searchGrid() {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (canGo(i, j)) {
                peopleArr.push(dfs(i, j));
            }
        }
    }
}

function canGo(r, c) {
    // 1. 격자를 벗어나면 패스
    if (!inRange(r, c)) {
        return false;
    }
    // 2. 벽이 있으면 패스
    if (!inputGrid[r][c]) {
        return false;
    }
    // 3. 방문한 경우 패스
    if (visitedGrid[r][c]) {
        return false;
    }
    return true;
}

function makeAnswer() {
    searchGrid();
    peopleArr.sort((a, b) => a - b);

    console.log(peopleArr.length);
    peopleArr.forEach((elem) => {
        console.log(elem);
    })
}

makeAnswer();