/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(N) {
    let nmap = new Map(), ans = 0,
        seen = new Uint32Array(N.length)
    for (let i = 0; i < N.length; i++)
        if (!nmap.has(N[i])) nmap.set(N[i], i)
    for (let n of N) {
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