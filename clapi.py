#!/usr/bin/env python3

import json
import click
import os
import requests
from typing import Dict, Any
from pygments import highlight, lexers, formatters

CLAPISECRET = str(os.getenv('CLAPISECRET'))
CLAPITOKEN = str(os.getenv('CLAPITOKEN'))

def swapsecrets(headers: dict, env_name: str, env_value: str) -> dict:
    for k,v in headers.items():
        headers[k] = v.replace(env_name,env_value)
    return headers

def injector(settings: dict) -> dict:
    headers = settings['headers']
    headers = swapsecrets(headers, 'CLAPISECRET', CLAPISECRET)
    headers = swapsecrets(headers, 'CLAPITOKEN', CLAPITOKEN)
    return settings

def output(x: dict):
    formatted_json = json.dumps(x, indent=4, sort_keys=True)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)

def get(url, headers, path):

    location = '%s/%s' % (url,path)

    resp = requests.get(location, headers=headers).text
    resp = json.loads(resp)
    return resp



@click.command()
@click.argument('path', type=str)
def main(path: str):
    settingsFiles = open('clapi.json','r')
    settings = json.load(settingsFiles)
    settings = injector(settings)
    output(settings)
    headers = settings['headers']
    output(headers)
    url = str(settings['url'])

    response = get(url, headers, path)

    output(response)



if __name__ == '__main__':
    main()
