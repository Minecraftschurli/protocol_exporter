import os
import os.path

from nbconvert.exporters.pdf import PDFExporter
from traitlets.config import Config, default


class ProtocolExporter(PDFExporter):
    """
    Protocol exporter
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "Protocol"

    @default('template_data_paths')
    def _template_data_paths_default(self):
        return super()._template_data_paths_default()+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'protocol'

    @default("default_preprocessors")
    def _default_preprocessors_default(self):
        return [
            'nbconvert.preprocessors.RegexRemovePreprocessor',
            'nbconvert.preprocessors.ClearOutputPreprocessor',
            'nbconvert.preprocessors.ExecutePreprocessor',
            'nbconvert.preprocessors.TagRemovePreprocessor',
            'nbconvert.preprocessors.coalesce_streams',
            'nbconvert.preprocessors.SVG2PDFPreprocessor',
            'nbconvert.preprocessors.LatexPreprocessor',
            'nbconvert.preprocessors.HighlightMagicsPreprocessor',
            'nbconvert.preprocessors.ExtractOutputPreprocessor',
            'nbconvert.preprocessors.ClearMetadataPreprocessor',
        ]

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
                'remove_cell_tags': {'exclude', 'run_only'},
                'remove_input_tags': {'hidden', 'output_only'}
            },
            'RemoveMagicPreprocessor': {
                'enabled': True
            },
            'HighlightMagicsPreprocessor': {
                'enabled': False
            }
        }))
        return c
