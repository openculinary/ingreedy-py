from ingreedypy import Ingreedy


def test_amounts():
    assert Ingreedy().parse('2 cups of potatoes')['amount'] == 2
    assert Ingreedy().parse('12345 potatoes')['amount'] == 12345
    assert Ingreedy().parse('1/2 potato')['amount'] == 0.5
    assert Ingreedy().parse('1 1/2 potatoes')['amount'] == 1.5
    assert Ingreedy().parse('5 3/4 pinches potatoes')['amount'] == 5.75
    assert Ingreedy().parse('1.5 potatoes')['amount'] == 1.5
    assert Ingreedy().parse('.5 potatoes')['amount'] == 0.5
    assert Ingreedy().parse('12oz potatoes')['amount'] == 12
    assert Ingreedy().parse("1 cup flour")['amount'] == 1
    assert Ingreedy().parse("one cup flour")['amount'] == 1
    assert Ingreedy().parse("a cup of flour")['amount'] == 1
    assert Ingreedy().parse("1 1/2 cups flour")['amount'] == 1.5
    assert Ingreedy().parse("1.0 cup flour")['amount'] == 1
    assert Ingreedy().parse("1.5 cups flour")['amount'] == 1.5
    assert Ingreedy().parse("1 2/3 cups flour")['amount'] == round(float(5.0/3), 3)
    assert Ingreedy().parse("1 (28 ounce) can crushed tomatoes")['amount'] == 28
    assert Ingreedy().parse("2 (28 ounce) can crushed tomatoes")['amount'] == 56
    assert Ingreedy().parse("3 28 ounce cans of crushed tomatoes")['amount'] == 84
    assert Ingreedy().parse("one 28 ounce can crushed tomatoes")['amount'] == 28
    assert Ingreedy().parse("two five ounce can crushed tomatoes")['amount'] == 10
    assert Ingreedy().parse("two 28 ounce cans crushed tomatoes")['amount'] == 56
    assert Ingreedy().parse("three 28 ounce cans crushed tomatoes")['amount'] == 84
    assert Ingreedy().parse("1/2 cups flour")['amount'] == 0.5
    assert Ingreedy().parse(".25 cups flour")['amount'] == 0.25
    assert Ingreedy().parse("12oz tequila")['amount'] == 12

def test_unit():
    assert Ingreedy().parse('2 cups of potatoes')['unit'] == 'cup'
    assert Ingreedy().parse('12345 potatoes')['unit'] == None
    assert Ingreedy().parse('1/2 potato')['unit'] == None
    # assert Ingreedy().parse('1 1/2 potatoes')['unit'] == None
    # assert Ingreedy().parse('5 3/4 pinches potatoes')['unit'] == 'pinch'
    # assert Ingreedy().parse('1.5 potatoes')['unit'] == None
    # assert Ingreedy().parse('.5 potatoes')['unit'] == None
    # assert Ingreedy().parse('12oz potatoes')['unit'] == None
    # assert Ingreedy().parse("1 cup flour")['unit'] == 'cup'
    # assert Ingreedy().parse("one cup flour")['unit'] == 'cup'
    # assert Ingreedy().parse("a cup of flour")['unit'] == 1
    # assert Ingreedy().parse("1 1/2 cups flour")['unit'] == 1.5
    # assert Ingreedy().parse("1.0 cup flour")['unit'] == 1
    # assert Ingreedy().parse("1.5 cups flour")['unit'] == 1.5
    # assert Ingreedy().parse("1 2/3 cups flour")['unit'] == round(float(5.0/3), 3)
    # assert Ingreedy().parse("1 (28 ounce) can crushed tomatoes")['unit'] == 28
    # assert Ingreedy().parse("2 (28 ounce) can crushed tomatoes")['unit'] == 56
    # assert Ingreedy().parse("3 28 ounce cans of crushed tomatoes")['unit'] == 84
    # assert Ingreedy().parse("one 28 ounce can crushed tomatoes")['unit'] == 28
    # assert Ingreedy().parse("two five ounce can crushed tomatoes")['unit'] == 10
    # assert Ingreedy().parse("two 28 ounce cans crushed tomatoes")['unit'] == 56
    # assert Ingreedy().parse("three 28 ounce cans crushed tomatoes")['unit'] == 84
    # assert Ingreedy().parse("1/2 cups flour")['unit'] == 0.5
    # assert Ingreedy().parse(".25 cups flour")['unit'] == 0.25
    # assert Ingreedy().parse("12oz tequila")['unit'] == 12
