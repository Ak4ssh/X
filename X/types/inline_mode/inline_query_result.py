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

from uuid import uuid4

import X
from X import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~X.types.InlineQueryResultCachedAudio`
    - :obj:`~X.types.InlineQueryResultCachedDocument`
    - :obj:`~X.types.InlineQueryResultCachedAnimation`
    - :obj:`~X.types.InlineQueryResultCachedPhoto`
    - :obj:`~X.types.InlineQueryResultCachedSticker`
    - :obj:`~X.types.InlineQueryResultCachedVideo`
    - :obj:`~X.types.InlineQueryResultCachedVoice`
    - :obj:`~X.types.InlineQueryResultArticle`
    - :obj:`~X.types.InlineQueryResultAudio`
    - :obj:`~X.types.InlineQueryResultContact`
    - :obj:`~X.types.InlineQueryResultDocument`
    - :obj:`~X.types.InlineQueryResultAnimation`
    - :obj:`~X.types.InlineQueryResultLocation`
    - :obj:`~X.types.InlineQueryResultPhoto`
    - :obj:`~X.types.InlineQueryResultVenue`
    - :obj:`~X.types.InlineQueryResultVideo`
    - :obj:`~X.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "X.Client"):
        pass
