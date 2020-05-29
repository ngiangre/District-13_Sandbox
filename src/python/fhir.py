from fhirclient import client
import requests
import json

class Patient:

	def __init__(self,id="SarahThompson"):

		self.id = id
		self.base_url = "https://v8xnb6p8-inter.interopland.com/"
		self.fivelakes_url = "five-lakes-health-system/fhir/"
		self.payload = {}
		self.headers = {
		'Authorization': 'Basic aW50ZXJvcF9waXQ6VkwybExZNUhoTFpVOHozak02VkJvQ1d0NFMyRDlsZkZWSTVX'
		}
		self.getPatientData()
		self.extractPatientDemographics()

	def makeResourceUrl(self,resource="Careplan"):

		return self.base_url+self.fivelakes_url+resource+"?_pretty=true"

	def getPatientData(self):

		resource = "Patient/"+self.id+"/_history/1"
		response = requests.request("GET", self.makeResourceUrl(resource=resource), headers=self.headers, data = self.payload)
		parsed = response.json()
		self.patient_data = parsed

	def extractPatientDemographics(self):

		dem_dict = {
		'Given name' : ' '.join(self.patient_data['name'][0]['given']),
		"Family name" : self.patient_data['name'][0]['family'],
		"Birthdate" : self.patient_data['birthDate'],
		"Sex" : self.patient_data['gender'].title(),
		"Street" : self.patient_data["address"][0]["line"][0],
		"City" : self.patient_data["address"][0]["city"],
		"State" : self.patient_data["address"][0]["state"],
		"Country" : self.patient_data["address"][0]["country"]
		}

		self.demographicsDictionary = dem_dict


patient=Patient(id="SarahThompson")
patient.extractPatientDemographics()
