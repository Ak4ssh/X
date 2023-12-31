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

from typing import Optional

import X
from X import raw, enums
from X import types
from ..object import Object


class MessageEntity(Object):
    """One special entity in a text message.
    
    For example, hashtags, usernames, URLs, etc.

    Parameters:
        type (:obj:`~X.enums.MessageEntityType`):
            Type of the entity.

        offset (``int``):
            Offset in UTF-16 code units to the start of the entity.

        length (``int``):
            Length of the entity in UTF-16 code units.

        url (``str``, *optional*):
            For "text_link" only, url that will be opened after user taps on the text.

        user (:obj:`~X.types.User`, *optional*):
            For "text_mention" only, the mentioned user.

        language (``str``. *optional*):
            For "pre" only, the programming language of the entity text.
    """

    def __init__(
        self,
        *,
        client: "X.Client" = None,
        type: "enums.MessageEntityType",
        offset: int,
        length: int,
        url: str = None,
        user: "types.User" = None,
        language: str = None
    ):
        super().__init__(client)

        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language

    @staticmethod
    def _parse(client, entity: "raw.base.MessageEntity", users: dict) -> Optional["MessageEntity"]:
        return MessageEntity(
            type=enums.MessageEntityType(entity.__class__),
            offset=entity.offset,
            length=entity.length,
            url=getattr(entity, "url", None),
            user=types.User._parse(client, users.get(getattr(entity, "user_id", None), None)),
            language=getattr(entity, "language", None),
            client=client
        )

    async def write(self):
        args = self.__dict__.copy()

        for arg in ("_client", "type", "user"):
            args.pop(arg)

        if self.user:
            args["user_id"] = await self._client.resolve_peer(self.user.id)

        if not self.url:
            args.pop("url")

        if self.language is None:
            args.pop("language")

        entity = self.type.value

        if entity is raw.types.MessageEntityMentionName:
            entity = raw.types.InputMessageEntityMentionName

        return entity(**args)
