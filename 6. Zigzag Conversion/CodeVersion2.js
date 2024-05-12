/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1 || numRows >= s.length) {
        return s;
    }

    const matrix = [];
    for (let i = 0; i < numRows; i++) {
        matrix.push([]);
    }
    let i = 0;
    let direction = 1; // 1 for down, -1 for up

    for (const char of s) {
        matrix[i].push(char);
        if (i === 0) {
            direction = 1;
        } else if (i === numRows - 1) {
            direction = -1;
        }
        i += direction;
    }

    // Concatenate the characters row by row
    let convertedString = '';
    for (const row of matrix) {
        convertedString += row.join('');
    }
    return convertedString;
};
