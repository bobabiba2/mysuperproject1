import script10

class Test_adder:
    def test_sum_4_5_6_7(self):
        assert script10.adder(4,5,6,7) == 22
    def test_sum_1_2_3_5_6(self):
        assert script10.adder(1,2,3,5,6) == 17
    def test_sum_1_2_3_4_5(self):
        assert script10.adder(1,2,3,4,5) == 15
        