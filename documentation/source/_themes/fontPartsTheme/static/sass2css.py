# compile sass into css

import os
import os.path
import subprocess

# sass (CSS extension language) compiler
# http://sass-lang.com/install

def compileSass(sassPath):
    '''
    Compile a sass file (and dependencies) into a single css file.

    '''
    cssPath = os.path.splitext(sassPath)[0] + ".css"
    subprocess.call(["sass", sassPath, cssPath])

# gets path for directory of sass2css.py
baseFolder = os.path.split(os.path.abspath(__file__))[0]

for f in os.listdir(baseFolder):
    name, extension = os.path.splitext(f)

    # note: be sure that you import /partials into the the main.sass file, or code won't make it into CSS
    if extension == ".sass":
        sassPath = os.path.join(baseFolder, f)
        compileSass(sassPath)
