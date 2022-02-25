from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import random
import numpy as np

from utils.general import clumpyRandom

class EmptyEnv(MiniGridEnv):
    """
    Empty grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=8,
        agent_start_pos=(1,1),
        agent_start_dir=0,
        rainbow_floor=False,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir 
        
        self.rainbow_floor = rainbow_floor
        if self.rainbow_floor:
            colorprobability = [0.05, 0.05, 0.75, 0.05, 0.05, 0.05]
            self.tile_pattern = clumpyRandom(size,COLOR_NAMES,colorprobability,numiter=200)


        super().__init__(
            grid_size=size,
            max_steps=10*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)
        
        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
#         self.put_obj(Goal(), width - 2, height - 2) #orig
        coordsW = np.random.randint(low=1, high=width-1, size=2)
        self.put_obj(Goal(), coordsW[0], coordsW[1])
        
        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()
        
        if self.rainbow_floor:
            # Fill the grid with tiles
            for ww in range(1,width-1):
                for hh in range(1,height-1):
                    if coordsW[0]==ww and coordsW[1]==hh: #don't overlap the goal
                        continue
                    else:
                        tilecolor = self.tile_pattern[ww,hh]
                        self.put_obj(Floor(tilecolor), ww, hh)

        self.mission = "get to the green goal square"

class EmptyEnv5x5(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=5, **kwargs)

class EmptyRandomEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

class EmptyEnv6x6(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=6, **kwargs)

class EmptyRandomEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None)

class EmptyEnv16x16(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=16, **kwargs)
        
class EmptyEnv16x16_rainbow(EmptyEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None,rainbow_floor=True)
        
class EmptyEnv22x22_rainbow(EmptyEnv):
    def __init__(self):
        super().__init__(size=22, agent_start_pos=None,rainbow_floor=True)



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
    id='MiniGrid-Empty-Rainbow-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyEnv16x16_rainbow'
)

register(
    id='MiniGrid-Empty-Rainbow-22x22-v0',
    entry_point='gym_minigrid.envs:EmptyEnv22x22_rainbow'
)
