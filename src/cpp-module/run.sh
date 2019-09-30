#!/bin/bash

cmake -H. -Bbuild && cmake --build build
python3 module.py
