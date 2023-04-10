#!/usr/bin/env python3

import requests

"""Handles API calls and responses"""

def get_id(response: requests.Response, year: str) -> str:
    results = response.json()['results']
    for i in range(len(results)):
        page = None
        if results[i]['releaseYear']['year'] == year:
            page = i
        else:
            continue
    if page:
        id = results[page]['id']
        return id
    else:
        print("No movies found for that year.")
        return ""
