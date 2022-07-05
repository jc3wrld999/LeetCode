/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(N) {

    if(N.length == 0)return 0;
    N.sort((a,b) => a-b);
    let count = 1, max = 0;

    for(let i = 1;i<N.length;i++) {
        if(N[i]-N[i-1] === 1) count++;
        else if(N[i] !== N[i-1]){
            console.log(N[i])
            max = Math.max(max, count)
            count = 1;
        }
    }
    return Math.max(max, count)
};