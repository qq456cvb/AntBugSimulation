from Agent import Agent
import Action
import random


class Bug(Agent):
    BREED_CYCLE = 15
    STARVE_MAX = 5

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.breed_cnt = 0
        self.starve_cnt = 0
        self.dead = False

    def __str__(self):
        return '$'

    # get adjacent cells observation
    def get_obs(self, env):
        obs = dict()
        adjacent_idx = {
            Action.RIGHT: (1, 0),
            Action.LEFT: (-1, 0),
            Action.DOWN: (0, 1),
            Action.UP: (0, -1),
        }
        for k, v in adjacent_idx.items():
            idx = (self.x + v[0], self.y + v[1])

            # check if not out of boundary
            if 0 <= idx[0] < env.blocks.shape[0] and 0 <= idx[1] < env.blocks.shape[1]:
                obs[k] = env.blocks[idx[0]][idx[1]]
        return obs

    def move_to(self, env, direction):
        env.blocks[self.x][self.y] = None
        self.x += Action.dir2idx[direction][0]
        self.y += Action.dir2idx[direction][1]
        env.blocks[self.x][self.y] = self

    def eat(self, env, direction):
        env.blocks[self.x][self.y] = None
        self.x += Action.dir2idx[direction][0]
        self.y += Action.dir2idx[direction][1]
        env.blocks[self.x][self.y].dead = True
        env.blocks[self.x][self.y] = self
        self.starve_cnt = 0

    def breed(self, env):
        obs = self.get_obs(env)
        for direction in obs:
            if obs[direction] is None:
                pos = (self.x + Action.dir2idx[direction][0], self.y + Action.dir2idx[direction][1])
                child = Bug(pos[0], pos[1])
                env.add(child)
                break

    def step(self, env, obs):
        action = None
        if self.dead:
            return action

        # starve
        self.starve_cnt += 1
        if self.starve_cnt >= Bug.STARVE_MAX:
            self.dead = True
            if env.blocks[self.x][self.y] == self:
                env.remove(self)
            return action

        # try to eat ant
        eaten = False
        for direction in random.sample(list(obs), len(obs)):
            if obs[direction].__class__.__name__ == 'Ant':
                self.eat(env, direction)
                action = direction
                eaten = True
                break

        # choose a random direction that is blank
        if not eaten:
            for direction in random.sample(list(obs), len(obs)):
                if obs[direction] is None:
                    self.move_to(env, direction)
                    action = direction
                    break

        if action is None:
            action = Action.NOOP

        # breed
        self.breed_cnt += 1
        if self.breed_cnt % Bug.BREED_CYCLE == 0:
            self.breed(env)

        return action
