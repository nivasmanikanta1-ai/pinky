from flask import Flask, render_template, request

app = Flask(__name__)

crop_data = {
    "rice": {
        "temperature": "28°C",
        "humidity": "65%",
        "soil": "Good",
        "irrigation": "Required",
        "health": "Healthy"
    },
    "wheat": {
        "temperature": "24°C",
        "humidity": "55%",
        "soil": "Good",
        "irrigation": "Moderate",
        "health": "Healthy"
    },
    "cotton": {
        "temperature": "30°C",
        "humidity": "60%",
        "soil": "Suitable",
        "irrigation": "Required",
        "health": "Healthy"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    crop = ""
    data = None
    message = ""

    if request.method == "POST":
        crop = request.form.get("crop", "").strip().lower()
        data = crop_data.get(crop)
        if not data:
            message = "Crop not found. Please enter Rice, Wheat, or Cotton."

    return render_template("index.html", crop=crop, data=data, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
