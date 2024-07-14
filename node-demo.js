"use strict";

/**
 * @param {number[]} nums
 * @return {number}
 */
x = ":clap:";
var maxFrequencyElements = function (nums) {
  let dict = {};
  let maxFreq = 0;
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let key = nums[i];
    // Count frequency of each element
    if (key in dict) {
      dict[nums[i]] += 1;
    } else {
      dict[nums[i]] = 1;
    }
    // Determine max frequency and count
    let elemFreq = dict[nums[i]];
    if (elemFreq > maxFreq) {
      maxFreq = elemFreq;
      count = 1;
    } else if (elemFreq == maxFreq) {
      count += 1;
    }
  }
  return maxFreq * count;
};

let x = maxFrequencyElements([1, 2, 3, 4, 11, 23]);
console.log(x);
