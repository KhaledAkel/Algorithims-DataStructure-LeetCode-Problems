
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // Convert the number to a string
    const num = x.toString();

    // Check if the number is negative
    if (num[0] === '-') {
        return false;
    }

    // Reverse the string
    const rev = num.split('').reverse().join('');

    // Check if the reversed string is equal to the original string
    return num === rev;
};
