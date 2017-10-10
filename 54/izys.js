var fs = require('fs');

var chars = 'abcdefghijklmnopqrstuvwxyz';
var i = 0, str = '';

for (i=0; i<26; i++) {
  str = str + chars[i] + str;
}

fs.writeFileSync('abacaba_final.txt', str);