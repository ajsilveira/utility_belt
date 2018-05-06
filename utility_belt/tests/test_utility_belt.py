"""
Unit and regression test for the utility_belt package.
"""

# Import package, test suite, and other packages as needed
import utility_belt
import pytest
import sys

def test_utility_belt_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "utility_belt" in sys.modules
