/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const hashMap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    };

    const out = [];

    const dfs = (start, comb) => {
        if (start === digits.length) {
            out.push(comb);
            return;
        }

        for (const char of hashMap[digits[start]]) {
            dfs(start + 1, comb + char);
        }
    };

    if (digits) {
        dfs(0, "");
    }

    return out;
};
