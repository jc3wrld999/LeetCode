/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let nmap = new Map(), ans = 0,
        seen = new Uint32Array(nums.length)
    for (let i = 0; i < nums.length; i++)
        if (!nmap.has(nums[i])) nmap.set(nums[i], i)
    for (let n of nums) {
        let curr = n, count = 1
        if (seen[nmap.get(curr)]) continue
        while (nmap.has(curr+1)) {
            let ix = nmap.get(++curr)
            if (seen[ix]) {
                count += seen[ix]
                break
            } else seen[ix] = 1, count++
        }
        seen[nmap.get(n)] = count
        ans = Math.max(ans, count)
    }
    return ans
};