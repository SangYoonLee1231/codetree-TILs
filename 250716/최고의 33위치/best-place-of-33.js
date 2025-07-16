const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const grid = input.slice(1).map(line => line.split(' ').map(Number));

// Please Write your code here.
function solution() {
    let maxCount = 0;

    function chooseGrid(n) {
        for (let i = 0; i < n - 2; i++) {
            for (let j = 0; j < n - 2; j++) {
                const count = gridSearch(i, j);
                maxCount = Math.max(count, maxCount);
            }
        }
    }

    function gridSearch(r, c) {
        let count = 0;

        for (let i = 0; i < 3; i++) {
            for(let j = 0; j < 3; j++) {
                count += grid[r + i][c + j];
            }
        }

        return count;
    }

    chooseGrid(n);
    return maxCount;
}

console.log(solution());