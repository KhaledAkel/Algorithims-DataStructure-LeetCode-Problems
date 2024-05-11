/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length === 1) {
        return s;
    }
    
    let maxStr = s[0];

    function expand(l, r) {
        while (l >= 0 && r <= s.length - 1 && s[l] === s[r]) {
            l--;
            r++;
        }
        return s.substring(l + 1, r);
    }

    for (let i = 0; i < s.length - 1; i++) {
        let odd = expand(i, i);
        let even = expand(i, i + 1);

        if (odd.length > maxStr.length) {
            maxStr = odd;
        }
        if (even.length > maxStr.length) {
            maxStr = even;
        }
    }
    return maxStr;
};
