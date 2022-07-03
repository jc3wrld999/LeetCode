/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} hc
 * @param {number[]} vc
 * @return {number}
 */
var maxArea = function(h, w, hc, vc) {
    hc.sort((a,b) => a - b)
    hc.push(h)
    vc.sort((a,b) => a - b)
    vc.push(w)
    let max_h = hc[0];
    let max_v = vc[0];
    for (let i = 0; i < hc.length - 1;i++) {

        max_h = Math.max(hc[i+1]-hc[i], max_h)
        console.log(max_h)

    }
    for (let i = 0; i < vc.length - 1;i++) {
        max_v = Math.max(vc[i+1]-vc[i], max_v)
        console.log(max_v)
    }
    return BigInt(max_h) * BigInt(max_v) % 1000000007n
};