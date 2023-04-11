import copy
from random import randint
from sorting_algorithms import *
import time


def generate_matrix(n, m, min_limit, max_limit):
    return [[randint(min_limit, max_limit) for _ in range(m)] for _ in range(n)]


"""Set a matrix"""
n = int(input('number of matrix rows: '))
m = int(input('number of matrix columns: '))
min_limit = int(input('random generator min limit: '))
max_limit = int(input('random generator max limit: '))

matrix = generate_matrix(n, m, min_limit, max_limit)


"""Selection sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    selection_sort(line)

print(f'Selection sort: {round((time.time() - start_time) * 1000)} ms')


"""Insertion sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    insertion_sort(line)

print(f'Insertion sort: {round((time.time() - start_time) * 1000)} ms')


"""Bubble sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    bubble_sort(line)

print(f'Bubble sort: {round((time.time() - start_time) * 1000)} ms')


"""Shell sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    shell_sort(line)

print(f'Shell sort: {round((time.time() - start_time) * 1000)} ms')


"""Quick sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    quick_sort(line)

print(f'Quick sort: {round((time.time() - start_time) * 1000)} ms')


"""Tournament sort"""
copied_matrix = copy.deepcopy(matrix)

start_time = time.time()

for line in copied_matrix:
    tournament_sort(line)

print(f'Tournament sort: {round((time.time() - start_time) * 1000)} ms')
