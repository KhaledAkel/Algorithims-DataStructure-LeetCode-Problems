/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let number = x.toString();
    let neg = x < 0;

    if (neg) {
        number = number.substring(1);
    }

    let res = 0;
    for (let i = 0; i < number.length; i++) {
        res += parseInt(number[i]) * (10 ** i);
    }

    if (neg) {
        res = -res;
    }

    // Check for 32-bit signed integer overflow
    if (res < -(2 ** 31) || res > (2 ** 31) - 1) {
        return 0;
    }

    return res;
};
