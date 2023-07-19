"""
Training code on 'CodeWars'
Links of the kata :
https://www.codewars.com/kata/56d060d90f9408fb3b000b03
------------------------------------------------------
Author : Antonin Valente
Année : 2023
Contact : valente@lpccaen.in2p3.fr
Language : Python3.11
"""
import re

def derivative(x : str):
    """
    Derivation of a polynomial expression, valid for integer coefficients.
    
    Parameters : 
    ------------
        x : str
            The polynomial expression in natural language
    Return :
    --------
        The derived polynomial expression  
    """
    # Calculates the signature of the expression,
    signature = re.findall('[+-]',x)
    
    # Splits the terms
    sequence_of_terms = re.split('\+|-',x)
    # Removes empty elements
    sequence_of_terms = [term for term in sequence_of_terms if term]

    # Adds an empty sign to the signature if it is omitted at the beginning of the expression 
    if len(signature) != len(sequence_of_terms):
        signature.insert(0,'')

    # Iterates over the terms and signs
    for i, items in enumerate(zip(signature, sequence_of_terms)):
        
        sign, term = items
                          
        # If x is at an explicit power
        if 'x^' in term:

            # Splits the term into two components: the factor and the power
            factor, power = term.split('x^')
            
            # Applies the derivative to the factor
            if factor :
                factor = int(factor) * int(power) 
                factor = str(factor)
            
            # If the factor is implicitly 1
            else :
                factor = power
                
            # Applies the derivative to the power
            power  = str(int(power)-1)
            
            # Makes the power 1 implicit
            if power == '1':
                sequence_of_terms[i] = sign + factor + 'x'

            # Makes x at power 0 implicit
            if power == '0':
                sequence_of_terms[i] = sign + factor

            # Rebuilds the term expression
            elif power not in ('1','0') :
                sequence_of_terms[i] = sign + factor + 'x^' + power

        # If x is implicitly at power 1
        elif 'x' in term :
            if 'x' != term :
                sequence_of_terms[i] = sign + term[:-1]
            if 'x' == term:
                sequence_of_terms[i] = sign + "1"
                
        # If the term is null or constant
        else :
            # For a constant term
            if len(sequence_of_terms) == 1 : 
                sequence_of_terms[i] = '0'
            
            # For a null term
            else :
                sequence_of_terms[i] = ''

    # Reconstructs the derived expression
    return ''.join(sequence_of_terms)
