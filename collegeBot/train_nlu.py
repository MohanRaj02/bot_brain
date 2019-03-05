from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config


training_data = load_data("./data/nlu.md")

trainer = Trainer(config.load("config.yml"))

interpreter = trainer.train(training_data)

model_directory = trainer.persist("./models/nlu", fixed_model_name="demo")
