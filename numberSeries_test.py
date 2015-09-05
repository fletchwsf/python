import numberSeries

def test_GCD_answer():
    assert numberSeries.GCD(12,4) == 4
    assert numberSeries.GCD(4,12) == 4
    assert numberSeries.GCD(100,50) == 50
    assert numberSeries.GCD(50,100) == 50
    assert numberSeries.GCD(1,50) == 1

def test_Pie_answer():
    # this list result comparision has a syntax error
    assert numberSeries.Pie(1) == 3
    assert numberSeries.Pie(2) == [3,1]
    assert numberSeries.Pie(3) == [3,1,4]