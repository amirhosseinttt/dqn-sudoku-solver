from gym.envs.registration import register

register(
    id='mysudoku-v0',
    entry_point='gym_mysudoku.envs:MySudokuEnv',
)