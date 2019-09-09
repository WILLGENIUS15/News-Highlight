import unittest
from app.models import newsarticle

class newsarticleTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        Setup method that will run before every test
        '''
        self.new_article = newsarticle('bbc','bbc','silah koskei','Trump','Trump takes on swearing in of Kenya oposition leader',
                                    'www.bbc.com/kenya','www.bbc.com/kenya/image.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
