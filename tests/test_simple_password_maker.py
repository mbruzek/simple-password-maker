import unittest
import sys
from os import path
# Have to append the system path because this test is not a module.
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.SimplePasswordMaker import SimplePasswordMaker


# Test all the hash algorithms in standard python.
ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
CHARSET = SimplePasswordMaker.CHARSET
HEX_CHARS = '0123456789ABCDEF'


class TestPasswordMaker(unittest.TestCase):

    def test_algortihms(self):
        """Test each algorithm with empty data, 8 length, default charset."""
        expected = {
            ALGORITHMS[0]: 'YdudxA[E',
            ALGORITHMS[1]: 'e5(yAN.N',
            ALGORITHMS[2]: 'V-Cuq6rN',
            ALGORITHMS[3]: 'n?I%6#cU',
            ALGORITHMS[4]: '4?C,>;44',
            ALGORITHMS[5]: 'Tll1gz{B'
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            result = maker.generate_password(algorithm, '', '', '8', CHARSET)
            assert result == expected[algorithm], '%s failed' % algorithm

    def test_hexadecimal(self):
        """Test each algorithm with empty data, 9 length, hex charset."""
        expected = {
            ALGORITHMS[0]: '4DC9F0249',
            ALGORITHMS[1]: 'A93EEBBD2',
            ALGORITHMS[2]: '1A2CAAB97',
            ALGORITHMS[3]: '30428CC4A',
            ALGORITHMS[4]: '80071C68C',
            ALGORITHMS[5]: 'F315EF8D1'
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            result = maker.generate_password(algorithm, '', '', '9', HEX_CHARS)
            assert result == expected[algorithm], '%s failed' % algorithm

    def test_data(self):
        """Test with iterations of the data, ensure the passwords match."""
        expected = {
            ALGORITHMS[0]: 'm#T/*ny133',
            ALGORITHMS[1]: 'j%t%p^O!Pi',
            ALGORITHMS[2]: ',I[cn\O8tJ',
            ALGORITHMS[3]: 'qYmRYqzvT{',
            ALGORITHMS[4]: 'RH\#R0^q9k',
            ALGORITHMS[5]: 'cCvgC<Q$pc'
        }
        maker = SimplePasswordMaker()
        for algorithm in ALGORITHMS:
            one = maker.generate_password(algorithm, 'abcd', '', '10', CHARSET)
            assert one == expected[algorithm], '1. Mismatch %s != %s' % \
                (one, expected[algorithm])
            two = maker.generate_password(algorithm, '', 'abcd', '10', CHARSET)
            assert one == two, '2. Mismatch %s != %s' % (one, two)
            three = maker.generate_password(algorithm, 'ab', 'cd', '10', CHARSET)  # noqa
            assert one == three, '3. Mismatch %s != %s' % (one, three)


if __name__ == '__main__':
    unittest.main()
