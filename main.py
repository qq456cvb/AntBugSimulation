from Maze import Maze
from Ant import Ant
from Bug import Bug
import numpy as np
from Viewer import draw
import cv2


if __name__ == '__main__':
    np.random.seed(60
                   )
    maze = Maze(10, 10)
    maze.reset()
    for _ in range(50):
        ant = Ant(np.random.randint(10), np.random.randint(10))
        maze.add(ant)
    for _ in range(5):
        bug = Bug(np.random.randint(10), np.random.randint(10))
        maze.add(bug)

    for step in range(100):
        print('step: ', step)
        all_agents = maze.get_all_agents()
        for agent in all_agents:
            obs = agent.get_obs(maze)
            action = agent.step(maze, obs)
        print(maze)
        all_agents = maze.get_all_agents()
        print('%d ants, %d bugs' % (sum([agent.__class__.__name__ == 'Ant' for agent in all_agents]),
                                    sum([agent.__class__.__name__ == 'Bug' for agent in all_agents])))
        img = draw(maze)
        cv2.imshow('test', img)
        cv2.waitKey()
