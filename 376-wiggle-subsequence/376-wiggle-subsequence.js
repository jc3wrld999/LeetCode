/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(N) {
//     let len = N.length
//     let i = 1;
//     while(N[i]===N[i-1]) i++;
//     let up = N[i] > N[i-1]
//     console.log(up)
//     let ans = 1

//     for (; i < len-1; i++)
//         if ((up && N[i] > N[i+1]) || (!up && N[i] < N[i+1])) {
//             up = !up, ans++
//             console.log(N[i])
//         }
            
//     return ans
        let len = N.length, i = 1
    while (N[i] === N[i-1]) i++
    let up = N[i-1] > N[i], ans = 1
    for (; i < len; i++)
        if ((up && N[i] < N[i-1]) || (!up && N[i] > N[i-1]))
            up = !up, ans++
    return ans
};