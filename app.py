from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200585516"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON request
    req = request.get_json(force=True)
    
    # Extract the intent name from the request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Initialize a response dictionary
    response = {"fulfillmentMessages": []}
    
    # Handle the Phonebrand intent
    if intent_name == "fruits":
        # List of phone brands
        Fruits_Name = ["Apple", "orange", "grapes", "banana", "Blueberry"]
        # Building the response text
        response_text = "Fruits I like to eat are: \n" + "\n".join([f"{i+1} - {item}" for i, item in enumerate(Fruits_Name)])
        
        # Set the response in the fulfillmentMessages format
        response["fulfillmentMessages"].append({
            "text": {"text": [response_text]}
        })
    
    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
