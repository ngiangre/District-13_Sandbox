from fhirclient import client
settings = {
'app_id' : 'interop_pit',
'app_secret' : 'aW50ZXJvcF9waXQ6VkwybExZNUhoTFpVOHozak02VkJvQ1d0NFMyRDlsZkZWSTVX',
'api_base' : 'https://v8xnb6p8-inter.interopland.com/five-lakes-health-system/fhir/',
'password' : 'VL2lLY5HhLZU8z3jM6VBoCWt4S2D9lfFVI5W'
}
smart = client.FHIRClient(settings=settings)
import fhirclient.models.patient as p
