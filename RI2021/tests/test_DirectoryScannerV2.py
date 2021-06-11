from unittest import TestCase
from unittest.mock import Mock

from SE.io.DirectoryScannerV2 import DirectoryScannerV2


class TestDirectoryScannerV2(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.processor = Mock()
        self.engine: DirectoryScannerV2 = DirectoryScannerV2(self.processor)

    def test_reads_all_files(self):
        self.engine.scan_directory("files/", )
        self.processor.process_file.assert_any_call("files/one.txt", 'This is an example of a text containing from simple acronyms like N.A.S.A., other like countries as Colombia, Chile or their abreviations as Arg. Uy.\nmore people as Lucas like to travel, since 11/4/1992 when he was born in Lujàn he traveled like 10 times in 5 years, reaching many many many places.')
        self.processor.process_file.assert_any_call('files/two.txt', 'Esto es un texto en castellano el cual contiene un conjunto pequeño con algun caracter raro. Ojo con la diferencia entre character del ingles y caracter del castellano.\nAca se vienen un par de nombres personales como Lucas Mufato que trabaja como software engineer en Etermax y Micaela Guerrero que trabaja en Freevoices')
        self.processor.process_file.assert_any_call("files/three.txt", """this is a very very very short text text\nthat is not long\n""")
