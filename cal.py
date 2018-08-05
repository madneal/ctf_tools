#!/usr/bin/env python3
import cgi;
import sys
from html import escape
from secret import get_flag

OK_200 = """Content-type: text/html

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<center>
<title>Calculate</title>
<h1>Calculate</h1>
<form>
<input class="form-control col-md-4" type=text name=t placeholder='Input your team token' %s />
<input class="form-control col-md-4" type=text name=value1 placeholder='Value 1 (Example: 1  abc)' />
<input class="form-control col-md-4" type=text name=op placeholder='Operator (Example: + - * ** / // == != )' />
<input class="form-control col-md-4" type=text name=value2 placeholder='Value 2 (Example: 1  abc)' />
<input class="form-control col-md-4 btn btn-success" type=submit value=EVAL />
</form>
<a href='?%ssource=1'>Source</a>
</center>
"""

arguments = cgi.FieldStorage()
if 't' in arguments:
    token = str(arguments['t'].value)
    print(OK_200 % ("value="+token+' readonly', "t="+token+"&"))
else:
    print(OK_200 % ("", ""))

if 'source' in arguments:
    source = arguments['source'].value
else:
    source = 0

if source == '1':
    print('<pre>'+escape(str(open(__file__,'r').read()))+'</pre>')

if 'value1' in arguments and 'value2' in arguments and 'op' in arguments and 't' in arguments:

    FLAG = 'flag{' + get_flag(arguments['t'].value) + '}'

    def get_value(val):
        val = str(val)[:64]
        if str(val).isdigit(): return int(val)
        blacklist = ['(',')','[',']','\'','"'] # I don't like tuple, list and dict.
        if val == '' or [c for c in blacklist if c in val] != []:
            print('<center>Invalid value</center>')
            sys.exit(0)
        return val

    def get_op(val):
        val = str(val)[:2]
        list_ops = ['+','-','/','*','=','!']
        if val == '' or val[0] not in list_ops:
            print('<center>Invalid op</center>')
            sys.exit(0)
        return val

    op = get_op(arguments['op'].value)
    value1 = get_value(arguments['value1'].value)
    value2 = get_value(arguments['value2'].value)

    if str(value1).isdigit() ^ str(value2).isdigit():
        print('<center>Types of the values don\'t match</center>')
        sys.exit(0)

    calc_eval = str(repr(value1)) + str(op) + str(repr(value2))

    print('<div class=container><div class=row><div class=col-md-2></div><div class="col-md-8"><pre>')
    print('>>>> print('+escape(calc_eval)+')')

    try:
        result = str(eval(calc_eval))
        if result.isdigit() or result == 'True' or result == 'False':
            print(result)
        else:
            print("Invalid") # Sorry we don't support output as a string due to security issue.
    except:
        print("Invalid")


    print('>>> </pre></div></div></div>')