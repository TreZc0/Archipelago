from CommonClient import CommonContext, ClientCommandProcessor, logger
# Python standard libraries
import asyncio
import json
import logging
import os
import subprocess
import sys

from asyncio import Task
from datetime import datetime
from logging import Logger
from typing import Awaitable

# Misc imports
import colorama
import pymem

from pymem.exception import ProcessNotFound

# Archipelago imports
import ModuleUpdate
import Utils

from CommonClient import ClientCommandProcessor, CommonContext, server_loop, gui_enabled
from NetUtils import ClientStatus


class UnlockerClient(CommonContext):
    game = "Unlocker"


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TextContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="unlocker")

    async def on_package(self, cmd: str, args: dict):
        # Handle custom server commands for Unlocker
        if cmd == "ReceivedItems":
            await self.on_items_received(args["items"])
        else:
            await super().on_package(cmd, args)

    async def on_items_received(self, items):
        for item in items:
            item_name = self.item_id_to_name(item["item"])
            logger.info(f"Received item: {item_name}")
            #check the location with the same id as the item
            location = self.locations.get(item["location"])
            self.check_locations(location)

    def unlock_item(self, item_name: str):
        # Implement actual unlock logic here
        logger.info(f"Unlocking item: {item_name}")

    def item_id_to_name(self, item_id):
        # Map item_id to item name using your data package
        return self.item_names.lookup_in_game(item_id, self.game)





async def main():
    Utils.init_logging("UnlockerClient", exception_logger="Client")

    ctx = UnlockerClient(None, None)


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
