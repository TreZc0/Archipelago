from .bases import ALttPRTestBaseNoDefaultTests
from .data import slot_data_crossed, slot_data_inverted_flute_shuffle


class TestBigBombDefaultSettings(ALttPRTestBaseNoDefaultTests):
    options = {
        "prize_shuffle": True,
        "start_inventory": {"Crystal 5": 1, "Crystal 6": 1, "Progressive Glove": 2, "Moon Pearl": 1, "Flippers": 1}
    }

    def test_big_bomb_open(self):
        self.collect_by_name("Bombos")  # Forcing the accessible locations to update after setup
        assert self.can_reach_location("Pyramid")
        self.assertCanReachWith(["Pyramid Fairy - Left", "Pyramid Fairy - Right"], "location", [["Hammer"], ["Magic Mirror", "Beat Agahnim 1"]])


class TestBigBombEntranceShuffle(ALttPRTestBaseNoDefaultTests):
    auto_construct = False
    options = {
        "prize_shuffle": True,
        "start_inventory": {"Crystal 5": 1, "Crystal 6": 1},
        "test_slot_data": {},
    }

    def test_big_bomb_shop_in_kak(self):
        slot_data = slot_data_crossed.slot_data.copy()
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Red Shield Shop"
        slot_data["entrances"][1]["entrances"]["Kakariko Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachWith(["Pyramid Crack"],  "entrance", [
            ["Beat Agahnim 1"],
            ["Progressive Glove", "Hammer", "Moon Pearl"],
        ])
        self.assertCanNotReachWith(["Pyramid Crack"], "entrance", [["Progressive Glove", "Progressive Glove", "Flippers", "Moon Pearl"]])


    def test_big_bomb_shop_in_light_world_needs_flute(self):
        # Checking light world entrances which require Flute to carry the Big Bomb.
        # This will have to be rewritten if the slot data changes, so there aren't any duplicate entrances.
        entrances_to_test = {
            #"Cave 45": "Paradox Cave Exit (Bottom)",
            "Desert Palace Entrance (South)": "Bumper Cave Exit (Top)",
            "Desert Palace Entrance (West)": "Lake Hylia Fortune Teller",
            "Capacity Upgrade": "Desert Palace Exit (East)",
            "Two Brothers House (West)": "Bonk Fairy (Light)",
            "Waterfall of Wishing": "Desert Healer Fairy",
            "Death Mountain Return Cave (West)": "Death Mountain Return Cave Exit (East)",
            "Old Man Cave (East)": "Hookshot Fairy",  # Only grabbing one example from DM since they all have the same logic
        }

        for entrance, connected_region in entrances_to_test.items():
            with self.subTest(entrance=entrance, connected_region=connected_region):
                slot_data = slot_data_crossed.slot_data.copy()
                slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = connected_region
                slot_data["entrances"][1]["entrances"][entrance] = "Big Bomb Shop"
                self.options["test_slot_data"] = slot_data
                self.world_setup()

                self.assertCanReachWith(["Pyramid Crack"],  "entrance", [
                    ["Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"]
                ])
                self.assertCanNotReachWith(["Pyramid Crack"], "entrance", [
                    ["Beat Agahnim 1"],
                    ["Progressive Glove", "Hammer", "Moon Pearl"],
                ])


    def test_big_bomb_shop_in_east_dark_world(self):
        slot_data = slot_data_crossed.slot_data.copy()
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Archery Game"
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.can_reach_entrance("Pyramid Crack")


    def test_big_bomb_shop_in_north_dark_world(self):
        slot_data = slot_data_crossed.slot_data.copy()
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "20 Rupee Cave"
        slot_data["entrances"][1]["entrances"]["Thieves Town"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachWith(["Pyramid Crack"],  "entrance", [
            ["Magic Mirror", "Beat Agahnim 1"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"],
        ])
        self.assertCanNotReachWith(["Pyramid Crack"], "entrance", [["Progressive Glove", "Flippers", "Moon Pearl"]])


    def test_big_bomb_shop_dark_world_mirror_then_walk(self):
        # Entrances in the dark world where you must use the Mirror, but can then walk the Big Bomb to another portal
        entrances_to_test = {
            "Red Shield Shop": "Mimic Cave",
            "Dark Lake Hylia Ledge Fairy": "Big Bomb Shop",
            "Mire Fairy": "Aginahs Cave",
            "Checkerboard Cave": "Chest Game",  # TODO: Overworld Glitches could also use Flute
            "Skull Woods Final Section": "Lake Hylia Shop",
        }

        for entrance, connected_region in entrances_to_test.items():
            with self.subTest(entrance=entrance, connected_region=connected_region):
                slot_data = slot_data_crossed.slot_data.copy()
                slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = connected_region
                slot_data["entrances"][1]["entrances"][entrance] = "Big Bomb Shop"
                self.options["test_slot_data"] = slot_data
                self.world_setup()

                self.assertCanReachWith(["Pyramid Crack"],  "entrance", [
                    ["Magic Mirror", "Beat Agahnim 1"],
                    ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
                ])
                self.assertCanNotReachWith(["Pyramid Crack"], "entrance", [["Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])


    def test_big_bomb_shop_dark_world_mirror_then_flute(self):
        # Entrances in the dark world where you need both Mirror and Flute to get to the Pyramid
        entrances_to_test = {
            "Ice Palace": "Dark Lake Hylia Shop",  # TODO: Overworld Glitch implications?
            "Bumper Cave (Top)": "Fairy Ascension Cave Exit (Bottom)",
            "Dark Death Mountain Fairy": "Superbunny Cave Exit (Bottom)",  # Representing any dark Death Mountain entrance
        }

        for entrance, connected_region in entrances_to_test.items():
            with self.subTest(entrance=entrance, connected_region=connected_region):
                slot_data = slot_data_crossed.slot_data.copy()
                slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = connected_region
                slot_data["entrances"][1]["entrances"][entrance] = "Big Bomb Shop"
                self.options["test_slot_data"] = slot_data
                self.world_setup()

                self.assertCanReachWith(["Pyramid Crack"], "entrance", [
                    ["Magic Mirror", "Ocarina (Activated)", "Beat Agahnim 1"],
                    ["Magic Mirror", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
                ])
                self.assertCanNotReachWith(["Pyramid Crack"], "entrance",
                                           [["Magic Mirror", "Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])

    # TODO: Dark Potion Shop
    def test_big_bomb_shop_at_dark_potion_shop(self):
        slot_data = slot_data_crossed.slot_data.copy()
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Dam"
        slot_data["entrances"][1]["entrances"]["Dark Potion Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachWith(["Pyramid Crack"],  "entrance", [
            ["Progressive Glove"],
            ["Magic Mirror", "Ocarina (Activated)", "Beat Agahnim 1"],
        ])


class TestBigBombInverted(ALttPRTestBaseNoDefaultTests):
    options = {
        "world_mode": "inverted",
        "prize_shuffle": True,
        "start_inventory": {"Crystal 5": 1, "Crystal 6": 1, "Flippers": 1, "Progressive Glove": 1}
    }

    def test_big_bomb_inverted(self):
        self.collect_by_name("Bombos")  # Forcing the accessible locations to update after world_setup
        assert self.can_reach_location("Pyramid")
        self.assertCanReachWith(["Pyramid Fairy - Left", "Pyramid Fairy - Right"], "location",
        [["Hammer"], ["Ocarina (Activated)"], ["Magic Mirror", "Progressive Glove", "Moon Pearl"]])


class TestBigBombInvertedFluteShuffle(ALttPRTestBaseNoDefaultTests):
    auto_construct = False
    options = {
        "world_mode": "inverted",
        "prize_shuffle": True,
        "flute_shuffle": "chaos",
        "start_inventory": {"Crystal 5": 1, "Crystal 6": 1, "Flippers": 1},
        "test_slot_data": {},
    }

    def test_big_bomb_inverted_flute_to_catfish(self):
        # TODO: Why is this passing? Something seems wrong
        # When the only Flute to east Dark World is near Catfish
        slot_data = slot_data_inverted_flute_shuffle.slot_data.copy()
        slot_data["ow-flutespots"][1] = [0, 2, 3, 10, 15, 16, 19, 48]
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        assert self.can_reach_location("Pyramid")
        self.assertCanReachWith(["Pyramid Fairy - Left", "Pyramid Fairy - Right"], "location",
                                        [["Hammer"],
                                                        ["Ocarina (Activated)", "Progressive Glove"],  # Flute to catfish
                                                        ["Ocarina (Activated)", "Lamp", "Magic Mirror"],  # Flute to DM -> Light World DM -> DMD -> walk to Bomb Shop
                                                        ["Magic Mirror", "Progressive Glove", "Progressive Glove", "Moon Pearl"]])


    def test_big_bomb_inverted_flute_no_east_dark_world(self):
        # There are no Flute spots in east dark world
        slot_data = slot_data_inverted_flute_shuffle.slot_data
        slot_data["ow-flutespots"][1] = [0, 2, 3, 10, 16, 17, 19, 48]
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        assert self.can_reach_location("Pyramid")
        self.assertCanNotReachWith(["Pyramid Fairy - Left", "Pyramid Fairy - Right"], "location", [["Ocarina (Activated)", "Progressive Glove"]])
