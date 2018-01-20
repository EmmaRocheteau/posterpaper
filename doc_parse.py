# Class definitions for the document model. The document class must be article
class Document:
    def __init__(self, src):
        self.sections = []
        self.graphics = []
        self.preamble = ""
        self.title = ""
        self.authors = ""
        self.abstract = ""
        return

    def _parseSource(self, src):
        return

    def _cleanInput(self):
        return

class Section:
    def __init__(self):
        self.subsections = []
        self.content = ""
        self.name = ""
        return

class Subsection:
    def __init__(self):
        self.subsubsections = []
        self.content = ""
        self.name = ""

class Subsubsection:
    def __init__(self):
        self.content = ""
        self.name = ""

class Graphic:
    def __init__(self):
        self.content = ""
        self.section_name = ""
        self.name = ""