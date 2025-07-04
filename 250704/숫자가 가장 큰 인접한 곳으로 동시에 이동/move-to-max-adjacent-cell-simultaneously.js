const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m, t] = input[0].split(' ').map(Number);
const grid = input.slice(1, 1 + n).map(line => line.split(' ').map(Number));
let marbles = input.slice(1 + n, 1 + n + m).map(line => line.split(' ').map(Number));

// Please Write your code here.
const [dr, dc] = [[-1, 1, 0, 0], [0, 0, -1, 1]];

function move(r, c) {
    let [maxR, maxC] = [0, 0];

    for (let dirNum = 0; dirNum < 4; dirNum++) {
        const [nr, nc] = [r + dr[dirNum], c + dc[dirNum]];
        if (isRange(nr, nc) && grid[nr][nc] > grid[r][c]) {
            [maxR, maxC] = [r, c];
        }
    }

    return [maxR, maxC];
}

function isRange(r, c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

function solution() {
    for (let time = 0; time < t; time++) {
        marbles = marbles.map((elem) => {
            let [r, c] = elem;
            [r, c] = [r - 1, c - 1];

            return move(r, c);
        })


        const unique = Array.from(                          // ❹ Set → 배열
            new Set(                                          // ❶ 문자열 중복 제거
                marbles.map(item => JSON.stringify(item))          // ❷ 각 하위배열을 문자열화
            ), 
            str => JSON.parse(str)                            // ❸ 문자열 → 원래 배열
        );

        marbles = unique;
    }

    console.log(marbles.length);
}

solution();
