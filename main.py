from mlflow import logger 

from mlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

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