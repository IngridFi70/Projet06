import pickle
import bentoml

# Charger ton modèle pickle
with open("/Users/ingrid/Documents/OpenClassrooms/PROJETS/model/finalized_model.sav", "rb") as f:
    model = pickle.load(f)

# Sauvegarder dans le store BentoML
bentoml.picklable_model.save_model("selected_model:latest", model)

# import bentoml
# from service import RandomForestService  # import de la classe service définie

# Instanciez votre service BentoML
# svc = RandomForestService()

# Enregistrez votre modèle entraîné dans l’artefact
# svc.pack('model', selected_model)

# Sauvegardez le service dans le BentoML store local
# bento_ref = svc.save()

# print(f"Modèle enregistré avec le tag : {bento_ref.tag}")