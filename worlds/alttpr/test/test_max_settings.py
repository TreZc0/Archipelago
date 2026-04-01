from .bases import ALttPRTestBase


# Testing if someone goes crazy and enables every setting they can.
class TestMaxSettings(ALttPRTestBase):
    options = {
        "world_mode": "standard",
        "goal": "triforcehunt",
        "open_pyramid": "auto",
        "crystals_needed_for_ganon": 6,
        "triforce_hunt_goal": 50,
        "triforce_hunt_total": 50,
        "entrance_shuffle": "crossed",
        "map_shuffle": "true",
        "compass_shuffle": "true",
        "small_key_shuffle": "true",
        "big_key_shuffle": "true",
        "pseudoboots": "true",
        "mirror_scroll": "true",
        "zelgawoods": "true",
    }