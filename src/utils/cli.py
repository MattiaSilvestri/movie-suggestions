#!/usr/bin/env python3

'''Handle command line interface and user inputs'''

def get_titles():
    title = input("Insert movie title: ")
    year = input("Insert movie year: ")

    return [title, year]
