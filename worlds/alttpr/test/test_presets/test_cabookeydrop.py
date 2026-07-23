from bases import ALttPRTestBase


class TestCabookeydrop(ALttPRTestBase):
    options = {
        "world_mode": "standard",
        "goal": "dungeons",
        "open_pyramid": "closed",
        "map_shuffle": "true",
        "compass_shuffle": "true",
        "small_key_shuffle": "true",
        "big_key_shuffle": "true",
        "key_drop_shuffle": "true",
        "start_inventory": {"Pegasus Boots": 1, "Progressive Sword": 1}
    }