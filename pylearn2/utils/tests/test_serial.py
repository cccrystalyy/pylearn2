import pylearn2
from pylearn2.utils.serial import read_bin_lush_matrix
import numpy as np

pylearn2_path = pylearn2.__path__[0]
example_bin_lush_path = pylearn2_path + '/utils/tests/example_bin_lush/'

def test_read_bin_lush_matrix_ubyte_scalar():
    #note: this is what happens when you write a scalar from
    #koray's matlab code which always makes everything 3D
    #writing it straight from lush you might be able to get a true scalar
    path = example_bin_lush_path + 'ubyte_scalar.lushbin'
    result = read_bin_lush_matrix(path)

    assert str(result.dtype) == 'uint8'
    assert len(result.shape) == 3
    assert result.shape[0] == 1
    assert result.shape[1] == 1
    assert result.shape[1] == 1
    assert result[0,0] == 12

def test_read_bin_lush_matrix_ubyte_3tensor():

    path = example_bin_lush_path + 'ubyte_3tensor.lushbin'
    result = read_bin_lush_matrix(path)

    assert str(result.dtype) == 'uint8'

    assert len(result.shape) == 3
    if result.shape != (2,3,4):
        raise AssertionError("ubyte_3tensor.lushbin stores a 3-tensor "
            "of shape (2,3,4), but read_bin_lush_matrix thinks it has "
            "shape "+str(result.shape))

    for i in xrange(1,3):
        for j in xrange(1,4):
            for k in xrange(1,5):
                assert result[i-1,j-1,k-1] == i + 3*j + 12*k


def test_read_bin_lush_matrix_int_3tensor():

    path = example_bin_lush_path + 'int_3tensor.lushbin'
    result = read_bin_lush_matrix(path)

    assert str(result.dtype) == 'int32'

    assert len(result.shape) == 3
    if result.shape != (3,2,4):
        raise AssertionError("ubyte_3tensor.lushbin stores a 3-tensor "
            "of shape (3,2,4), but read_bin_lush_matrix thinks it has "
            "shape "+str(result.shape))

    for i in xrange(1,result.shape[0]+1):
        for j in xrange(1,result.shape[1]+1):
            for k in xrange(1,result.shape[2]+1):
                assert result[i-1,j-1,k-1] == (i + 10000 ** j) * ( (-2)** k)


def test_read_bin_lush_matrix_float_3tensor():

    path = example_bin_lush_path + 'float_3tensor.lushbin'
    result = read_bin_lush_matrix(path)

    assert str(result.dtype) == 'float32'

    assert len(result.shape) == 3
    if result.shape != (4,3,2):
        raise AssertionError("ubyte_3tensor.lushbin stores a 3-tensor "
            "of shape (4,3,2), but read_bin_lush_matrix thinks it has "
            "shape "+str(result.shape))

    for i in xrange(1,result.shape[0]+1):
        for j in xrange(1,result.shape[1]+1):
            for k in xrange(1,result.shape[2]+1):
                assert np.allclose(result[i-1,j-1,k-1], i + 1.5 * j + 1.7 * k)


def test_read_bin_lush_matrix_double_3tensor():

    path = example_bin_lush_path + 'double_3tensor.lushbin'
    result = read_bin_lush_matrix(path)

    assert str(result.dtype) == 'float64'

    assert len(result.shape) == 3
    if result.shape != (4,2,3):
        raise AssertionError("ubyte_3tensor.lushbin stores a 3-tensor "
            "of shape (4,2,3), but read_bin_lush_matrix thinks it has "
            "shape "+str(result.shape))

    for i in xrange(1,result.shape[0]+1):
        for j in xrange(1,result.shape[1]+1):
            for k in xrange(1,result.shape[2]+1):
                assert np.allclose(result[i-1,j-1,k-1], i + 1.5 * j + (-1.7) ** k)
