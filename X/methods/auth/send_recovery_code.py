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

import logging

import X
from X import raw

log = logging.getLogger(__name__)


class SendRecoveryCode:
    async def send_recovery_code(
        self: "X.Client",
    ) -> str:
        """Send a code to your email to recover your password.

        Returns:
            ``str``: On success, the hidden email pattern is returned and a recovery code is sent to that email.

        Raises:
            BadRequest: In case no recovery email was set up.
        """
        return (await self.invoke(
            raw.functions.auth.RequestPasswordRecovery()
        )).email_pattern
