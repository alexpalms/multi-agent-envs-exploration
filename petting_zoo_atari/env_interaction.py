from pettingzoo.atari import space_invaders_v2

def main():

    env = space_invaders_v2.env(render_mode="human")
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
            action = env.action_space(agent).sample() # this is where you would insert your policy

        print("Termination: {}".format(termination))
        print("Truncation: {}".format(truncation))
        print("Action: {}".format(action))

        env.step(action)
    env.close()

if __name__ == "__main__":
    main()