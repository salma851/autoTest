from calcule import addition, multiplication, dividion
import pytest

def test_addition():
   assert addition(2,3) == 5
def test_multiplication():
   assert multiplication(4,3)==12   
def test_division():
   assert dividion(10,2)==5
def test_division_par_zero():
   with pytest.raises(ValueError):
      dividion(10,0)