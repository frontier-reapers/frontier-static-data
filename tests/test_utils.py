import sys
import os
import unittest

sys.path.insert(1, './static_data/')

import utils

class TestUtils(unittest.TestCase):

    def test_get_index_files(self):
        indexFiles = utils.get_index_files()
        self.assertEqual(len(indexFiles), 2)

    def test_find_resfile(self):
        indexFiles = list()
        indexFiles.append('res_index1')
        indexFiles.append('res_index2')

        testData = os.path.join(os.getcwd(), './tests/test_data')

        result = utils.find_resfile(testData, 'res:test1', indexFiles)
        self.assertEqual(result.res, '9a/9a04912e76b0add4_2bc9040fc690a2509cfb0d9ddbeacd11')
        self.assertEqual(result.index, 'res_index1')

    def test_find_resfile_second_file(self):
        indexFiles = list()
        indexFiles.append('res_index1')
        indexFiles.append('res_index2')

        testData = os.path.join(os.getcwd(), './tests/test_data')

        result = utils.find_resfile(testData, 'res:test2', indexFiles)
        self.assertEqual(result.res, '9b/9b2a8aee52be2cb6_006b54687f9d4f70c47ace00247d5405')
        self.assertEqual(result.index, 'res_index2')

    def test_find_resfile_no_match(self):
        indexFiles = list()
        indexFiles.append('res_index1')

        testData = os.path.join(os.getcwd(), './tests/test_data')

        result = utils.find_resfile(testData, 'res:nothing_at_all', indexFiles)
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()
