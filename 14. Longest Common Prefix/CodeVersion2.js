/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return "";
    }

    let l = 0;
    let pre = "";
    let con = true;
    
    while (con) {
        for (let i = 0; i < strs.length; i++) {
            if (l >= strs[i].length) {
                con = false;
                break;
            }
            if (i === 0) {
                var letter = strs[i][l];
            } else if (strs[i][l] !== letter) {
                con = false;
                break;
            }
        }
        if (con) {
            pre += letter;
            l++;
        }
    }

    return pre;
    
};
