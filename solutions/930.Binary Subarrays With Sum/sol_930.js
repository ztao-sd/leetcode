"using-string";

/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function (nums, goal) {
  const sumCounts = new Map();
  sumCounts.set(0, 1);
  let sum = 0;
  let res = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    if (sumCounts.has(sum - goal)) {
      res += sumCounts.get(sum - goal);
    }
    if (sumCounts.has(sum)) {
      sumCounts.set(sum, sumCounts.get(sum) + 1);
    } else {
      sumCounts.set(sum, 1);
    }
  }
  return res;
};

nums = [0, 0, 0, 0, 0];
goal = 0;
res = numSubarraysWithSum(nums, goal);
console.log(res);
