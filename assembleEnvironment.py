#!/bin/python

from mikobot import MiKoBot
from OpenGL import GLU

import gym.envs.registration as reg
import gym
from mikobot import MiKoBot

reg.register("MiKo-v1",
             reward_threshold=2500,
             entry_point=MiKoBot,
             max_episode_steps=1000,
             tags={"pg_complexity": 8000000})


def mikoEnvironment():
    env = gym.make("MiKo-v1")
    return env, 10, 8


def bipedalEnvironment():
    env = gym.make("BipedalWalker-v2")
    return env, 24, 4



