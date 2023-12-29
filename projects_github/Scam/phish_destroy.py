import random
import time

#randomlists.com for usernames, passwords
#-VPN > Navigate to Site > Inspect > Network > Submit fake Credentials > Obtain Form Data 
#-Python:

payload = {
    "EMAILDESCRIPTION":"EMAIL",
    "INPUTPASSWORD":"PASSWORD",
}
def postRequest(payload):
    response=response.post('http://URLOFPOST/login.html', data=payload)
    print(payload)
    print(response)
    return

def main():
    newPayload = payload
    with open('usernames.txt','r') as usernameFile:
        usernames=usernameFile.readlines()
    with open('passwords.txt','r') as passwordFile:
        passwords=passwordFile.readlines()
    for i in range(0,len(usernames)):
        newPayload['EMAILDESCRIPTION']=(usernames[i].rstrip() + str(random.randint(1960,2021) + '@gmail.com'))
        newPayload['INPUTPASSWORD']=passwords[i].rstrip()
        print(f'Sending fake data... Iteration # {(i+1)}')
        postRequest(newPayload)
        sleepTime=random.randint(0,10)
        print(f'Sleeping for {sleepTime} seconds!')
        time.sleep(sleepTime)

while True:
    main()

#usernames.txt
#passwords.txt