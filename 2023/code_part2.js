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

function getAllinArray(item,string) {
  var i = 0;
  var n = 0;
  var matches = [];
  while (n != -1){
    if (string.indexOf(item,i) != -1){
    	matches.push(string.indexOf(item,i));
    }
    n = string.indexOf(item,i);
    i = n + 1;
  }
  return matches;
}

var correction = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
     "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9
};

var regex = /\d/g;
var test_array = ["1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
     "26"];

var test_array2 = [ "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen" ];

var test3 = test_array2.concat(test_array);

var test4 = ["five3xhpsdfkg94two3six"];
get_input().then(x => {
    var test = x.split("\n");
    var sum = [];
  	var realsum = 0;
    test.forEach(e => {
     	if (e) {
     		console.log(e);
				var dict = {};
        Object.keys(correction).forEach(k => {
        	var match = getAllinArray(k,e);
					match.forEach(m => {
						dict[m] = correction[k];
						});
          });
         	//console.log(dict);
        	var max = Math.max(...Object.keys(dict).map(Number));
        	var min = Math.min(...Object.keys(dict).map(Number));
        	//console.log("Min is " + dict[min] + ", " + "Max is " + dict[max]);
        	sum.push(parseInt(" " + dict[min] + dict[max]));
        }
    });
  	sum.forEach( n => {
    	realsum += n;
    });
    console.log("Sum is " + realsum);
});
