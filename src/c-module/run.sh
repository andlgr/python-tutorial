#!/bin/bash

gcc -fPIC -shared module.c -o module.so
python3 module.py
