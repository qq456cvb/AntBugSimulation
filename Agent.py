import numpy as np
import abc


class Agent:
    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    @abc.abstractmethod
    def get_obs(self, env):
        pass

    @abc.abstractmethod
    def step(self, env, obs):
        pass



