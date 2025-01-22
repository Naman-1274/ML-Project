import os
import sys
import pickle

import numpy as np 
import pandas as pd
import dill
from src.ML_project.exception import Excception_handler

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise Excception_handler(e, sys)