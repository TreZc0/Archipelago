from .bases import ALttPRTestBaseNoDefaultTests


class TestCannotFluteInRainState(ALttPRTestBaseNoDefaultTests):
    options = {
        "start_inventory": {"Ocarina (Activated)": 1},
        "world_mode": "standard",
        "pre_activated_flute": True,
    }

    def test_cannot_flute_in_rain_state(self):
        assert not self.can_reach_region("Kakariko Village"), "Can Flute to Kak despite having not completed the Escape sequence in a Standard start."
