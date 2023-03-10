import glob
import re

plugins = 0
themes = 0
core = 0
other = 0

for file in glob.glob("./nuclei-templates/**/*.yaml"):
    with open(file) as f:
        content = f.read()

        if re.search("wp-plugin", content):
            plugins+=1
        
        if re.search("wp-theme", content):
            themes+=1

        if re.search("wp-core", content):
            core+=1

other = len(glob.glob("./nuclei-templates/*.yaml"))

table = "<!-- START: __STATISTICS_TABLE -->\n"
table += "| templates | total | |\n"
table += "|---|---|---|\n"
table += f"| plugins | {plugins} | |\n"
table += f"| themes | {themes} | |\n"
table += f"| core | {core} | |\n"
table += f"| other | {other} | |\n"
table += "<!-- END: __STATISTICS_TABLE -->"

with open("README.md", "r") as f:
    content = f.read()
    content = re.sub(r"<!-- START: __STATISTICS_TABLE -->.*<!-- END: __STATISTICS_TABLE -->", table, content, 0, re.S)
    
    with open("README.md", "w") as f2:
        f2.write(content)
        

