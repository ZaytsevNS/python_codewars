import unittest
import main


class TestDomainName(unittest.TestCase):
    def test_one(self):
        """ Should return the domain name """
        self.assertEqual('github', main.domain_name('http://github.com/carbonfive/raygun'))
        self.assertEqual('zombie-bites', main.domain_name('http://www.zombie-bites.com'))
        self.assertEqual('cnet', main.domain_name('https://www.cnet.com'))
        
if __name__ == '__main__':
    unittest.main()
