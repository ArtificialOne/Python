import requests
import threading

url='http://google.com'

#Copy Form Data, needs all of it
data = {
        'firstName': 'james',
        'lastName': 'studoff',
        'shippingCountry': 'US',
        'shippingZip': '12333',
        'shippingAddress1': '8220 somewhere else',
        'shippingCity': 'Test City',
        'shippingState': 'FL',
        'phone': '1234561767',
        'email': 'slsl@gmail.com',
        'bill_checkbox': 'on',
        'billingSameAsShipping': 'yes',
        'creditCardType': 'visa',
        'creditCardNumber': '4007000000000027',
        'CVV': '234',
        'expmonth': '01',
        'expyear': '24'
}

response = requests.post(url,data=data).text
print(response)

#def do_request():
#    while True:
#        response = requests.post(url,data=data).text
#        print(response)
#
#threads = []
#for i in range(50):
#    t = threading.Thread(target=do_request)
#    t.daemon=True
#    threads.append(t)

#for i in range(50):
#    threads[i].start()

#for i in range(50):
#        threads[i].join()