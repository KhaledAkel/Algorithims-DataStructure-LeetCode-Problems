/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const strX = x.toString();
    return strX === strX.split('').reverse().join('');
};
