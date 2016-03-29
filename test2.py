__author__ = 'sileix'

class Student:

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def __init__(self, name, score):
        self.name = name
        self._score = score

    # def get_grade(self):
    #     if self.score >= 90:
    #         return 'A'
    #     elif self.score >= 60:
    #         return 'B'
    #     else:
    #         return 'C'

bart = Student('bart')

class Animal(object):
    def run(self):
        print('Animal is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')

def run_twice(obj):
    obj.run()
    obj.run()

from types import MethodType
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)

class Screen:
    __slots__ = ('_width', '_height')
    def __init__(self, w=0, h = 0):
        self._width = w
        self._height = h

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width* self._height
    def __len__(self):
        return self.__sizeof__()
    def __str__(self):
        return 'Screen object (resolution: %s * %s)' % (self._width, self._height)

a = Screen()
a.width = 1024
a.height = 768
a.resolution = 10

import sqlite3

