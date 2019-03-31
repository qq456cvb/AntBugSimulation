import numpy as np
from Env import Env
from Ant import Ant
import Action


class Maze(Env):
    def __init__(self, x, y):
        super().__init__()
        self.blocks = np.empty((x, y), dtype=object)

    def __str__(self):
        return '\n'.join([' '.join(['-' if not self.blocks[i][j] else str(self.blocks[i][j]) for i in range(self.blocks.shape[0])]) for j in range(self.blocks.shape[1])])

    def add(self, agent):
        self.blocks[agent.x, agent.y] = agent

    def remove(self, agent):
        self.blocks[agent.x, agent.y] = None

    def get_all_agents(self):
        agents = []
        for i in range(self.blocks.shape[0]):
            for j in range(self.blocks.shape[1]):
                if self.blocks[i][j] is not None:
                    agents.append(self.blocks[i][j])
        return agents


if __name__ == '__main__':
    maze = Maze(20, 20)
    print(maze.__class__.__name__)
    a = Ant(2, 2)
    maze.blocks[0][0] = a
    print(maze)
    # print(np.where(maze.blocks == a))
    # print(maze.blocks[np.where(maze.blocks == a)])
