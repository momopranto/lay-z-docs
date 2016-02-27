#!/usr/bin/python
import json, string

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
