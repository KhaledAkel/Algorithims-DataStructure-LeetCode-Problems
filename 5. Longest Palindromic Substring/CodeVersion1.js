/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length <= 1) {
        return s;
    }
    
    let maxLen = 1;
    let maxStr = s[0];

    for (let i = 0; i < s.length - 1; i++) {
        for (let j = i + 1; j < s.length; j++) {
            if ((j - i + 1) > maxLen && s.substring(i, j + 1) === s.substring(i, j + 1).split('').reverse().join('')) {
                maxLen = s.substring(i, j + 1).length;
                maxStr = s.substring(i, j + 1);
            }
        }
    }
    return maxStr;
};
