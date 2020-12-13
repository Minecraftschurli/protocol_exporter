import os
import os.path

from nbconvert.exporters.pdf import PDFExporter
from traitlets.config import Config


class ProtocolExporter(PDFExporter):
    """
    Protocol exporter
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "Protocol"

    def _template_data_paths_default(self):
        return super()._template_data_paths_default()+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'protocol'

    @property
    def default_config(self):
        c = super().default_config
        c.merge(Config({
            'ExecutePreprocessor': {
                'enabled': True
            },
            'TagRemovePreprocessor': {
                'enabled': True,
                'remove_all_outputs_tags': {'silent'},
                'remove_cell_tags': {'exclude'},
                'remove_input_tags': {'hidden'}
            },
            'RemoveMagicPreprocessor': {
                'enabled': True
            },
            'HighlightMagicsPreprocessor': {
                'enabled': False
            }
        }))
        return c
