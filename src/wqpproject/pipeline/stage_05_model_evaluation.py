from wqpproject.config.configuration import ConfigurationManager
from wqpproject.components.model_evaluation import ModelEvaluation
from wqpproject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e