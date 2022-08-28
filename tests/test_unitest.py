import unittest
from unittest import result
from app import *
from tasks import *
# 下面為TASK測試目前除了進度以外其他都能正常測試


class TestTaskMethods(unittest.TestCase):

    def test_text(self):
        self.assertEqual(text('foo'), 'foo')

    def test_add(self):
        expected = 1225  # 1~49
        result = add(0)
        self.assertEqual(expected, result)

    def test_upload(self):
        result = upload.apply("c")
        self.assertEqual(result.state, "SUCCESS")

    def test_task_regester(self):
        self.assertEqual(task_regester('input_test'), 'success')


#
if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity=2為測試訊息結果的訊息複雜訊息，輸出完整訊息
