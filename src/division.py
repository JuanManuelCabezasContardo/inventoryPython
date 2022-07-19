

def make_division_by(n):
    """
        this closure returns a function that returns the division
        of a x number by n
    """
    assert (type(n) == int or type(n) == float ) , "solo puedes usar numeros"
    def division(x):
        assert (type(x) == int or type(x) == float ) , "solo puedes usar numeros"
        return x/n
    
    return division

division_by_3 =make_division_by("A")
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by(18)
print(division_by_18(54))
