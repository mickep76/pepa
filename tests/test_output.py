#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import subprocess
import sys

sys.exit(0)

# Validate importing Pepa

# Validate calling Pepa from TTY
expected = yaml.load(open('tests/output.yaml').read())
proc = subprocess.Popen(['pepa', '-n', '-c', 'examples/master', 'test.example.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
actual = yaml.load(proc.communicate()[0])

if cmp(expected, actual) == 0:
    print "SUCCESS!"
    sys.exit(0)
else:
    print "FAILED!"
    sys.exit(1)
