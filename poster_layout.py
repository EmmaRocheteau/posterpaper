class Poster:
    def __init__(self, doc):
        self.columns = []
        self.author = ""
        self.title = ""
        self.preamble = ""
        return

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
