"""
Training code on 'CodeWars'
Links of the kata : 
https://www.codewars.com/kata/546e2562b03326a88e000020/python
-------------------------------------------------------------
Author : Antonin Valente
Année : 2023
Contact : valente@lpccaen.in2p3.fr
Language : Python3.11
"""
def square_digits(num: int):
    """
    Function that square digits of intergers

    Steps :
    -------
    1. Convert the integer to string
    2. Build a list comprehension whith each character
       - Convert into int
       - Then squared it
       - The convert into str
    3. Join the list of str
    4. Reconvert into int

    Parameters
    ----------
        num : int
            The integer
    
    Returns
    -------
        num : int
            The squared integer
    """
    return int(''.join([str(int(digit)**2) for digit in str(num)]))