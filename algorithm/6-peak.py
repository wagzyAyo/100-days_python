#!/usr/bin/python3
'''Algorith that find the peak
in a list of integers'''

def find_peak(list_of_integers):
    '''funtion returns peak in a list of integers'''
    peak = []

    if len(list_of_integers) == 0:
        return 'None'
    
    if list_of_integers[0] > list_of_integers[-1]:
        peak = list_of_integers[0]
    elif list_of_integers[-1] > list_of_integers[0]:
        peak = list_of_integers[-2]
    else:
        peak = list_of_integers[1]

    return peak