const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, t] = input[0].split(" ").map(Number);
let [r, c, d] = input[1].split(" ");
[r, c] = [r, c].map(Number);

const grid = Array.from({ length: n }, () => Array(n).fill(0));

const dir = {
    'U': 0,
    'D': 3,
    'R': 1,
    'L': 2,
};

let dir_num = dir[d];

const [drs, dcs] = [[-1, 0, 0, 1], [0, 1, -1, 0]];

//
function oneMove(cr, cc) {
    const [nr, nc] = [cr + drs[dir_num], cc + dcs[dir_num]];

    if (!inRange(nr, nc)) {
        // 위치 변경
        dir_num = 3 - dir_num;
        return [cr, cc];
    }

    return [nr, nc];
}

function inRange(r, c) {
    return r >= 1 && r <= n && c >= 1 && c <= n;
}

function tMove(r, c) {
    let [currR, currC] = [r, c];

    for (let i = 0; i < t; i++) {
        [currR, currC] = oneMove(currR, currC);
    }

    return [currR, currC];
}

function printSpot(r, c) {
    const [resultR, resultC] = tMove(r, c);
    console.log(resultR, resultC);
}

printSpot(r, c);