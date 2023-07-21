"""
Training code on 'CodeWars'
Links of the kata :
------------------------------------------------------
Author : Antonin Valente
Année : 2023
Contact : valente@lpccaen.in2p3.fr
Language : Python3.11
"""
from typing import List

def histogram(values: List[int], bin_width: int) -> List[int]:
    """
    Produce a histogram of values with given bin width.
    
    Parameters
    ----------
    values : List[float]
        List of values to histogram.
    bin_width : float
        Width of bins.

    Returns
    -------
    List[float]
        List of bins.
    """
    print(f'Table : {values}')
    print(f'Bin width : {bin_width}')
    # Empty dataset
    if not values :
        return []
    
    # Singleton dataset
    if len(values) == 1 :
        max_value = max(values)
        min_value = 0

    # Normal dataset
    if len(values) > 1:
        # Calculate the min and max
        max_value = max(values)
        min_value = min(values)
    
    # Calculate the number of bins
    bins_number = int((max_value - 0)/bin_width) + 1

    # Create the bins
    bins = [0] * bins_number

    # Create the bin ranges
    bin_ranges = list(range(min_value + bin_width, max_value + bin_width, bin_width))
    print(f'Bins ranges : {bin_ranges}')

    # Fill the bins
    for value in values :
        # Iterating until range is find
        for i in range(len(bin_ranges)):
            if value >= bin_ranges[i-1] and value < bin_ranges[i] and i != 0 :
                bins[i] += 1
                break
            if value < bin_ranges[0] :
                bins[0] += 1
                break
            if value == bin_ranges[-1] :
                bins[-1] += 1
                break
            else :
                continue
    return bins 
                



