# This file is the main one...

# Read in the latex file and parse it

class document:
    def __init__(self):
        self.sections = []
        self.graphics = []
        self.preamble = ""
        return

class section:
    def __init__(self):
        self.subsections = []
        self.content = ""
        return

class subsection:
    def __init__(self):
        self.subsubsections = []
        self.content = ""

class subsubsection:
    def __init__(self):
        self.content = ""

class graphic:
    def __init__(self):
        self.content = ""


