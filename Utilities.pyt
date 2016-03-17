from lib.Sitemap_Tool import SiteMapGenerator
from lib.Data_Updater import MultipleLayerUpdater
class Toolbox(object):
    def __init__(self):
        self.label = 'Mapping Toolbox'
        self.alias = 'Mapping'
        self.tools = [SiteMapGenerator, MultipleLayerUpdater]