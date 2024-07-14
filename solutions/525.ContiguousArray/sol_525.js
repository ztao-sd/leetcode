"use-strict";

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  let maxLength = 0;
  let zeroCount = 0;
  let oneCount = 0;
  let pairCount = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      zeroCount++;
    } else {
      oneCount++;
    }
    pairCount = Math.min(zeroCount, oneCount);
    if (pairCount * 2 > maxLength) {
      let subZeroCount = 0;
      let subOneCount = 0;
      for (let j = i; j >= 0; j--) {
        if (nums[j] === 0) {
          subZeroCount++;
        } else {
          subOneCount++;
        }
        if (subZeroCount === subOneCount && 2 * subZeroCount > maxLength) {
          maxLength = 2 * subZeroCount;
          if (subZeroCount == pairCount) break;
        }
      }
    }
  }
  return maxLength;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength2 = function (nums) {
  let maxLength = 0;
  let subLength = nums.length;
  for (let start = 0; start < nums.length - 1; start++) {
    let subZeroCount = 0;
    let subOneCount = 0;
    for (let i = start; i < nums.length; i++) {
      if (nums[i] === 0) {
        subZeroCount++;
      } else {
        subOneCount++;
      }
      if (subZeroCount === subOneCount && 2 * subZeroCount > maxLength) {
        maxLength = 2 * subZeroCount;
      }
    }
    subLength = nums.length - start;
    if (maxLength >= subLength) break;
  }
  return maxLength;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength3 = function (nums) {
  const countIndices = new Map();
  countIndices.set(0, -1);
  let count = 0;
  let maxLength = 0;
  for (let i = 0; i < nums.length; i++) {
    count += nums[i] === 1 ? 1 : -1;
    if (!countIndices.has(count)) {
      countIndices.set(count, i);
    } else {
      maxLength = Math.max(maxLength, i - countIndices.get(count));
    }
  }
  return maxLength;
};

nums = [0, 1, 0, 0, 1, 0, 1, 0, 1, 1];
const res = findMaxLength3(nums);
console.log(res);
