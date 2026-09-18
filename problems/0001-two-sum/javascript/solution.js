// Time: O(n) | Space: O(n)
// Store each seen number and its index, then look up the complement.

function twoSum(nums, target) {
  const seen = new Map();

  for (let index = 0; index < nums.length; index += 1) {
    const needed = target - nums[index];
    if (seen.has(needed)) {
      return [seen.get(needed), index];
    }
    seen.set(nums[index], index);
  }

  throw new Error("No valid pair exists");
}

module.exports = { twoSum };
