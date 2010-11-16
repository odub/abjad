import py.test
from abjad.tools.treetools.BoundedInterval import BoundedInterval


def test_BoundedInterval___init____01( ):
    '''High value must be greater than or equal to low value.'''
    py.test.raises(AssertionError,
        "i = BoundedInterval(0, -10, 'this should fail.')")

def test_BoundedInterval___init____02( ):
    '''BoundedIntervals cannot be instantiated from floats.'''
    py.test.raises(AssertionError,
        "i = BoundedInterval(0.5, 2.3, 'this should fail.')")

def test_BoundedInterval___init____03( ):
    '''BoundedIntervals can be instantiated from other intervals.'''
    i1 = BoundedInterval(0, 10, 'data')
    i2 = BoundedInterval(i1)
    assert i1.signature == i2.signature
    assert i1 != i2

def test_BoundedInterval___init____04( ):
    '''BoundedIntervals can be instantiated with just a low and high value.'''
    i = BoundedInterval(0, 10)

def test_BoundedInterval___init____05( ):
    '''BoundedIntervals can be instantiated with 3 non-keyword arguments.'''
    i = BoundedInterval(0, 10, 'data')

def test_BoundedInterval___init____06( ):
    '''BoundedIntervals copy data on instantiation.'''
    data = { }
    i = BoundedInterval(0, 10, data)
    data['cat'] = 'dog'
    assert data != i.data
