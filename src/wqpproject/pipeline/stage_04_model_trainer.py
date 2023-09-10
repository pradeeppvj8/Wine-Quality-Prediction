from wqpproject.config.configuration import ConfigurationManager
from wqpproject.components.model_trainer import ModelTrainer
from wqpproject import logger

STAGE_NAME = "Data Transformation Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e