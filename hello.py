#!/usr/bin/python
# -*- coding: UTF-8 -*-


def menu():
    from statistics import median as md

    print('Hello world')

    edad = int(input('How old are you? '))

    if edad < 18:
        print('You are young', edad)
    else:
        print('You are a grandpha')

    arreglo = [4, 5, 8, 9, 4]

    mitad = md(arreglo)
    print(mitad)


if __name__ == '__main__':
    menu()
