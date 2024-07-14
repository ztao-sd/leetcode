"using-string";

/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function (points) {
  let subLen = 1;

  // Merge sort
  while (subLen <= points.length - (points.length % 2)) {
    for (let i = 0; i < Math.ceil(points.length / subLen); i++) {
      let left = points.slice(i * subLen, (i + 1) * subLen);
      let right = points.slice((i + 1) * subLen, (i + 2) * subLen);
      let [j, k, l] = [0, 0, i * subLen];
      while (j < left.length && k < right.length) {
        if (left[j][0] <= right[k][0]) {
          points[l] = left[j];
          j++;
        } else {
          points[l] = right[k];
          k++;
        }
        l++;
      }
      while (j < left.length) {
        points[l] = left[j];
        j++;
        l++;
      }
      while (k < right.length) {
        points[l] = right[k];
        k++;
        l++;
      }
      i++;
    }
    subLen *= 2;
  }

  // Calculate overlap
  let end = points[0][1];
  let start;
  let numArrow = points.length;
  for (let i = 1; i < points.length; i++) {
    start = points[i][0];
    if (start <= end) {
      numArrow--;
      end = Math.min(end, points[i][1]);
    } else {
      end = points[i][1];
    }
  }

  return numArrow;
};

let points = [
  [1, 2],
  [0, 4],
  [6, 9],
  [3, 4],
  [2, 10],
];
res = findMinArrowShots(points);
console.log(res);
