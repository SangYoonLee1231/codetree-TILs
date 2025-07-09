const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const inputGrid = input.slice(1, n + 1).map(line => line.split(' ').map(Number));

// Please Write your code here.
const [dr, dc] = [[1, -1, 0, 0], [0, 0, 1, -1]];
const visitedGrid = Array.from({length: n}, () => new Array(n).fill(false));
const peopleArr = [];

// 핵심 함수 1
function dfs(r, c) {
    let cnt = 1;
    visitedGrid[r][c] = true;

    for (let i = 0; i < 4; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]];

        if (canGo(nr, nc)) {
            cnt += dfs(nr, nc);
        }
    }

    return cnt;
}

// 핵심 함수 2
function searchGrid() {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (canGo(i, j)) {
                peopleArr.push(dfs(i, j));
            }
        }
    }
}

// 핵심 함수 3
function makeAnswer() {
    searchGrid();
    peopleArr.sort((a, b) => a - b);

    console.log(peopleArr.length);
    peopleArr.forEach((elem) => {
        console.log(elem);
    })
}

// 보조 함수들
function inRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

function canGo(r, c) {
    // 1. 격자를 벗어나면 패스
    // 2. 벽이 있으면 패스
    // 3. 방문한 경우 패스
    return inRange(r, c) && inputGrid[r][c] && !visitedGrid[r][c];
}

makeAnswer();