from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class hrrlEnv(MiniGridEnv):
    """
    hrrl grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=8,
        agent_start_pos=(1,1),
        agent_start_dir=0,
        max_steps=float('inf'),
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        super().__init__(
            grid_size=size,
            max_steps=float('inf'),
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an hrrl grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
#         self.put_obj(Goal(), width - 2, height - 2)
        
        # Place drive locations
        coordsW = np.random.randint(low=1, high=width-1, size=2)
        self.put_obj(Water(), coordsW[0], coordsW[1])
        
        coordsF = np.random.randint(low=1, high=width-1, size=2)
        while np.all(coordsW == coordsF):
            coordsF = np.random.randint(low=1, high=width-1, size=2)
        self.put_obj(Food(), coordsF[0], coordsF[1])
        
        coordsH = np.random.randint(low=1, high=width-1, size=2)
        while np.all(coordsW == coordsH) or np.all(coordsF == coordsH):
            coordsH = np.random.randint(low=1, high=width-1, size=2)
        self.put_obj(Home(), coordsH[0], coordsH[1])
        
        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

class hrrlEnv5x5(hrrlEnv):
    def __init__(self):
        super().__init__(size=5)

class hrrlRandomEnv5x5(hrrlEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

class hrrlEnv6x6(hrrlEnv):
    def __init__(self):
        super().__init__(size=6)

class hrrlRandomEnv6x6(hrrlEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None)

class hrrlEnv16x16(hrrlEnv):
    def __init__(self):
        super().__init__(size=16)

register(
    id='MiniGrid-hrrl-5x5-v0',
    entry_point='gym_minigrid.envs:hrrlEnv5x5'
)

register(
    id='MiniGrid-hrrl-Random-5x5-v0',
    entry_point='gym_minigrid.envs:hrrlRandomEnv5x5'
)

register(
    id='MiniGrid-hrrl-6x6-v0',
    entry_point='gym_minigrid.envs:hrrlEnv6x6'
)

register(
    id='MiniGrid-hrrl-Random-6x6-v0',
    entry_point='gym_minigrid.envs:hrrlRandomEnv6x6'
)

register(
    id='MiniGrid-hrrl-8x8-v0',
    entry_point='gym_minigrid.envs:hrrlEnv'
)

register(
    id='MiniGrid-hrrl-16x16-v0',
    entry_point='gym_minigrid.envs:hrrlEnv16x16'
)
