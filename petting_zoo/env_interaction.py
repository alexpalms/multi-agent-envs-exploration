import argparse
from pettingzoo import atari
from pettingzoo import butterfly
import sys

def parallel_api(env, interactive):

    print("Observations space")
    print(env.observation_space)

    print("Action space")
    print(env.action_space)

    observations = env.reset()

    while env.agents:
        # this is where you would insert your policy
        actions = {agent: env.action_space(agent).sample() for agent in env.agents}

        observations, rewards, terminations, truncations, infos = env.step(actions)

        print("Rewards: {}".format(rewards))
        print("Termination: {}".format(terminations))
        print("Truncation: {}".format(truncations))
        print("Infos: {}".format(infos))
        print("Action: {}".format(actions))
        if interactive:
            input("Press Button")

    env.close()

def aec_api(env, interactive):
    print("Observations space")
    print(env.observation_space)

    print("Action space")
    print(env.action_space)

    env.reset(seed=42)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
        else:
            # invalid action masking is optional and environment-dependent
            if "action_mask" in info:
                mask = info["action_mask"]
            elif isinstance(observation, dict) and "action_mask" in observation:
                mask = observation["action_mask"]
            else:
                mask = None
            action = env.action_space(agent).sample(mask) # this is where you would insert your policy

        print("Reward: {}".format(reward))
        print("Termination: {}".format(termination))
        print("Truncation: {}".format(truncation))
        print("Action: {}".format(action))
        print("Mask: {}".format(mask))
        print("Info: {}".format(info))
        if interactive:
            input("Press Button")

        env.step(action)

    env.close()

def main(category, env_name, api, interactive):

    if api == "aec":
        env = getattr(category, env_name).env(render_mode="human")
        aec_api(env, interactive)
    else:
        env = getattr(category, env_name).parallel_env(render_mode="human")
        parallel_api(env, interactive)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PettingZoo Environment Runner")
    parser.add_argument("--category", type=str, default="atari", help="Environment category")
    parser.add_argument("--env", type=str, default="double_dunk_v3", help="Name of the environment")
    parser.add_argument("--api", type=str, default="parallel", help="API type: aec or parallel")
    parser.add_argument("--interactive", type=str, default="0", help='Enable or disable interactive execution')
    args = parser.parse_args()
    print(args)

    if (args.category == "atari"):
        category = atari
    elif (args.category == "butterfly"):
        category = butterfly
    else:
        sys.exit(1)

    main(category, args.env, args.api, bool(int(args.interactive)))
