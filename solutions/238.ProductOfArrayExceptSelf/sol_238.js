"using-string";

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const ans = [1];
  let product = 1;
  for (let i = 1; i < nums.length; i++) {
    product *= nums[i - 1];
    ans[i] = product;
  }
  product = 1;
  for (let i = nums.length - 2; i >= 0; i--) {
    product *= nums[i + 1];
    ans[i] *= product;
  }
  return ans;
};

nums = [-1, 1, 0, -3, 3];
res = productExceptSelf(nums);
console.log(res);
