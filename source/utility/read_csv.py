#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd


in_file_name = str(input("File location of .csv file to read: "))
if os.path.exists(in_file_name):
    r_csv_index = pd.read_csv(f"{in_file_name}")
    r_csv_index.info(verbose=True, memory_usage=True, show_counts=True)
else:
    print(f"{in_file_name} was not found.")
