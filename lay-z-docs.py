#!/usr/bin/python
import json, string, sys
import utils, package

# language: [definition style, comment style]
P_LANG = {
        'c':[DEF_STYLE[0],COM_STYLE[0]],
        'c++':[DEF_STYLE[0],COM_STYLE[0]],
        'c#':[DEF_STYLE[0],COM_STYLE[0]],
        'python':[DEF_STYLE[1],COM_STYLE[1]],
        'java':[DEF_STYLE[3],COM_STYLE[0]],
        'ruby':[DEF_STYLE[1],COM_STYLE[1]],
        'javascript':[DEF_STYLE[2],COM_STYLE[0]],
        'php':[DEF_STYLE[2],COM_STYLE[0]+COM_STYLE[1]]
        }
DEF_STYLE = [
        ['function identifier regex'],
        ['def'],
        ['function'],
        ['java identifier regex']
        ]
COM_STYLE = [
        ['//','/*','*/'],
        ['#'],
        ['--'],
        ]


if len(sys.argv) > 1:
    pkg = None
    targets = sys.argv[1:]
    for src in targets:
        ext = utils.ext_of(src)
        if ext == 'py':
            pkg = utils.scan_py_dec(src)
        elif ext == 'c':
            pkg = utils.scan_c_dec(src)
        elif ext == 'js':
            pkg = utils.scan_js_dec(src)
        else:
            LANG_ERROR(src)
    if pkg:
        #do stuff
