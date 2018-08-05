var arr= [45,45,32,46,46,45,32,45,46,32,46,45,32,46,46,45,46,32,46,46,45,32,45,46,46,46,32,46,46,46,46,32,45,46,45,32,46,46,46,45,32,46,45,32,45,32,45,45,46,45,32,45,46,46,46,32,46,45,32,45];

var result = []
arr.forEach(function(ele) {
    if (ele == 45) {
        result += '-';
    } else if (ele == 46) {
        result += '.';
    } else if (ele == 32) {
        result += ' ';
    } else {
        console.log('has not found' + ele);
    }
})

result = result.split(' ');
dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.'
        };
var str = '';
for (var i = 0; i < result.length; i++) {
    var ele = result[i];
    str += dict[ele];
}
console.log(str)