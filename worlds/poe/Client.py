import asyncio
import colorama
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, server_loop, gui_enabled
from .poeClient import main as poe_main
from .poeClient import gggAPI


def sync_run_async(coroutine):
    """Run an async coroutine in a synchronous context.
    If an event loop is already running, it creates a task and returns a Future.
    If no event loop is running, it uses asyncio.run to execute the coroutine.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No event loop running, safe to use asyncio.run
        return asyncio.run(coroutine)
    else:
        # Already in an event loop, create a task and return a Future
        return asyncio.create_task(coroutine)

class PathOfExileCommandProcessor(ClientCommandProcessor):


    def _cmd_testing(self) -> bool:
        """A test command to check if the command processor is working."""
        return True

    def _cmd_poe_auth(self) -> bool:
        """Authenticate with Path of Exile's OAuth2 service."""
        sync_run_async(gggAPI.request_new_access_token())



    def _cmd_poe_char_name(self, character_name: str = "") -> bool:
        """Set the character name for the Path of Exile client."""
        poe_main.character_name = character_name
        if not character_name:
            self.output("ERROR: Please provide a character name.")
            return False
        else:
            self.output(f"Character name set to: {character_name}")

    def _cmd_start_poe(self) -> bool:
        """Start the Path of Exile client."""
        if not poe_main.character_name:
            self.output("ERROR: Please set your character name first using 'poe_char_name <name>'.")
            return False
        self.output(f"Starting Path of Exile client for character: {poe_main.character_name}")
        poe_main.run(self.ctx)
        return True


class PathOfExileContext(CommonContext):
    game = "Path of Exile"
    command_processor = PathOfExileCommandProcessor
    items_handling = 0b111
    _debug = True  # Enable debug mode for poe client

    item_name_to_unlocker_location = {} # remove this I think?
    required_for_finish_player_location_table = {}
    item_id_to_location_name = {}

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TextContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="Path of Exile")

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            pass
        if cmd == "ReceivedItems":
            pass
        super().on_package(cmd, args)


    def run_gui(self) -> None:
        #from .ClientGui import start_gui # custom UI

        #

        #start_gui(self)
        super().run_gui()






async def main():
    Utils.init_logging("PathOfExileContext", exception_logger="Client")

    ctx = PathOfExileContext(None, None)


    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch():
    # use colorama to display colored text highlighting
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()
