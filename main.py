import math
import os.path
import sys

from stable_baselines3 import A2C

from PidTunerEnv import PidTunerEnv


def step(time):
    if time >= 25.0:
        return 1.0
    else:
        return 0.0


def sin(time):
    return math.sin(2 * math.pi * time/12)


if __name__ == '__main__':
    training = False
    input_function = step
    model_name = "PID-Parameter-Model"

    # Basic argument  processing
    if "sin" in sys.argv:
        input_function = sin
    elif "step" in sys.argv:
        input_function = step
    if "-t" in sys.argv:
        training = True

    # Setup
    env = PidTunerEnv(input_function=input_function)
    if os.path.isfile("PID-Parameter-Model.zip"):
        model = A2C.load(model_name, env=env)
    else:
        model = A2C('MlpPolicy', env, verbose=1)

    if training:
        model.learn(total_timesteps=25000)
        model.save(model_name)

    obs = env.reset()
    action, _state = model.predict(obs, deterministic=True)
    print(action)
    obs, reward, done, info = env.step(action)
    print(reward)
    env.render()
    if done:
        obs = env.reset()
