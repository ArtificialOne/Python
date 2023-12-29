# cd C:\Users\Artificial\Documents\xxPython\practice\app
#flask --app app --debug run
#flask run --host 0.0.0.0
#curl.exe -X GET -i -w '\n' localhost:5000
#200 = Successful
#201 = New resource created
#202 = Request accepted, in process
#204 = Request completed, no content returned
#400 = Invalid request
#401 = Missing or invalid Credentials
#403 = Credentials not sufficient
#404 = Resource not found
#405 = Operation not supported
#500 = Error on server side

from flask import Flask, render_template, request, make_response
#from project1.module_geometry import func_area_of_rectangle

app = Flask(__name__)
#app = Flask("Sentiment Analysis")

data = [
    {
        "first_name": "Tanya",
        "Last_name": "Panda",
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "graduation_year": "1989"
    },
    {
        "first_name": "John",
        "Last_name": "Doe",
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "graduation_year": "1989"
    }
        ]

@app.route('/') #Implicit GET response Decorator for Routes / URL handlers, any argument of Slash and returns make_response
#@app.route('/', methods=["GET", "POST"]) #Explicit GET, POST response
def index():
    res = make_response("<b>Make_Response for custom 200 status code</b>")
    res.status_code = 200

    if request.method=="POST":
        res.status_code = 201
    
    if request.method=="GET":
        res.status_code = 200

    return res

    return {"message": "Welcome to this app"} #Can use this or below
    return jsonify(message="Welcome to this app") #Can use this or above

@app.route('/sample')
def sample_html():
    return render_template('sample.html')

@app.route('/path')
def path():
    return ("Hey, Panda!", 200)

@app.route('/path2')
def path2():
    return ({"message": "Another manner of message"}, 200)


#Confirm Data is accessible#
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404


########If q in Request########
#curl.exe -X GET -i -w '\n' "localhost:5000/name_search?q=Tanya"
#curl.exe -X GET -i -w '\n' "localhost:5000/name_search"
#curl.exe -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"
@app.route('/name_search')
def search_response():
    query = request.args.get('q')

    if not query:
        return {"error_message": "Input 'q' parameter missing"}, 422 #If missing 'q'

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return({"message": "Person not found"},404) #If person not found

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form['name']
        #record = create_new_record(name) if function defined
        #return redirect(url_for('read', id=record.id)) if record function defined
    return render_template("create.html")

@app.get("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500
    
#Dynamic URLs, RESTful API = Resource info sent as part of request URL
@app.route('/count')
def get_count():
    try: 
        return {"Data count": len(data)}, 200
    except NameError:
        return {"message": "Data not found"}, 500
    
#Dynamic url /person/type:var
#curl.exe -X GET -i localhost:5000/person/0dd63e57-0b5f-44bc-94ae-5c1b4947cb49
@app.route('/person/<uuid:id>')
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
        #TODO#    
    return {"message": "Person not found"}, 404

#curl.exe -X DELETE -i localhost:5000/person/0dd63e57-0b5f-44bc-94ae-5c1b4947cb49
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person ["id"] == str(id):
            data.remove(person)
            return {"message":f"{id}"}, 200
    return {"message": "Person not found"}, 404

#curl.exe -X POST -i -w '\n' \
#  --url http://localhost:5000/person \
#  --header 'Content-Type: application/json' \
#  --data '{}'
@app.route('/person', methods=["POST"])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message":"Invalid input parameter"}, 422
    try:
        data.append(new_person)
    except NameError:
        return {"message":"data not defined"}, 500
    
    return {"messsage":f"{new_person['id']}"}, 200

#If URL Path not found, return 404
@app.errorhandler(404)
def api_not_found(error):
    return {"message":"API not found"}, 404

#Run only if name is main; default unless explicitely changed
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)