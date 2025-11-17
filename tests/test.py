import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from lab6 import arrays, total_displacement

@pytest.fixture
def get_results_1():
    test_1_out_array1 = np.float64(np.loadtxt("tests/array1.txt",delimiter=","))
    test_1_out_array2 = np.float64(np.loadtxt("tests/array2.txt",delimiter=","))
    test_1_out_array3 = np.float64(np.loadtxt("tests/array3.txt",delimiter=","))
    test_1_out_array4 = np.float64(np.loadtxt("tests/array4.txt",delimiter=","))
    test_1_out_array5 = np.float64(np.loadtxt("tests/array5.txt",delimiter=","))
    test_1_out_array6 = np.float64(np.loadtxt("tests/array6.txt",delimiter=","))
    test_1_out_array7 = np.float64(np.loadtxt("tests/array7.txt",delimiter=","))
    test_1_out_array8 = np.float64(np.loadtxt("tests/array8.txt",delimiter=","))
    test_1_out_array9 = np.float64(np.loadtxt("tests/array9.txt",delimiter=","))
    test_1_out_array10 =np.float64(np.loadtxt("tests/array10.txt",delimiter=","))                            
    return test_1_out_array1, test_1_out_array2, test_1_out_array3, test_1_out_array4, test_1_out_array5, test_1_out_array6, test_1_out_array7, test_1_out_array8, test_1_out_array9, test_1_out_array10 


@pytest.fixture
def get_results_2():
    test_2_in = np.float64(np.loadtxt("tests/test_in.txt", delimiter=","))
    test_2_out = np.float64(np.loadtxt("tests/test_out.txt", delimiter=","))
    return test_2_in, test_2_out


def test_array1(get_results_1):
    test_out = get_results_1

    true_array1 = test_out[0]
    
    res = arrays()[0]
    
    assert np.array_equal(true_array1, res)

    
def test_array2(get_results_1):
    test_out = get_results_1

    true_array2 = test_out[1]

    res = arrays()[1]
    
    assert np.array_equal(true_array2, res)

    
def test_array3(get_results_1):
    test_out = get_results_1

    true_array3 = test_out[2]

    res = arrays()[2]
    
    assert np.array_equal(true_array3, res)

    
def test_array4(get_results_1):
    test_out = get_results_1

    true_array4 = test_out[3]

    res = arrays()[3]
    
    assert np.array_equal(true_array4, res)

    
def test_array5(get_results_1):
    test_out = get_results_1

    true_array5 = test_out[4]

    res = arrays()[4]
    
    assert np.array_equal(true_array5, res)

    
def test_array6(get_results_1):
    test_out = get_results_1

    true_array6 = test_out[5]

    res = arrays()[5]
    
    assert np.array_equal(true_array6, res)

    
def test_array7(get_results_1):
    test_out = get_results_1

    true_array7 = test_out[6]

    res = arrays()[6]
    
    assert np.array_equal(true_array7, res)

    
def test_array8(get_results_1):
    test_out = get_results_1

    true_array8 = test_out[7]

    res = arrays()[7]
    
    assert np.array_equal(true_array8, res)

    
def test_array9(get_results_1):
    test_out = get_results_1

    true_array9 = test_out[8]

    res = arrays()[8]
    
    assert np.array_equal(true_array9, res)

    
def test_array10(get_results_1):
    test_out = get_results_1

    true_array10 = test_out[9]

    res = arrays()[9]
    
    assert np.array_equal(true_array10, res)
    
    
def test_2_values_arr(get_results_2):
    "x component"
    test_in = get_results_2[0]
    test_out = get_results_2[1]

    test_v1x = test_in[0]
    test_v1y = test_in[1]
    test_v2x = test_in[2]
    test_v2y = test_in[3]
    test_v3x = test_in[4]
    test_v3y = test_in[5]

    test_vRx = test_out[:,0]
    test_vRy = test_out[:,1]
    test_vRul = test_out[:,2]
    
    for i in range(4):
        res = total_displacement(test_v1x[i],
                                 test_v1y[i],
                                 test_v2x[i],
                                 test_v2y[i],
                                 test_v3x[i],
                                 test_v3y[i])
        
        true_vRx = test_vRx[i]
        true_vRy = test_vRy[i]
        true_vRul = test_vRul[i]

        assert res[0][0] == true_vRx


def test_3_values_arr(get_results_2):
    "y component"
    test_in = get_results_2[0]
    test_out = get_results_2[1]

    test_v1x = test_in[0]
    test_v1y = test_in[1]
    test_v2x = test_in[2]
    test_v2y = test_in[3]
    test_v3x = test_in[4]
    test_v3y = test_in[5]

    test_vRx = test_out[:,0]
    test_vRy = test_out[:,1]
    test_vRul = test_out[:,2]
    
    for i in range(4):
        res = total_displacement(test_v1x[i],
                                 test_v1y[i],
                                 test_v2x[i],
                                 test_v2y[i],
                                 test_v3x[i],
                                 test_v3y[i])
        
        true_vRx = test_vRx[i]
        true_vRy = test_vRy[i]
        true_vRul = test_vRul[i]

        assert res[0][1] == true_vRy

def test_4_values_arr(get_results_2):
    "length"
    test_in = get_results_2[0]
    test_out = get_results_2[1]

    test_v1x = test_in[0]
    test_v1y = test_in[1]
    test_v2x = test_in[2]
    test_v2y = test_in[3]
    test_v3x = test_in[4]
    test_v3y = test_in[5]

    test_vRx = test_out[:,0]
    test_vRy = test_out[:,1]
    test_vRul = test_out[:,2]
    
    for i in range(4):
        res = total_displacement(test_v1x[i],
                                 test_v1y[i],
                                 test_v2x[i],
                                 test_v2y[i],
                                 test_v3x[i],
                                 test_v3y[i])
        
        true_vRx = test_vRx[i]
        true_vRy = test_vRy[i]
        true_vRul = test_vRul[i]


        assert res[1] == true_vRul
        
