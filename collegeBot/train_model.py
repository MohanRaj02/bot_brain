from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy

fallback = FallbackPolicy(fallback_action_name = "utter_unclear",
                              core_threshold = 0.2,
                              nlu_threshold = 0.6)
agent = Agent('domain.yml', policies=[fallback, MemoizationPolicy(), KerasPolicy()])
training_data = agent.load_data('stories.md')
agent.train(
        training_data,
        validation_split = 0.2,
        epochs = 500
)
agent.persist('./models/dialogue')
