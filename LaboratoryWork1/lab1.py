from random import randint
from sortingAlgorithms import *
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
start_time = time.time()

for line in matrix:
    selection_sort(line.copy())

print(f'Selection sort: {round((time.time() - start_time) * 1000)} ms')


"""Insertion sort"""
start_time = time.time()

for line in matrix:
    insertion_sort(line.copy())

print(f'Insertion sort: {round((time.time() - start_time) * 1000)} ms')


"""Bubble sort"""
start_time = time.time()

for line in matrix:
    bubble_sort(line.copy())

print(f'Bubble sort: {round((time.time() - start_time) * 1000)} ms')


"""Shell sort"""
start_time = time.time()

for line in matrix:
    shell_sort(line.copy())

print(f'Shell sort: {round((time.time() - start_time) * 1000)} ms')


"""Quick sort"""
start_time = time.time()

for line in matrix:
    quick_sort(line.copy())

print(f'Quick sort: {round((time.time() - start_time) * 1000)} ms')


"""Tournament sort"""
start_time = time.time()

for line in matrix:
    tournament_sort(line.copy())

print(f'Tournament sort: {round((time.time() - start_time) * 1000)} ms')
