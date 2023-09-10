from wqpproject.config.configuration import ConfigurationManager
from wqpproject.components.data_transformation import DataTransformation
from wqpproject import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            status = "False"
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()

            with open(data_validation_config.STATUS_FILE, 'r') as f:
                status = f.read().split(" ")[-1]

            if status == "True":     
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.perform_train_test_split()
            else:
                raise Exception("Schema is invalid")
        except Exception as e:
            logger.exception(e)
            raise e

# TODO :- Check if its required       
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e