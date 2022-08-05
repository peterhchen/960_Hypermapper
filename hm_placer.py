"""
File Name: hmPplacer.py
Description:
  Usage:
   > python hm_placer.py
Created by Peter Hanping Chen (7/16/2022)
"""
#!/usr/bin/python
#import math

import os
import sys
#import warnings
#from collections import OrderedDict

# ensure backward compatibility
from hypermapper import optimizer  # noqa
MIN_NUM = sys.float_info.max
HM_CNT = 0

def compute_function(x_in):
    """
    Description:
      Input: 20 features and randomly selected vector values
      from 64 feature vectors.
      Values: 20 target values.
      Calculate the penalty based on the input.
    :param x_in: dictionary containing the input points.
    :return: the value of the objective function.
    """
    global MIN_NUM
    global HM_CNT
    penalty = 0
    # Drive all parameters to their 10th value in the categorical space
    values = \
        [10, 10, 10, 10, 10,
        10, 10, 10, 10, 10,
        10, 10, 10, 10, 10,
        10, 10, 10, 10, 10]
    #print("==> x_in:")
    #print(x_in)            # {'0': '49', '1': '28', ..., '19': '15'} 
    parameters = []
    for _, value in x_in.items():
        parameters.append(value)
    for p_in, t_val in zip(parameters, values): # twenty 10s
        penalty += abs(int(p_in)-t_val)
    distance = penalty / len(parameters)
    print('HM_CNT:', HM_CNT)
    print('MIN_NUM:', MIN_NUM) 
    HM_CNT += 1
    if distance < MIN_NUM:
        print('Min distance found => HM_CNT:', HM_CNT)
        print("Min distance found => MIN_NUM:", MIN_NUM)
        MIN_NUM = distance

    return distance

def main():
    """
    Description:
      1. Read scenario file
      2. Call Hypermapper optimization function.
    """
    parameters_file = "./placer_scenario.json"
    # optimizer.optimize(parameters_file, branin4_function)
    optimizer.optimize(parameters_file, compute_function)
    print("End of test.")

if __name__ == "__main__":
    main()
