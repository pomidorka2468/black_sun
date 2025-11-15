import re

input_text = open("input.txt", encoding="utf-8").read()
matches = re.findall(r"### Sektion (\d+) ###\n(.+?)\n{2}", input_text, re.DOTALL)

sections = []
for match_array in matches:
    section = {}
    section["number"] = match_array[0]
    section["text"] = match_array[1]
    section["next_section"] = "placeholder"
    sections.append(section)

print (sections)