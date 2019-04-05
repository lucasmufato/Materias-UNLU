from SearchEngine.Configuration import Configuration
from SearchEngine.SearchEngine import SearchEngine


config = Configuration()
config.steamer = "lancaster"
config.verbose_steamer = True

se = SearchEngine(config)


se.scan_directory("archivos/")
se.armar_archivos_estadisticos()