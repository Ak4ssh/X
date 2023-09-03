#  X - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of X.
#
#  X is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  X is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with X.  If not, see <http://www.gnu.org/licenses/>.

import X
from X import raw
from .menu_button import MenuButton


class MenuButtonCommands(MenuButton):
    """A menu button, which opens the bot's list of commands.
    """

    def __init__(self):
        super().__init__("commands")

    async def write(self, client: "X.Client") -> "raw.types.BotMenuButtonCommands":
        return raw.types.BotMenuButtonCommands()