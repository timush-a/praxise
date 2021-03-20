Requirements:
Python 3.8

Python Web API with one endpoint that takes a product id as a parameter and returns a list of all products recommended for it. You can specify a minimum proximity threshold parameter for recommendations.

To create a database, a csv file is used, in which in the 'product, another_product, probability' format are product id and recommendation probability.
Format of csv file:
YCQHFOR6Tb,SurAZyOklI,0.7
5qEw7HFnHW,2dubpkERaa,0.1
6LmjtnReqY,GuvpY7Ov2J,0.9
qO2iouOYnU,Rqm2HAQ9jl,0.5
XyWh23TtFv,IMhvAfXbOi,0.4
TY8Ac7vaYZ,XB5aqnAFVu,0.7

There are two ways to store data, json and shelve.

In the main_app.py file, you can choose which way of storing data will be used, the shelve module is used by default.
To store it in a json file, you need to import the json_storage_driver module and pass it to the constructor of the Server class.


To check responses from the server, you can use the requests module or browser.
Example:

import requests

response = requests.get('http://127.0.0.1:5000/get_probability/xtyFh38cQF')
print(response.content)  # 3lxasdpgNQxc 3lxtpgNaxc 3lxtpgNQxc 3lxtpgasdNQxc 3lxtpgNasdQx

response = requests.get('http://127.0.0.1:5000/get_probability/xtyFh38cQF&1')
print(response.content)  # 3lxasdpgNQxc




