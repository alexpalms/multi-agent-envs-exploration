import argparse
from pettingzoo import atari

def main(game_name):
    env = getattr(atari, game_name).env(render_mode="human")
    env.reset(seed=42)

    print("Observations space")
    print(env.observation_space)

    print("Action space")
    print(env.action_space)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
        else:
            action = env.action_space(agent).sample()  # this is where you would insert your policy

        print("Termination: {}".format(termination))
        print("Truncation: {}".format(truncation))
        print("Action: {}".format(action))

        env.step(action)
    env.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PettingZoo Atari Game Runner")
    parser.add_argument("--game", type=str, default="double_dunk_v3", help="Name of the game")
    args = parser.parse_args()

    main(args.game)
