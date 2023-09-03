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

from typing import Callable

import X


class OnDisconnect:
    def on_disconnect(self=None) -> Callable:
        """Decorator for handling disconnections.

        This does the same thing as :meth:`~X.Client.add_handler` using the
        :obj:`~X.handlers.DisconnectHandler`.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, X.Client):
                self.add_handler(X.handlers.DisconnectHandler(func))

            return func

        return decorator
