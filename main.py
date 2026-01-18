from flask import Flask,request,jsonify,render_template
from google import genai
 

client = genai.Client(api_key="YOUR_API_KEY")

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
    prompt=request.json["message"]
    response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )
    return jsonify({"reply":response.text})

if __name__ == "__main__":
    app.run(port=8013)
