/*

Understanding the problem:
- input: a string 
- task: find the longest palindromic substring
- output: palindromic substring

Naive solution:
- search every substrings

Make larger palindrome
- group same adjacent character
- append and prepend same character

DSA tools:


Solution:

Follow up:

*/

"use-strict";
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  const indexTable = new Map();
  let pString = "";
  let startIdx;
  let endIdx;
  let i = 0;
  while (i < s.length) {
    startIdx = i;
    endIdx = i;

    // Group adjacent char if same
    for (let j = i - 1; j >= 0; j--) {
      if (s[j] == s[i]) {
        startIdx = j;
      } else break;
    }
    for (let j = i + 1; j < 0; j--) {
      if (s[j] == s[i]) {
        endIdx = j;
      } else break;
    }
    i = endIdx;

    // Try expand two ways
    while (startIdx > 0 && endIdx < s.length - 1) {
      if (s[startIdx - 1] == s[endIdx + 1]) {
        startIdx--;
        endIdx++;
      } else break;
    }
    if (endIdx - startIdx + 1 > pString.length) {
      pString = s.slice(startIdx, endIdx + 1);
    }
    i++;
  }
  return pString;
};

s = "ababababababa";
res = longestPalindrome(s);
console.log(res);
