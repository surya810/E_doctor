from flask import Flask, request, render_template

app = Flask(__name__)

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
    return render_template("diagnose.html")

# Submit disease page
@app.route("/submit_disease", methods=["GET", "POST"])
def submit_disease():
    if request.method == "POST":
        disease = request.form.get("disease")
        symptoms = request.form.getlist("symptoms")
        medicines = request.form.getlist("medicines")
        if disease in diseases:
            message = f"{disease} already exists in the database."
