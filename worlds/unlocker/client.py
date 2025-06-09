import asyncio
import Utils
import websockets
import functools
from copy import deepcopy
from typing import List, Any, Iterable
from NetUtils import decode, encode, JSONtoTextParser, JSONMessagePart, NetworkItem, NetworkPlayer
from MultiServer import Endpoint
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser
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



import logging

logger = logging.getLogger("UnlockerClient")

class UnlockerClient(CommonClient):
    game = "Unlocker"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_items_received(self, items):
        """
        Called when items are received from the server.
        `items` is a list of dicts with keys: item, location, player, flags.
        """
        for item in items:
            item_name = self.item_id_to_name(item["item"])
            logger.info(f"Item received: {item_name}")
            self.unlock_item(item_name)
            await self.send_item(item_name)

    def unlock_item(self, item_name: str):
        logger.info(f"Unlocking item: {item_name}")
        # ...actual unlock logic...

    async def send_item(self, item_name: str):
        logger.info(f"Sending item: {item_name}")
        # Example: send a custom message to the server
        await self.send_msgs([{
            "cmd": "Bounce",
            "tags": ["Unlocker", "ItemSend"],
            "data": {"item_name": item_name, "player": self.slot}
        }])

    def item_id_to_name(self, item_id):
        # Implement this mapping based on your item table
        # For now, just return str(item_id)
        return str(item_id)
