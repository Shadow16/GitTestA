#!/usr/bin/python
# -*- encoding: UTF-8 -*-

def welcome(nombre):
    print('Hello world', nombre)
    edad = int(input('How old are you? '))
    print('You are young', edad)
    # Import script hey
    from hey import status as f
    x = f(nombre, edad)
    print(x)


def main():
    nombre = input('Nombre: ')
    welcome(nombre)


if __name__ == '__main__':
    main()
