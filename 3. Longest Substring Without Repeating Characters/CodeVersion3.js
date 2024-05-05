/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length <= 1){
        return s.length;
    }

    let visited = new Set();
    let longest = 0, i = 0, j = 0;

    while (i < s.length && j < s.length) {
        if (!visited.has(s[j])){
            visited.add(s[j]);
            j++;
            longest = Math.max(longest, j - i);
        } else {
            visited.delete(s[i]);
            i++;
        }
    }

    return longest;
};
