# GeoFriends2 v2

An OpenAI Gym environment with complex puzzle maps, highly adequate for single- or multi-agent reinforcement learning approaches, based on [Geometry Friends](http://gaips.inesc-id.pt/geometryfriends/) and [GeoFriends2](https://github.com/bluemoon93/GeoFriends2).

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

The major classes