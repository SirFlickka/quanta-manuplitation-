#!/usr/bin/env python

import csv

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#logging data in binary dimensional array on two multiple dimensional csv

dataset = pd.read_csv("logging.csv")

#quibits storage container data

container_data = dataset.groupby("container")

#plotting the binary data on two different axes

plt.figure(figsize=(15, 8))

plt.plot(dataset["container"], dataset["quibits"], color="blue")

plt.plot(container_data["container"], container_data["quibits"], color="red")

plt.xlabel("Container")

plt.ylabel("Quibits")

plt.show()
