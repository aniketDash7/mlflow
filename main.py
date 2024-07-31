from mlflow import logger 

from mlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlflow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlflow.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Data transformation stage"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Model Training Stage"

if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise(e)