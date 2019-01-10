from MapGenerators.Basic import Basic
from MapGenerators.Corners import Corners
from MapGenerators.Dome import Dome
from MapGenerators.Floors import Floors
from MapGenerators.HighPlatform import HighPlatform
from MapGenerators.Pyramid import Pyramid
from MapGenerators.Split import Split
from MapGenerators.TwoFloors import TwoFloors
from MapGenerators.TwoHighTowers import TwoHighTowers
from MapGenerators.TwoTowers import TwoTowers
from Players.Circle import Circle
from Players.Rectangle import Rectangle
from Simulator.Geofriends2 import GeometryFriends2

agent_rectangle = Rectangle(can_interrupt_growth=False)
agent_circle = Circle()

circle_maps = [Basic(), HighPlatform(), Corners(), Pyramid(), TwoTowers()]
rect_maps = [Basic(), HighPlatform(), Floors(), TwoFloors()]
all_maps = [Basic(), TwoHighTowers(), Split(), Dome()]

environment = GeometryFriends2([agent_rectangle, agent_circle], all_maps,
                               agent_collision=True)

for trial_number in range(3):
    observation, additional_information = environment.reset()
    environment.render()
    print("Obstacles", [str(obs) for obs in additional_information["obstacles"]])
    print(observation[0])       # Rectangle's internal state, Circle's external state, rewards
    print(observation[1])       # Circle's internal state, Rectangle's external state, rewards

    while True:
        action = environment.action_space.sample()  # take a random action
        observation, reward, terminal, additional_information = environment.step(action)  # step
        environment.render()

        #print(observation[0])  # Rectangle's internal state, Circle's external state, rewards
        #print(observation[1])  # Circle's internal state, Rectangle's external state, rewards

        if reward != 0:
            print("Got " + str(reward) + " points")

        if terminal:
            print("Episode over")
            break

environment.close()
