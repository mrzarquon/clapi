# clapi
Command Line API

This is a really rough POC around a generic cli api handler.

Mostly to learn click and play with requests more

But the idea is you set secrets/tokens you want to use with a rest API as env variables, give a template of the header requests in the example json, and the base URL for the api as well.

calling clapi.py pathname

turns it into a requests.get call and does a poor attempt at jq-fying the output