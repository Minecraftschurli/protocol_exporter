import re

from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode


class RemoveMagicPreprocessor(Preprocessor):
    def preprocess_cell(self, cell: NotebookNode, resources, index):
        if cell.cell_type == 'code':
            for match in re.finditer(r'^%{1,2}(?P<magic>[^ \n\t]*) (?P<parameters>.*)$', cell.source):
                magic = match.group('magic')
                parameters = match.group('parameters').split()
                resources['magics'][magic] = parameters
                cell.source = cell.source[:match.start()] + cell.source[match.end() + 1:]
        return cell, resources
