"using-string";

/*

Understanding the problem:
- input: list of non-overlapping intervals (start, end) sorted by start (ascending order)
- input: a new interval (start(*), end(*))
- task: insert new interval in list
- constraint: ascending order and non-overlapping (through merging)\
- output: list of intervals

Intuition/exploration:
- search intervals: start(i) <= start(*) <= start(i+1), end(j) <= end(*) <= end(j+1)

Cases:
- empty list
- one element
- append
- prepend
- insert between two interval

DSA tools:


Solution:

Follow up:

*/

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  const intervalsNew = [];
  const startNew = newInterval[0];
  const endNew = newInterval[1];
  let preInterval = [-2, -1];

  if (!intervals.length) {
    return [[startNew, endNew]];
  }

  for (let i = 0; i < intervals.length; i++) {
    let [start, end] = intervals[i];

    // Append interval to new list
    intervalsNew.push([start, end]);

    // Insert
    if (startNew <= start && startNew > preInterval[0]) {
      if (endNew < start) {
        // Simple insert
        if (startNew > preInterval[1]) {
          intervalsNew.push([start, end]);
          intervalsNew[i] = [startNew, endNew];
          // Merge with pre-interval
        } else {
          intervalsNew[i - 1][1] = Math.max(endNew, preInterval[1]);
        }
        // Merge into interval
      } else if (endNew >= start && endNew <= end) {
        // Merge with interval only
        if (startNew > preInterval[1]) {
          intervalsNew[i][0] = startNew;
          // Merge with both intervals
        } else {
          intervalsNew.pop();
          intervalsNew[i - 1][1] = end;
        }
      } else if (endNew > end) {
        // Merge with interval only
        if (startNew > preInterval[1]) {
          intervalsNew[i][0] = startNew;
          intervalsNew[i][1] = endNew;
          preInterval = intervals[i];
          let idx;
          for (let j = i + 1; j < intervals.length; j++) {
            let [start, end] = intervals[j];
            // Insert
            if (endNew > preInterval[1]) {
              if (endNew < start) {
                intervalsNew[i][1] = endNew;
                intervalsNew.push([start, end]);
                idx = j;
                break;
              } else if (endNew >= start && endNew <= end) {
                intervalsNew[i][1] = end;
                idx = j;
                break;
              } else {
                idx = j;
              }
            }
            preInterval = intervals[j];
          }
          i = idx;
          // Merge with both intervals
        } else {
          intervalsNew.pop();
          intervalsNew[i - 1][1] = endNew;
          preInterval = intervals[i];
          let idx;
          for (let j = i + 1; j < intervals.length; j++) {
            let [start, end] = intervals[j];
            // Insert
            if (endNew > preInterval[1]) {
              if (endNew < start) {
                intervalsNew[i - 1][1] = endNew;
                intervalsNew.push([start, end]);
                idx = j;
                break;
              } else if (endNew >= start && endNew <= end) {
                intervalsNew[i - 1][1] = end;
                idx = j;
                break;
              } else {
                idx = j;
              }
            }
            preInterval = intervals[j];
          }
          i = idx;
        }
      }
    } else if (startNew > start && i == intervals.length - 1) {
      if (startNew <= end && endNew > end) {
        intervalsNew[i][1] = endNew;
      } else if (startNew > end) {
        intervalsNew.push([startNew, endNew]);
      }
    }
    preInterval = intervals[i];
  }
  return intervalsNew;
};

let intervals = [
  [0, 0],
  [1, 4],
  [6, 8],
  [9, 11],
];
let newInterval = [0, 9];
res = insert(intervals, newInterval);
console.log(...res);
