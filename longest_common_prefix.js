/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (!strs.length) return "";
    strs.sort();
    let initialArr = "";
    for (let i = 0; i<strs[0].length; i++){
        if(strs[0][i] == strs[strs.length - 1][i]){
            initialArr += strs[0][i];
        }
        else{
            break;
        }
    }
    return initialArr;
};
