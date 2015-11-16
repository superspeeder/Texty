import os
import texty
import unittest
import tempfile

class TextyTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, texty.app.config['DATABASE'] = tempfile.mkstemp()
        texty.app.config['TESTING'] = True
        self.app = texty.app.test_client()
        texty.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(texty.app.config['DATABASE'])
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data
if __name__ == '__main__':
    unittest.main()
