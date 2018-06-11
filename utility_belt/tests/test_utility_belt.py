"""
Unit and regression test for the utility_belt package.
"""

# Import package, test suite, and other packages as needed
import utility_belt as ub
import pytest
import sys
import pandas as pd
import matplotlib.pyplot as plt

def test_utility_belt_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "utility_belt" in sys.modules

def test_constructor():
    a=ub.lammps_parser('data/log.lammps')
    assert a.properties == ['Step', 'Temp','PotEng','KinEng','TotEng']
    assert a.firstline == 89
    assert a.lastline == 90

def test_explore_lines():
    a=ub.lammps_parser('data/log.lammps')
    for f in a.explore_file():
        u = f['PotEng']
    assert u == -3178.119

def test_data_frame():
    a=ub.lammps_parser('data/log.lammps')
    assert a.data_frame()['PotEng'].tolist() == [-3196.8652, -3178.119]



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
tlow=ub.lammps_parser('data/tlow.log',run =1)
tlow.data_frame().hist(column='Hs', bins=100, ax = ax1, alpha = 0.5)
thigh=ub.lammps_parser('data/thigh.log',run=1)
thigh.data_frame().hist(column='Hs', bins=100, ax = ax1, alpha = 0.5)
plt.show()

