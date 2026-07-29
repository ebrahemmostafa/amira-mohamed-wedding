import os

filepath = 'css/typekit-dup6afg.css'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

imports = []
other_lines = []

for line in lines:
    if line.strip().startswith('@import'):
        imports.append(line)
    else:
        other_lines.append(line)

# Remove duplicate imports
unique_imports = []
for imp in imports:
    if imp not in unique_imports:
        unique_imports.append(imp)

new_content = ''.join(unique_imports) + '\n' + ''.join(other_lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed CSS imports order.")
