import requests
import json

url = 'http://127.0.0.1:5000'
data={'age':63, 'sex':1, 'cp':3,'trestbps':145, 'chol':233, 'fbs':1,'restecg':0, 'thalach':150, 'exang':0,'oldpeak':2.3, 'slope':0, 'ca':0,'thal':1}
data = json.dumps(data)

send_requests=requests.post(url,data)
print(send_requests)