import bentoml
from bentoml.io import JSON

# Charger le modèle depuis le store BentoML
model_runner = bentoml.picklable_model.get("selected_model:latest").to_runner()

svc = bentoml.Service("seleted_model_service", runners=[model_runner])

# Endpoint API
@svc.api(input=JSON(), output=JSON())
def predict(input_data):
    # Ici input_data est un dict envoyé en JSON
    # Convertir en format que ton modèle comprend
    features = input_data["features"]  # Ex: liste ou dict
    prediction = model_runner.run(features)
    return {"prediction": prediction}

