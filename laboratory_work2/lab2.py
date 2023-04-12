import os
from random import shuffle
from Stack import Stack
from Deque import Deque

"""Task 1"""


def alphabet_sort(books):
    result = []
    d1 = Deque(*[book[:-1] for book in books.readlines()])
    d2 = Deque()

    while not d1.is_empty():
        while not d2.is_empty() and d2.get_first() < d1.get_first():
            d1.add_last(d2.pop_first())
        d2.add_first(d1.pop_first())

    while not d2.is_empty():
        result.append(d2.pop_first())
    return result


books = open(os.getcwd() + '\\test1')
print(*alphabet_sort(books), sep='\n')

"""Task 2"""


def encode(text: str):
    result = []

    for letter in text:
        if not letter.isalpha():
            result += letter
        else:
            while key_ring.get_first() != letter:
                key_ring.rotate()
            key_ring.rotate()
            result += key_ring.get_first()

    return ''.join(result)


def decode(text):
    result = ''

    for letter in text:
        if not letter.isalpha():
            result += letter
        else:
            while key_ring.get_first() != letter:
                key_ring.rotate(backward=True)
            key_ring.rotate(backward=True)
            result += key_ring.get_first()

    return ''.join(result)


alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet += ''.join(alphabet).upper()
shuffle(alphabet)
print(*alphabet)

key_ring = Deque(*[letter for letter in alphabet])

text = input('Enter text: ')
encoded_text = encode(text)
decoded_text = decode(encoded_text)
print(encoded_text)
print(decoded_text)

"""Task 3"""


def move(a, b):
    if c.size() == len(disks):
        return
    if a.size() == 0 and b.size() > 0:
        a.add_last(b.pop_last())
    elif a.size() > 0 and b.size() == 0:
        b.add_last(a.pop_last())
    elif a.size() > 0 and b.size() > 0:
        if a.get_last() > b.get_last():
            a.add_last(b.pop_last())
        else:
            b.add_last(a.pop_last())


disks = [_ for _ in range(int(input('Enter number of disks: ')), 0, -1)]

a = Stack(*disks)
b = Stack()
c = Stack()

while c.size() != len(disks):
    move(a, c)
    move(a, b)
    move(b, c)

while not c.is_empty():
    print(c.pop_last())

"""Task 4"""


def check_curve_braces(program: str):
    stack = Stack()
    for letter in program:
        if letter == '(':
            stack.add_last(letter)
        elif letter == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop_last()

    return True if stack.is_empty() else False


print(check_curve_braces('(())'))
print(check_curve_braces('((())'))
print(check_curve_braces('(()))'))
print(check_curve_braces('(()())()'))
"""Task 5"""


def check_square_braces(program: str):
    stack = Deque()
    for letter in program:
        if letter == '[':
            stack.add_last(letter)
        elif letter == ']':
            if stack.is_empty():
                return False
            else:
                stack.pop_last()

    return True if stack.is_empty() else False


print(check_curve_braces('[[]]'))
print(check_curve_braces('[[[]]'))
print(check_curve_braces('[[]]]'))
print(check_curve_braces('[[][]][]'))

"""Task 6"""


def digits_letters_others(text: str):
    result = []
    letters = Stack()
    other_symbols = Stack()

    for element in text:
        if element.isdigit():
            result += element
        elif element.isalpha():
            letters.add_last(element)
        else:
            other_symbols.add_last(element)
    letters.reverse()
    other_symbols.reverse()

    while not letters.is_empty():
        result += letters.pop_last()

    while not other_symbols.is_empty():
        result += other_symbols.pop_last()

    return ''.join(result)


print(digits_letters_others('a?b<cd1+2(34'))

"""Task 7"""


def negatives_positives(numbers):
    result = []
    positives = Deque()

    for element in numbers:
        if element < 0:
            result.append(element)
        else:
            positives.add_last(element)

    while not positives.is_empty():
        result.append(positives.pop_first())

    return result


print(negatives_positives([2, -3, 5, -7, 8, -9]))

"""Task 8"""


def swap_lines(text: list[str]):
    result = []
    lines = Stack()

    [lines.add_last(line) for line in text]
    while not lines.is_empty():
        result.append(lines.pop_last())

    return result


text = open(os.getcwd() + '\\test8')
print(*alphabet_sort(text), sep='\n')
