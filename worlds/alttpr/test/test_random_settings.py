from .bases import ALttPRTestBase


class TestRandomSettings(ALttPRTestBase):
    options = {
        "world_mode": "random",
        "goal": "random",
        "open_pyramid": "random",
        "crystals_needed_for_ganons_tower": "random",
        "crystals_needed_for_ganon": "random",
        "triforce_hunt_goal": "random-range-1-30",
        "triforce_hunt_total": "random-range-30-50",
        "map_shuffle": "random",
        "compass_shuffle": "random",
        "small_key_shuffle": "random",
        "big_key_shuffle": "random",
        "key_drop_shuffle": "random",
        "entrance_shuffle": "random",
        "zelgawoods": "random",
        "enemy_shuffle": "random",
        "boss_shuffle": "random",
        "shopsanity": "random",
        "prize_shuffle": "random",
        "flute_shuffle": "random",
        "pre_activated_flute": "random",
        "pseudoboots": "random",
        "mirror_scroll": "random",
        "heart_beep_rate": "random",
        "heart_color": "random",
        "fast_menu": "random",
        "disable_music": "random",
        "msu_resume": "random",
    }