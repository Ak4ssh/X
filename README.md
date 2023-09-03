<p align="center">
    <a href="https://github.com/X/X">
        <img src="https://docs.X.org/_static/X.png" alt="X" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://docs.X.org">
        Documentation
    </a>
    •
    <a href="https://docs.X.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/X">
        News
    </a>
</p>

## X

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from X import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from X!")


app.run()
```

**X** is a modern, elegant and asynchronous [MTProto API](https://docs.X.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support X, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/X).

### Key Features

- **Ready**: Install X with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/X/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install X
```

### Resources

- Check out the docs at https://docs.X.org to learn more about X, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/X and stay tuned for news, updates and announcements.