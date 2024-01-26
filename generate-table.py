#!/usr/bin/env python3

import os
import re

# Assuming the script is being run from the content/docs/tutorials/ directory
directory = 'content/docs/tutorials'
files = os.listdir(directory)

table = []
for file in sorted(files):
    if file.endswith('.md'):
        with open(f"{directory}/{file}", 'r') as f:
            content = f.read()
            title_search = re.search(r"title:\s*(.*)\n", content)
            if title_search:
                title = title_search.group(1)
                if title != "Tutorials":
                    table.append(f"[{title}](/docs/tutorials/{file.replace('.md', '')})")

table.sort()
                    
output = "|||\n|-|-|-|\n"
for i in range(0, len(table), 3):
    output += '|'.join(table[i:i+3]) + '|\n'

with open("content/docs/introduction/_table.md", 'w') as f:
    f.write(output)
