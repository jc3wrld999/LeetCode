/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} hc
 * @param {number[]} vc
 * @return {number}
 */
var maxArea = function(h, w, hc, vc) {
    hc.sort((a,b) => a - b)
    vc.sort((a,b) => a - b)
    let max_h = Math.max(hc[0], h - hc[hc.length - 1]);
    let max_v = Math.max(vc[0], w - vc[vc.length - 1]);
    for (let i = 1; i < hc.length;i++) {
        max_h = Math.max(hc[i]-hc[i - 1], max_h)
    }
    for (let i = 1; i < vc.length;i++) {
        max_v = Math.max(vc[i]-vc[i - 1], max_v)
    }
    return BigInt(max_h) * BigInt(max_v) % 1000000007n
};