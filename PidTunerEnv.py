import math
import gym
from gym import spaces
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

from pidsmd.pidspringmassdampersystem import PidSpringMassDamperSystem


class PidTunerEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, input_function: Callable[[float], float], duration=50.0):
        super(PidTunerEnv, self).__init__()
        smd = PidSpringMassDamperSystem()
        smd.initialize()
        self.step_size = smd.SpringMassDamper_PID_M.contents.Timing.stepSize0

        self.input_function_callable = input_function
        self.simulation_duration = duration
        self.response = []
        self.input = []
        self.time = []
        self.simulation_steps = math.ceil(self.simulation_duration / self.step_size)
        self.observation_space_size = 2*self.simulation_steps + 3

        self.action_space = spaces.Box(low=-1000000, high=1000000,
                                       shape=(3,), dtype=np.float)
        self.observation_space = spaces.Box(low=-100000000000, high=10000000000,
                                            shape=(self.observation_space_size,), dtype=np.float)

        smd.terminate()

    def step(self, action):
        smd = PidSpringMassDamperSystem()

        smd.initialize()

        smd.parameters.Kp = action[0]
        smd.parameters.Ki = action[1]
        smd.parameters.Kd = action[2]

        sum_of_error = 0
        for step in range(self.simulation_steps):
            simulation_time = step * self.step_size

            input_value = self.input_function_callable(simulation_time)
            smd.inputs.u_position = input_value

            self.time.append(simulation_time)
            self.input.append(input_value)

            smd.step()
            self.response.append(smd.outputs.position)
            sum_of_error = sum_of_error + np.square(smd.inputs.u_position - smd.outputs.position)

        smd.terminate()
        done = True
        reward = 1 / (sum_of_error / self.simulation_steps)
        info = {}
        state = []
        state.append(smd.parameters.Kp)
        state.append(smd.parameters.Ki)
        state.append(smd.parameters.Kp)
        state = state + self.input + self.response

        return np.array(state).astype(np.float), reward, done, info

    def reset(self):
        self.time.clear()
        self.input.clear()
        self.response.clear()
        return np.zeros(self.observation_space_size)  # reward, done, info can't be included

    def render(self, mode='human'):
        plt.ion()

        plt.figure(2)
        plt.clf()
        plt.plot(self.time, self.input, self.time, self.response)
        plt.legend(["Command Signal ", "Response"])
        plt.xlabel("Time (s)")
        plt.ylabel("Mass Position")
        plt.title("Controlled System Response")
        plt.show()

    def close(self):
        pass
