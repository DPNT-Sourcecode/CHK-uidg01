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
        assert checkout('BBB') == 75
        assert checkout('AAAA') == 180
        assert checkout('ABCD') == 115
        assert checkout('AAAB') == 160
        assert checkout('AAABB') == 175
        assert checkout('AAABBD') == 190


