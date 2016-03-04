#!/usr/bin/python
#import argparse
import json, string, sys
import utils, package


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
        with open(pkg.name + '-output.json','w') as f:
            f.write(json.dumps(pkg.data, sort_keys=True, indent=4, separators=(',', ': ')))
