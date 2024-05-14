/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let neg = false;
    let leadingZero = true;
    let digit = 1;
    let res = 0;

    for (let i = 0; i < s.length; i++) {
        let ele = s[i];
        if (ele === " ") {
            if (!leadingZero) {
                break;
            } else {
                continue;
            }
        }

        if (ele === "-" || ele === "+") {
            if (!leadingZero) {
                break;
            }
            neg = ele === "-";
            leadingZero = false;
            continue;
        }

        if (!isNaN(parseInt(ele))) {
            leadingZero = false;
            if (!leadingZero) {
                res = res * 10 + parseInt(ele);
                digit *= 10;
            }
        } else {
            break;
        }
    }

    res = neg ? -res : res;
    return Math.max(Math.min(res, 2 ** 31 - 1), -(2 ** 31));
};
