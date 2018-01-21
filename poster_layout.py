class Poster:
    def __init__(self, doc):
        self.columns = []
        self.author = ""
        self.title = ""
        self.preamble = ""
        self.boxes = []
        self._makeBoxes(doc)
        self.total_char_count = self._charCount()
        self.text_space = self._textSpace()
        self._makeColumns(doc)
        return

    def _makeBoxes(self, doc):
        box = Box(doc)
        box.title = "Abstract"
        box.reference = "section0"
        box.content = doc.abstract
        box.char_count = len(doc.abstract)
        self.boxes.append(box)
        for i, section in enumerate(doc.sections):
            if section.include is True:
                box = Box(doc)
                box.figures = section.figures
                box.content = section.content
                box.title = section.name
                box.char_count = section.char_count
                box.reference = "section" + str(i+1)
                self.boxes.append(box)
        return

    def _charCount(self):
        cumulative_char_count = 0
        for box in self.boxes:
            cumulative_char_count += box.char_count
        return cumulative_char_count

    def _textSpace(self):
        cumulative_space_taken = 0
        for box in self.boxes:
            cumulative_space_taken += box.size_without_text
        return 632 * 3 - cumulative_space_taken

    def _makeColumns(self, doc):
        self.columns = [Column(), Column(), Column()]
        for box in self.boxes:
            box.sizeOfText(self.total_char_count, self.text_space)
            box.totalSize()

        #Add correct number of boxes to first column
        count = 0
        size_one_before = 0
        while self.columns[0].cumulative_size < 632:
            size_one_before = self.columns[0].cumulative_size
            self.columns[0].cumulative_size += self.boxes[count].total_size
            count += 1

        if (self.columns[0].cumulative_size - 632) > 632 - size_one_before:
            for i in range(count):
                self.columns[0].boxes.append(self.boxes[i])
                self.columns[0].column_size = self.columns[0].cumulative_size
        else:
            for i in range(count - 1):
                self.columns[0].boxes.append(self.boxes[i])
                self.columns[0].column_size = size_one_before

        self.columns[0].number_of_boxes = len(self.columns[0].boxes)

        #Add correct number of boxes to second column
        box_number = self.columns[0].number_of_boxes
        count = 0
        size_one_before = 0
        while self.columns[1].cumulative_size < 632:
            size_one_before = self.columns[1].cumulative_size
            self.columns[1].cumulative_size += self.boxes[box_number].total_size
            count += 1
            box_number += 1

        if (self.columns[1].cumulative_size - 632) > 632 - size_one_before:
            for i in range(count):
                self.columns[1].boxes.append(self.boxes[i + self.columns[0].number_of_boxes])
                self.columns[1].column_size = self.columns[1].cumulative_size
        else:
            for i in range(count - 1):
                self.columns[1].boxes.append([i + self.columns[0].number_of_boxes])
                self.columns[1].column_size = size_one_before

        #Add correct number of boxes to third column
        box_number = self.columns[0].number_of_boxes + self.columns[1].number_of_boxes
        count = 0
        size_one_before = 0
        while self.columns[2].cumulative_size < 632:
            size_one_before = self.columns[2].cumulative_size
            self.columns[2].cumulative_size += self.boxes[box_number].total_size
            count += 1
            box_number += 1

        if (self.columns[2].cumulative_size - 632) > 632 - size_one_before:
            for i in range(count):
                self.columns[2].boxes.append(self.boxes[i + self.columns[0].number_of_boxes + self.columns[1].number_of_boxes])
                self.columns[2].column_size = self.columns[2].cumulative_size
        else:
            for i in range(count - 1):
                self.columns[2].boxes.append([i + self.columns[0].number_of_boxes + self.columns[1].number_of_boxes])
                self.columns[2].column_size = size_one_before
        return


class Column:
    def __init__(self):
        self.boxes = []
        self.cumulative_size = 0
        self.column_size = 0
        self.number_of_boxes = 0
        return

class Box:
    def __init__(self, doc):
        self.figures = []
        self.content = ""
        self.title = ""
        self.reference = ""
        self.char_count = 0
        self.size_without_text = 0
        self.size_of_text = 0
        self.total_size = 0
        self._sizeWithoutText(doc)
        return

    def _sizeWithoutText(self, doc):
        figure_space = 0
        for figure in self.figures:
            if figure.include is True:
                figure_space += 0.9 * 325 * figure.height + 20 #20 is an approximation of the caption size
        self.size_without_text = 9 + 16 + figure_space
        return

    def sizeOfText(self, total_char_count, text_space):
        self.size_of_text = (self.char_count / total_char_count) * text_space
        return

    def totalSize(self):
        self.total_size = self.size_of_text + self.size_without_text
        return