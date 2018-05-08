"""
Unit and regression test for the utility_belt package.
"""

# Import package, test suite, and other packages as needed
import utility_belt as ub
import pytest
import sys

def test_utility_belt_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "utility_belt" in sys.modules

def test_constructor():
    a=ub.lammps_parser('data/log.lammps')
    assert a.properties == ['Step', 'Temp','PotEng','KinEng','TotEng','Press','2'] + ['Esoftcor']*16
    assert a.firstline == 89
    assert a.lastline == 90
