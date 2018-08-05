import uncompyle6
import py_compile

def compile(py_file):
    py_compile.compile(py_file)


def decompile(pyc_file):
    

if __name__ == '__main__':
    compile('./pyc_reverse.py')
