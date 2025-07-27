import asyncio
from random import Random

from typing import TYPE_CHECKING

    

import colorama
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, server_loop, gui_enabled
from settings import Path

from .poeClient.fileHelper import load_settings, save_settings
from .poeClient import main as poe_main
from .poeClient import gggAPI


def sync_run_async(coroutine):
    """Run an async coroutine in a synchronous context.
    If an event loop is already running, it creates a task and returns a Future.
    If no event loop is running, it uses asyncio.run to execute the coroutine.
    """
    try:
        loop = asyncio.get_running_loop() # this will raise RuntimeError if no event loop is running.
        # Use the thread-safe method
        future = asyncio.run_coroutine_threadsafe(coroutine, loop)
        return future.result(timeout=60)
    except RuntimeError:
        # No event loop running, safe to use asyncio.run
        return asyncio.run(coroutine)

class PathOfExileCommandProcessor(ClientCommandProcessor):
    if TYPE_CHECKING:
        ctx: "PathOfExileContext"
        
#    def _cmd_test_tts(self) -> bool:
#        from .poeClient import tts
#
#        import worlds.poe.Items as Items
#        # mock a context with missing locations, player names, and item lookup and such
#        class mockCtx:
#            class mock_network_item:
#                def __init__(self, item, player):
#                    self.item = item
#                    self.player = player
#
#            class mock_item_names:
#                def lookup_in_slot(self, item, player):
#                    # Mock item names lookup
#                    return f"ItemName_{str(item)} for Player{player}"
#
#            def __init__(self):
#                self.missing_locations = list(Items.item_table.keys())
#                self.locations_info = {
#                    loc_id: self.mock_network_item(item, player)
#                    for (loc_id, item), player in zip(Items.item_table.items(), range(1, len(Items.item_table) + 1))
#                }
#                self.player_names = {player_id: f"Player{player_id}" for player_id in
#                                     range(1, len(Items.item_table) + 1)}
#                self.item_names = self.mock_item_names()
#
#        mctx = mockCtx()
#        tts.generate_tts_tasks_from_missing_locations(mctx)
#        tts.run_tts_tasks()

    def _cmd_generate_tts(self) -> bool:
        """Generate TTS for missing locations."""
        from .poeClient import tts

        if not self.ctx.missing_locations:
            self.output("No missing locations to generate TTS for, are you connected to the server?")
            return False

        tts.generate_tts_tasks_from_missing_locations(self.ctx)
        tts.run_tts_tasks()
        return True

    def _cmd_poe_auth(self) -> bool:
        """Authenticate with Path of Exile's OAuth2 service."""
        sync_run_async(gggAPI.request_new_access_token())

    def _cmd_set_client_text_path(self, path: str) -> bool:
        """Set the path to the Path of Exile client text file. (Use )"""
        if not path:
            self.output("ERROR: Please provide a valid path to the client text file.")
            return False
        if not Path(path).exists():
            self.output(f"ERROR: The provided path does not exist: {path}")
            return False
        
        self.ctx.client_text_path = Path(path)
        poe_main.path_to_client_txt = self.ctx.client_text_path
        self.ctx.update_settings()
        self.output(f"Client text path set to: {path}")
        return True

    def _cmd_char_name(self, character_name: str = "") -> bool:
        """Set the character name for the Path of Exile client."""
        if not character_name:
            self.output("ERROR: Please provide a character name.")
            return False
        self.ctx.character_name = character_name
        self.ctx.update_settings()
        self.output(f"Character name set to: {character_name}")
        

    #def _cmd_set_current_character(self) -> bool:
    #    self.ctx.player_verify_code = Random.randint()

    def _cmd_base_item_filter(self, filter_name: str) -> bool:
        """Set the base item filter. (do not add the .filter extension)"""
        if not filter_name:
            self.output("ERROR: Please provide a valid item filter name.")
            return False
        self.ctx.base_item_filter = filter_name
        self.ctx.update_settings()  # Save the settings
        self.output(f"Base item filter set to: {filter_name}")
        return True

    def _cmd_start_poe(self) -> bool:
        """Start the Path of Exile client."""
        #required
        if not self.ctx.client_text_path:
            self.output("Please set the client text path using the 'poe_client_text_path <path>' command.")
            return False
        
        #optional to start
        if not self.ctx.character_name:
            self.output("Please set your character name using when in game typing '!ap char', or by using the 'poe_char_name <name> command'.")
        if not self.ctx.base_item_filter:
            self.output("If you would like to use a custom item filter, please set the base item filter using the 'poe_base_item_filter <filter_name>' command.")

        self.output(f"Starting Path of Exile client for character: {self.ctx.character_name}")
        poe_main.client_start(self.ctx)
        return True

    def _cmd_t(self):
        """A test command to check if the command processor is working. -- This is a placeholder for testing purposes."""
#        self._cmd_connect("Player1:@localhost:38281")
        # wait 4 seconds to allow the character name to be set
        #self._cmd_poe_char_name("_ap_test_one")

        self._cmd_received()

        self._cmd_start_poe()




class PathOfExileContext(CommonContext):
    game = "Path of Exile"
    command_processor = PathOfExileCommandProcessor
    items_handling = 0b111
    
    last_response_from_api = {}
    character_name: str = ""
    client_text_path: Path = ""
    base_item_filter: str = ""
    _debug = True  # Enable debug mode for poe client

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="Path of Exile")

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == 'Connected':
            # Request info for all locations after connecting
            location_ids = list(self.missing_locations)
            sync_run_async(self.send_msgs([{"cmd": "LocationScouts", "locations": location_ids}]))

            # load the client settings
            settings = sync_run_async(load_settings(self))
            if settings:
                self.client_text_path = settings.get("client_txt", self.client_text_path)
                self.character_name = settings.get("last_char", self.character_name)
                self.base_item_filter = settings.get("base_item_filter", self.base_item_filter)
                if self._debug:
                    print(f"[DEBUG] Loaded settings: {settings}")
    
    def update_settings(self):
        """Update a setting and save it to the settings file."""
        sync_run_async(save_settings(self))
        

    def run_gui(self) -> None:
        #from .ClientGui import start_gui # custom UI

        #

        #start_gui(self)
        super().run_gui()


async def main():
    Utils.init_logging("PathOfExileContext", exception_logger="Client")

    ctx = PathOfExileContext(None, None)


    #if gui_enabled:
    if True: # we can disable GUI for testing here
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch():
    # use colorama to display colored text highlighting
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()