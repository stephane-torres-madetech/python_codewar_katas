from ..codewar_problems.bmi import  bmi

def test_bmi_returns_correct_string():
    assert(bmi(50, 1.8)) == "Underweight"
    assert(bmi(80, 1.8)) == "Normal"
    assert(bmi(90, 1.8)) == "Overweight"
    assert(bmi(110, 1.8)) == "Obese"
    assert(bmi(50, 1.5)) == "Normal"
    