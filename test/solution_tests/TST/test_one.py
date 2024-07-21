from solutions.TST import one
from solutions.CHK.checkout_solution import checkout


class TestSum():
    def test_sum(self):
        assert one.get() == 1


class TestCheckut():
    def test_checkout(self):
        assert checkout('A') == 50
        assert checkout('B') == 30
        assert checkout('C') == 20
        assert checkout('D') == 15
        assert checkout('AA') == 100
        assert checkout('BB') == 45
        assert checkout('AAA') == 130
        assert checkout('AAAA') == 180
        assert checkout('BBB') == 75
        assert checkout('AAAA') == 180
        assert checkout('ABCD') == 115
        assert checkout('AAAB') == 160
        assert checkout('AAABB') == 175
        assert checkout('AAABBD') == 190
        assert checkout('EE') == 80
        assert checkout('EEB') == 80
        assert checkout('EEEB') == 120
        assert checkout('EEEEBB') == 160
        assert checkout('ABCDEABCDE') == 280
        assert checkout('CCADDEEBBA') == 280

    def test_checkout_f(self):
        assert checkout('F') == 10
        assert checkout('FF') == 20
        # assert checkout('FFF') == 20
        # assert checkout('FFFF') == 30
        # assert checkout('FFFFF') == 40
        # assert checkout('FFFFFF') == 40
        # assert checkout('FFFFFFF') == 50
