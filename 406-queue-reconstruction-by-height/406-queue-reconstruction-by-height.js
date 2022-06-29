/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    var result= [];
    people.sort((a,b)=>a[1]-b[1]).sort((a,b)=>b[0]-a[0]);
    for(var i=0; i<people.length; i++) {
        result.splice(people[i][1], 0, people[i]);
    }
    return result;
};