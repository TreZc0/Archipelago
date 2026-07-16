from test.bases import WorldTestBase


class ALttPRTestBase(WorldTestBase):
    game = "The Legend of Zelda: A Link to the Past"


class ALttPRTestBaseNoDefaultTests(ALttPRTestBase):
    @property
    def run_default_tests(self):
        return False