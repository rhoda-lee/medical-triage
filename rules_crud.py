from config import session
from models import MedicalRule
import json

class RulesCrud():
    def __init__(self, session):
        self.session = session

    def infer_priority(self, symptoms):
        rules = self.session.query(MedicalRule).all()
        for rule in rules:
            stored_conditions = rule.conditions.split(",")
            if all(condition.strip().lower() in symptoms for condition in stored_conditions):
                return {"priority": rule.priority, "message": rule.message}
        return {"priority": "Normal", "message": "No immediate attention needed."}