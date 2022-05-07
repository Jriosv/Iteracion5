# Algoritmo de aprendizaje

import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
from tensorflow import keras
from chess_env import * 
from q_network import *
from mcts import *

env = ChessEnv()
q_model = Q_model(keras.models.load_model("./checkpoint3"))
examples = []

for i in range(4, 100):
    outcome = env.execute_episode(q_model,simulations = 10)
    q_model = env.train_model(q_model)
    print('Episode:',str(i),
          'Loss:',env.loss_history[-1],
          'Mean Loss:',np.mean(env.loss_history),
          'Outcome:',outcome)
    q_model.model.save("checkpoint" + str(i))
    env.reset()