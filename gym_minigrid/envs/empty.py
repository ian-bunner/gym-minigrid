from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class EmptyEnv(MiniGridEnv):
    """
    Empty grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=7,
        agent_start_pos=None,
        agent_start_dir=0,
        goal_pos=None

    ):
        if agent_start_pos == None:
            agent_start_pos = (int((size+1)/2), int((size+1)/2))

        if goal_pos == None:
            goal_pos = (size, size)
        
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
        self.size = size
        self.goal_pos=goal_pos

        super().__init__(
            grid_size=size+2,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
        #x, y = self._rand_pos(0, self.size - 1, 0, self.size -1)
        x, y = self.goal_pos[0], self.goal_pos[1] 
        self.grid.set(x, y, Goal())
        self.goal_x = x
        self.goal_y = y

        # Place the agent
        if self.agent_start_pos is not None:
            self.start_pos = self.agent_start_pos
            self.start_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

class EmptyEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5)

class EmptyRandomEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

class EmptyEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6)

class EmptyRandomEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None)

class EmptyEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16)

class EmptyEnv7x7(EmptyEnv):
    def __init__(self):
        super().__init__(size=7, agent_start_pos=(3,3))

class EmptyEnv11x11(EmptyEnv):
    def __init__(self):
        super().__init__(size=13, agent_start_pos=(6,6))

class EmptyEnv25x25(EmptyEnv):
    def __init__(self):
        super().__init__(size=27, agent_start_pos=(13,13))

class EmptyEnvNxN(EmptyEnv):
    def __init__(self, size=None, start=None, goal=None):
        '''
        if _agent_start_pos == None:
            _agent_start_pos_ = ((_size+1)/2 , (_size+1)/2)
        if _goal_pos=None:
            _goal_pos = (_size - 2, _size - 2)
        '''
        super().__init__(size=size+2, agent_start_pos = start, goal_pos = goal)


register(
    id='MiniGrid-Empty-NxN-v0',
    entry_point='gym_minigrid.envs:EmptyEnvNxN'
)
register(
    id='MiniGrid-Empty-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyEnv5x5'
)

register(
    id='MiniGrid-Empty-Random-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv5x5'
)

register(
    id='MiniGrid-Empty-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyEnv6x6'
)

register(
    id='MiniGrid-Empty-Random-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv6x6'
)

register(
    id='MiniGrid-Empty-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyEnv'
)

register(
    id='MiniGrid-Empty-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyEnv16x16'
)

register(
    id='MiniGrid-Empty-7x7-v0',
    entry_point='gym_minigrid.envs:EmptyEnv7x7'
)

register(
    id='MiniGrid-Empty-11x11-v0',
    entry_point='gym_minigrid.envs:EmptyEnv11x11'
)

register(
    id='MiniGrid-Empty-25x25-v0',
    entry_point='gym_minigrid.envs:EmptyEnv25x25'
)


