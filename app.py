from src.ML_project.logger import logging
from src.ML_project.exception import Excception_handler
from src.ML_project.components.data_ingestion import DataIngestion
from src.ML_project.components.data_ingestion import DataIngestionConfig
from src.ML_project.components.data_transformation import DataTransformationConfig,DataTransformation
from src.ML_project.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise Excception_handler(e,sys)