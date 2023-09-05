/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let j = 0;
    let max = 0;

    for (let i = 1; i<prices.length; i++){
        if (prices[i] - prices[j] < 0){
            j = i;
        }
        else{
            if (max < prices[i] - prices[j]){
                max = prices[i] - prices[j]
            }

        }
    }return max
    
};