string = "aaaaa"
translate = {"a": "bc", "b": "a", "c": "aaa"}
while len(string) > 1:
	string = string[2:] + translate[string[0]]
	print(string)
