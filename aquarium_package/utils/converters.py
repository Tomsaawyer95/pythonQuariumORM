import pandas as pd

def convert_to_df(aquarium):
    if aquarium.algues_list == []:
        pd_algue = pd.DataFrame()
    else :
        pd_algue = pd.DataFrame([algue.to_dict() for algue in aquarium.algues_list if algue.algue_aquarium_id])
    
    if aquarium.fishs_list == []:
        pd_fish = pd.DataFrame()
    else : 
        pd_fish = pd.DataFrame([fish.to_dict() for fish in aquarium.fishs_list if fish.fish_aquarium_id == aquarium.id])
    return pd_algue,pd_fish

