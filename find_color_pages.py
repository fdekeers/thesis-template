#!/usr/bin/env python
# author: Maxime Piraux
import os
import subprocess
import sys
import time

thesis_file = "thesis_elec.pdf"
time_modification = time.ctime(os.path.getmtime(thesis_file))
print(f"parsing content of file '{thesis_file}', modified at {time_modification}")

gs_proc = subprocess.run(['gs', '-q', '-o', '-', '-sDEVICE=inkcov', thesis_file], capture_output=True, universal_newlines=True)

color_pages = []

for i, line in enumerate(gs_proc.stdout.splitlines()):
    line_no = i + 1
    c, m, y, k, *_ = line.split()
    c, m, y, k = map(float, [c, m, y, k])
    if c or m or y:
	    color_pages.append(line_no)

print("The following pages are to be printed in color. They the page numbers on the PDF.\n")
print(*color_pages, sep=', ')
