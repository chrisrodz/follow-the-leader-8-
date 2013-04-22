import json
from t02 import t02

data = '[{"pk": 1, "model": "ccomforms.t02", "fields": {"f1": "Christian Rodr\\u00edguez", "f2": 801116705, "f3": "Nombramiento?", "f5": 200.0, "f6": "Sacar A en DB", "f8": "2013-04-21", "f9": "2013-04-21", "Transaccion": "Cambio", "f23": ["yes", "tumaieslagorda"], "f22": true, "f21": ["a", "s", "d", "f", "g", "h", "a", "s", "d", "f", "g"], "f20": [12.0, 13.0, 12.0, 41.0, 45.0, 23.0], "date_filled": "2013-04-21", "f26": "Naturales", "f25": false, "f24": false, "f27": ["1", "arrivederci", "2", "bogiorno"], "Ano_Fiscal": 2012, "Num_Referencia": 1234, "professor": 1, "f30": "Espero que salga bien", "f18": ["TEst2", "test3"], "f19": [0, 1], "f12": ["TEst2", "test3"], "f13": ["TEst2", "test3"], "f10": ["TEst2", "test3"], "f11": ["TEst2", "test3"], "f16": ["TEst2", "test3"], "f17": ["TEst2", "test3"], "f14": ["TEst2", "test3"], "f15": ["TEst2", "test3"]}}]'


generator = t02()
generator.buildPDF(data)