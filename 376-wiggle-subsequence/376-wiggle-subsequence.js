/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(N) {
    let len = N.length
    let i = 1;
    while(N[i]===N[i-1]) i++;
    let up = N[i] < N[i-1]

    let ans = 1
    
    for (; i < len; i++)
        if ((up && N[i] < N[i-1]) || (!up && N[i] > N[i-1])) 
            up = !up, ans++
            
    return ans

};