from mlops import logger 

from mlops.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlops.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlops.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlops.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline
from mlops.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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
    
STAGE_NAME = "Model Evaluation Stage"
if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise(e)