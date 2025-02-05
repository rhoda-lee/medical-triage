from flask import Flask, request, jsonify
from models import MedicalRule
from config import session
from rules_crud import RulesCrud

app = Flask(__name__)
rules_crud = RulesCrud(session)


@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    symptoms = [s.strip().lower() for s in data.get("symptoms", [])]
    result = rules_crud.infer_priority(symptoms)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)