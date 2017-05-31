let string = "aaaaa";
let translate = {
	"a": "bc",
	"b": "a",
	"c": "aaa"
};
while (string.length > 1) {
	string = string.substr(2) + translate[string.charAt(0)];
	console.log(string);
}