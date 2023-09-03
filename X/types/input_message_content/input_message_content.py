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

from ..object import Object

"""- :obj:`~X.types.InputLocationMessageContent`
    - :obj:`~X.types.InputVenueMessageContent`
    - :obj:`~X.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    X currently supports the following types:

    - :obj:`~X.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "X.Client", reply_markup):
        raise NotImplementedError
