# GeoFriends2 v2

An OpenAI Gym environment with complex puzzle maps, highly adequate for single- or multi-agent reinforcement learning approaches, based on [Geometry Friends](http://gaips.inesc-id.pt/geometryfriends/) and [GeoFriends2](https://github.com/bluemoon93/GeoFriends2).

![Demo](https://raw.githubusercontent.com/bluemoon93/GeoFriends2-v2/master/MapGenerators/TwoHighTowers.png)

To ready the environment, we recommend using VirtualEnv. You will need the [PyGame](https://www.pygame.org/news) and [Gym](https://github.com/openai/gym) environments.

    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install pygame gym
    python TestEnv-GUI.py

If you don't want a GUI, for example for Machine Learning approaches, then you can run this for a continuous local observation for each agent:

    python TestEnv.py

Or this for a graphical global state observation (pixels):

    python TestEnv-GraphicalState.py

## Description

The major classes are the [Agent](https://github.com/bluemoon93/GeoFriends2-v2/blob/master/Players/Agent.py), [MapGenerator](https://github.com/bluemoon93/GeoFriends2-v2/blob/master/MapGenerators/MapGenerator.py), and [GeoFriends2](https://github.com/bluemoon93/GeoFriends2-v2/blob/master/Simulator/Geofriends2.py). 

The Gym simulator is GeoFriends2, which you initialize with a list of Agents and a list of MapGenerators. To add new Agents, you need to re-implement the Agent class (there already are a Circle and a Rectangle agents). For new Maps, you re-implement the MapGenerator. There are a bunch of maps already implemented and associated images.