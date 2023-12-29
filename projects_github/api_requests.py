import requests, os
from PIL import Image
from IPython.display import IFrame

def get_ibm():
    url='https://www.ibm.com/'
    r=requests.get(url)
    header=r.headers

    print(f"The status code is variable.status_code: {r.status_code}\n")
    print(f"The body is variable.request.body: {r.request.body}\n")
    print(f"The headers are header=variable.headers: {header}\n")
    print(f"The header attribute date as header['date']: {header['date']}\n")
    print(f"The header attribute date as header['date']: {header['Content-Type']}\n")
    print(f"The encoding is r.encoding: {r.encoding}\n")
    print(f"The first 100 characters is r.text[0:100]: {r.text[0:100]}\n")

get_ibm()