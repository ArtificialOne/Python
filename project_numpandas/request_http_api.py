import requests
import os
import pandas as pd
from PIL import Image
from randomuser import RandomUser
import requests
import random
import json

def get_ibm():
    url='https://www.ibm.com/'
    r=requests.get(url)
    print(f"The status code: {r.status_code}\n")
    print(f"The headers: {r.request.headers}\n")
    print(f"The body: {r.request.body}\n")

    header=r.headers
    print(f"The status code is variable.status_code: {r.status_code}\n")
    print(f"The body is variable.request.body: {r.request.body}\n")
    print(f"The headers are header=variable.headers: {header}\n")
    print(f"The header attribute date as header['date']: {header['date']}\n")
    print(f"The header attribute date as header['date']: {header['Content-Type']}\n")
    print(f"The encoding is r.encoding: {r.encoding}\n")
    print(f"The first 100 characters is r.text[0:100]: {r.text[0:100]}\n")

def get_images():
    url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
    r=requests.get(url)
    path=os.path.join(os.getcwd(),'anynamehere.png')

    print(f"The headers of image r.headers: {r.headers}\n")
    print(f"The content type is r.headers['Content-Type']: {r.headers['Content-Type']}\n")
    print(f"Using path=os.path.join(os.getcwd(),'anynamehere.png'), ready image into cwd: {path}\n")
    with open(path,'wb') as f:
        f.write(r.content) #Puts file image.png in current directory
    Image.open(path).show() #Display image with  Image.open(path) method with path passed in, with .show() method at end.

def get_bin():
    url='https://www.httbin.org/get'
    payload={"name":"Joseph","ID":"123"}
    r=requests.get(url,params=payload)
    print(r.url) #Prints r which is requests.get(url) and the 'params' which is payload

    print(r.status_code,'\n')
    print(r.request.headers,'\n')
    print(r.request.body,'\n')
    print(r.text,'\n')
    print(f"The content type: {r.headers['Content-Type']}")

def post_bin():
    url_post='https://www.httbin.org/post'
    payload={"name":"Joseph","ID":"123"}
    r_post=requests.post(url_post,data=payload) 
    print(f"Post request URL: {r_post.url}\n") #Prints r_post which is requests.post(url) and the 'data' which is payload
    print(f"Post request body = r_post.request.body {r_post.request.body}\n")

def random_user():
    r=RandomUser()
    user_list=r.generate_users(10) #Generate 10 users in a list
    print(f"Memory location of user_list: {user_list}\n")

    name=r.get_full_name()
    print(f"For user in list, print user.get_full_name() and user.get_email()")
    for user in user_list:
        print(f"{user.get_full_name()}   {user.get_email()}")
    for user in user_list:
        print(f"{user.get_full_name()}   {user.get_picture()}")

def random_users_list(): #Generate table with info about users, return Pandas Dataframe with users
    users=[]
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(),"DOB":user.get_dob(),"Picture":user.get_picture()})
    print(pd.DataFrame(users))

def fruitvice():
    data = requests.get("https://fruityvice.com/api/fruit/all")
    results=json.loads(data.text)

    df1=pd.DataFrame(results) #Convert Json Results to Pandas DataFrame
    #print(df1)

    df2 = pd.json_normalize(results) #Since the "nutritions" column has multiple subcolumns, it needs to be 'normalized'
    #print(df2)

    cherry=df2.loc[df2["name"] == 'Cherry']
    print(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

    cal_banana=df2.loc[df2["name"] == "Banana"] #Finding calories of banana
    print(f"The calories of banana: cal_banana.iloc[0]['nutritions.calories']: {cal_banana.iloc[0]['nutritions.calories']}")

def public_api_catfacts():
    url='https://cat-fact.herokuapp.com/facts'
    r=requests.get(url)
    results=json.loads(r.text)
    
    df1=pd.DataFrame(results) #Convert Json Results to Pandas DataFrame
    print(df1)

def test():
    number_list=random.random()
    new_list=[x**2 for x in number_list] #Expression for item in iterable if condition
    print(new_list)

    new_list_copy=[x for x in number_list if x % 2 == 1]
    print(new_list_copy)


#get_ibm()
#get_bin()
#post_bin()
#get_images()
#random_user()
#df1=pd.DataFrame(random_users_list())
#fruitvice()
#public_api_catfacts()
test()