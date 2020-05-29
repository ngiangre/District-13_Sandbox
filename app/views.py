from flask import Blueprint, render_template
from src.python.fhir import Patient

home_view = Blueprint('home_view', __name__)

@home_view.route('/')
def display_home_page():
	patient = Patient()
	return render_template('home_page.html',num=10, id=patient.id, patient=patient)
