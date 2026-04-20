from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all 20 input values from form
        values = [
            float(request.form['anxiety_level']),
            float(request.form['self_esteem']),
            float(request.form['mental_health_history']),
            float(request.form['depression']),
            float(request.form['headache']),
            float(request.form['blood_pressure']),
            float(request.form['sleep_quality']),
            float(request.form['breathing_problem']),
            float(request.form['noise_level']),
            float(request.form['living_conditions']),
            float(request.form['safety']),
            float(request.form['basic_needs']),
            float(request.form['academic_performance']),
            float(request.form['study_load']),
            float(request.form['teacher_student_relationship']),
            float(request.form['future_career_concerns']),
            float(request.form['social_support']),
            float(request.form['peer_pressure']),
            float(request.form['extracurricular_activities']),
            float(request.form['bullying'])
        ]

        # Predict
        prediction = model.predict([values])[0]

        # Convert numeric output to text
        if prediction == 0:
            result = "Low Stress 😌"
        elif prediction == 1:
            result = "Medium Stress 😐"
        else:
            result = "High Stress 😰"

    except Exception as e:
        result = "Error: Please enter valid values"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)