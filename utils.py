import string, json, re
from package import Package


def ext_of(name):
    return name.split('.')[len(name.split('.'))-1]

def name_of(name):
    return name.split('.')[0]

def LANG_ERROR(src):
    print 'Error: ' + src + ' is invalid or uses a language that is currently unsupported.'

def scan_py_dec(src):
    with open(src) as f:
        data = {'functions':[]}
        code = f.readlines()
        filename = name_of(src)
        for line in code:
            if re.match('^def ', line):
                name = line.strip()[4:line.strip().find('(')]
                args = [{'name': n, 'type': None, 'default': r} for n,r in map(lambda n : (n.split('=')[0].strip(),n.split('=')[1].strip()) if '=' in n else (n,None), map(str.strip, line.strip()[line.strip().find('(')+1:line.strip().rfind(')')].split(',')))]
                data['functions'].append({'name': name, 'return-type': None, 'args': args})
        return Package('Python', data, filename)

def scan_js_dec(src):
    with open(src) as f:
        data = {'functions':[]}
        code = f.readlines()
        filename = name_of(src)
        for line in code:
            if re.match('^function ', line):
                name = line.strip()[4:line.strip().find('(')]
                args = [{'name': n, 'type': None, 'default': r} for n,r in map(lambda n : (n.split('=')[0].strip(),n.split('=')[1].strip()) if '=' in n else (n,None), map(str.strip, line.strip()[line.strip().find('(')+1:line.strip().rfind(')')].split(',')))]
                data['functions'].append({'name': name, 'return-type': None, 'args': args})
        return Package('JavaScript', data, filename)

def scan_c_dec(src):
    return None
