from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    triple_flour = flour.times(3)
    assert triple_flour.amount == 600
    assert flour.amount == 200  # Original remains unchanged

def test_multiplication_by_two():
    flour = Quantity(200)
    double_flour = flour.times(2)
    assert double_flour.amount == 400

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400