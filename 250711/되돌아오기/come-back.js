const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0]);
const moves = input.slice(1);

// Please Write your code here.
// const MAX_ROW_COL = 4001

const [startR, startC] = [1000, 1000];
let [r, c] = [1000, 1000];

const [drs, dcs] = [[-1, 0, 1, 0], [0, 1, 0, -1]];

const dirConvert = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

function solution() {
    // const grid = Array.from({ length: MAX_ROW_COL }, () => Array(MAX_ROW_COL).fill(0));
    console.log(move());
}

function move() {
    let time = 0;

    for (let i = 0; i < moves.length; i++) {
        let [dir, dist] = moves[i].split(" ");
        dist = Number(dist);

        const [dr, dc] = [drs[dirConvert[dir]], dcs[dirConvert[dir]]];

        for (let currMove = 0; currMove < dist; currMove++) {
            [r, c] = [r + dr, c + dc];
            time++;

            if (r === startR && c === startC) {
                return time;
            }
        }
    }

    return -1;
}

solution();