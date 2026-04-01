from .bases import ALttPRTestBase


class TestCasualBoots(ALttPRTestBase):
    options = {
        "start_inventory": {"Pegasus Boots": 1, "Progressive Sword": 1},
        "world_mode": "standard",
    }