class Poster:
    def __init__(self, doc):
        self.columns = []
        self.author = ""
        self.title = ""
        self.preamble = ""
        self.boxes = []
        self._makeBoxes()
        self._makeColumns()
        return

    def _makeBoxes(self, doc):
        box = Box()
        box.title = "Abstract"
        box.reference = "section0"
        box.content = doc.abstract
        self.boxes.append(box)
        for i, section in enumerate(doc.sections):
            if section.include is True:
                box = Box()
                box.figures = section.figures
                box.content = section.content
                box.title = section.title
                box.reference = "section" + str(i+1)
                self.boxes.append(box)
        return

    def _makeColumns(self, doc):
        

class Columns:
    def __init__(self):
        self.boxes = []
        return

class Box:
    def __init__(self):
        self.figures = []
        self.content = ""
        self.title = ""
        self.reference = ""
        return
