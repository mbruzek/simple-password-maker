import unittest
import sys
from os import path
# Have to append the system path because this test is no a module.
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.SimplePasswordMaker import SimplePasswordMaker


ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
CHARSET = SimplePasswordMaker.CHARSET
HEX_CHARS = '0123456789ABCDEF'


class TestPasswordMaker(unittest.TestCase):

    def test_algortihms(self):
        '''Test each algorithm with empty data, 10 length, default charset.'''
        expected = {
            ALGORITHMS[0]: 'YdudxA[Eti',
            ALGORITHMS[1]: 'e5(yAN.Ny\\',
            ALGORITHMS[2]: 'V-Cuq6rN*D',
            ALGORITHMS[3]: 'n?I%6#cU8"',
            ALGORITHMS[4]: '4?C,>;44/d',
            ALGORITHMS[5]: 'Tll1gz{B1['
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            result = maker.generate_password(algorithm, '', '', '10', CHARSET)
            assert result == expected[algorithm], '%s failed' % algorithm

    def test_hexadecimal(self):
        '''Test each algorithm with empty data, 11 length, hex charset.'''
        expected = {
            ALGORITHMS[0]: '4DC9F024909',
            ALGORITHMS[1]: 'A93EEBBD25F',
            ALGORITHMS[2]: '1A2CAAB9712',
            ALGORITHMS[3]: '30428CC4AB4',
            ALGORITHMS[4]: '80071C68C92',
            ALGORITHMS[5]: 'F315EF8D148'
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            result = maker.generate_password(algorithm, '', '', '11', HEX_CHARS)
            assert result == expected[algorithm], '%s failed' % algorithm

    def test_data(self):
        '''Test with iterations of the data, the passwords match.'''
        expected = {
            ALGORITHMS[0]: 'm#T/*ny133kRuhzf',
            ALGORITHMS[1]: 'j%t%p^O!Pi%Rw^mV',
            ALGORITHMS[2]: ',I[cn\O8tJ%y_Kdi',
            ALGORITHMS[3]: 'qYmRYqzvT{(#2r^"',
            ALGORITHMS[4]: 'RH\#R0^q9kUfa[EO',
            ALGORITHMS[5]: 'cCvgC<Q$pc`9Q@\N'
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            one = maker.generate_password(algorithm, 'abcd', '', '16', CHARSET)
            assert one == expected[algorithm], '%s test failed.' % algorithm
            two = maker.generate_password(algorithm, '', 'abcd', '16', CHARSET)
            assert one == two, 'Mismatch %s != %s' % (one, two)
            three = maker.generate_password(algorithm, 'ab', 'cd', '16', CHARSET)
            assert one == three, 'Mismatch %s != %s' % (one, three)


if __name__ == '__main__' and __package__ is None:
    unittest.main()


