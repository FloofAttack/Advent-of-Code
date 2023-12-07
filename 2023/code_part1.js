async function get_input() {
  const response = await fetch ("https://adventofcode.com/2023/day/1/input");
  const output = await response.text();
  return output;
}
function calValue(item) {
  const num_array = item.match(regex);
  const string = "" + num_array[0] + num_array[num_array.length - 1];
  console.log(string);
  sum += parseInt(string);
}

var regex = /\d/g;
var test_array = ["1abc2",
                  "pqr3stu8vwx",
                  "a1b2c3d4e5f",
                  "treb7uchet" ];

get_input().then(x => {
  var test = x.split("\n");
  var sum = 0;
  test.forEach(e => {
    if (e) {
    	const nums = e.match(regex);
      console.log(nums);
    	const string = "" + nums[0] + nums[nums.length - 1];
    	sum += parseInt(string);
    }
  });
  console.log(sum);
});
