from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["user_input"]
    
    # Very basic responses
    if "hello" in user_input.lower():
        reply = "Hi there! How can I help you?"
    elif "bye" in user_input.lower():
        reply = "Goodbye! Have a great day!"
    else:
        reply = "Sorry, I didn’t understand that."

    return render_template("index.html", reply=reply, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
