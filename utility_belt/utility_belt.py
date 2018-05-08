"""
utility_belt.py
A set of tools for my work

Handles the primary functions
"""

class lammps_parser:
    """
    A parser for LAMMPS log files.

    Parameters
    ----------
    file : string
        The name of a LAMMPS log file.

    run : int, Optional, default: 0
        An index denoting which run (counting from 0) will be processed.
    """

    def __init__(self, file, run=0):
        count = 0
        for num, line in enumerate(open(file, 'r').readlines()):
             if line.startswith('Step') and (count == run):          
                self.firstline = num + 1
                self.properties = line.split()
             if line.startswith('Loop time') and (count == run):
                 self.lastline = num - 1 
                 count += 1          

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    pass
