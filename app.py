from flask import Flask, request, render_template

app = Flask(__name__,template_folder="templates")

# List of common diseases and their associated symptoms and medicines
diseases = {
    "Common Cold": {
        "symptoms": ["fever", "cough", "sore throat"],
        "medicines": ["Acetaminophen", "Ibuprofen", "Cough suppressants"]
    },
    "Flu": {
        "symptoms": ["fever", "cough", "body aches"],
        "medicines": ["Antiviral medication", "Acetaminophen", "Ibuprofen"]
    },
    "Pneumonia": {
        "symptoms": ["fever", "cough", "shortness of breath"],
        "medicines": ["Antibiotics", "Bronchodilators", "Corticosteroids"]
    },
    # Add more diseases and their associated symptoms and medicines here
}

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Diagnostic page
@app.route("/diagnose", methods=["GET", "POST"])
def diagnose():
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")
        possible_diseases = []
        for disease, details in diseases.items():
            if all(symptom in symptoms for symptom in details["symptoms"]):
                possible_diseases.append(disease)
        if not possible_diseases:
            message = "No matches found. Please consult a doctor."
        else:
            message = "Possible diseases: " + ", ".join(possible_diseases) + "<br><br>Suggested medicines:<br>"
            for disease in possible_diseases:
                for medicine in diseases[disease]["medicines"]:
                    message += "- " + medicine + "<br>"
        return message
    return render_template("diagnose.html", diseases=diseases)

# Submit disease page
@app.route("/submit_disease", methods=["GET", "POST"])
def submit_disease():
    if request.method == "POST":
        disease_name = request.form["disease_name"]
        symptoms = request.form.getlist("symptoms")
        medicines = request.form.getlist("medicines")
        diseases[disease_name] = {"symptoms": symptoms, "medicines": medicines}
        message = "Disease added successfully."
        return render_template("submit_disease.html", message=message)
    return render_template("submit_disease.html")

if __name__ == "__main__":
    app.run(debug=True)
