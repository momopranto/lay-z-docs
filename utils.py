#import argparse
import string, json
import package


def ext_of(name):
    return src.split('.')[len(src.split('.'))-1]

def LANG_ERROR(src):
    print 'Error: ' + src + ' is invalid or uses a language that is currently unsupported.'

def scan_py_dec(src):
    with open(src) as f:
        data = {'functions':[]}
        code = f.readlines()
        for line in code:
            if 'def ' in line:
                name = line.strip()[4:line.strip().find('(')]
                args = [{'name': n, 'type': None} for n in map(str.strip, line.strip()[line.strip().find('(')+1:line.strip().rfind(')')].split(','))]
                data['functions'].append({'name': name, 'return-type': None, 'args': args})
        return Package('Python', data)

def scan_c_dec(src):


def scan_js_dec(src):
