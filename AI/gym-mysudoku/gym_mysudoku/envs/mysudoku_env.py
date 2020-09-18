import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np
import random
import copy

MAX_REWARD = 1
MIN_REWARD = -5
MAX_STEPS = 200

INITIAL_ACCOUNT_BALANCE = 10000


class MySudokuEnv(gym.Env):
    """A sudoku trading environment for OpenAI gym"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MySudokuEnv, self).__init__()

        self.data = self._read_data('/home/amirhossein/Desktop/python-sudoku-generator-solver-master/AI/mypuzzle.txt')

        self.reward_range = (MIN_REWARD, MAX_REWARD)

        self.action_space = spaces.Discrete(729)

        self.observation_space = spaces.Discrete(81)

    def step(self, action):
        # Execute one time step within the environment
        self.current_step += 1
        done = False
        if self.observation[int(action / 9)] != '0':
            reward = -5
        elif self.answer[int(action / 9)] == str(action % 9 + 1):
            reward = 1
            self.observation[int(action / 9)] = str(action % 9 + 1)
            done = True
            for i in self.observation:
                if i == 0:
                    done = False
                    break
        else:
            reward = -1
        if self.current_step > MAX_STEPS:
            done = True
        return self.observation, reward, done, {}

    def reset(self):
        index_of_sudoku = random.randint(0, len(self.data[0]) - 1)
        self.current_step = 0
        self.answer = copy.copy(self.data[1][index_of_sudoku])
        self.observation = copy.copy(self.data[0][index_of_sudoku])
        self.observation = [x for x in str(self.observation)]
        self.answer = [x for x in str(self.answer)]
        print(len(self.observation))
        print(self.observation)
        return self.observation

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        ...

    def _read_data(self, path):
        with open(path, 'rt') as f:
            lines = f.readlines()
        lines2 = []
        for i in lines:
            lines2.append(i[:-1])
        del lines
        question = lines2[::2]
        answer = lines2[1::2]
        return tuple((question, answer))
