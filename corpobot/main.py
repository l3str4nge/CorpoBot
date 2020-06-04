import sys
import aioconsole
import asyncio
import click


CORPOBOT_VERION = "0.1"


class Application:
    def __init__(self):
        self.running = False

    async def run(self):
        self.running = True
        while self.running:
            _input = await aioconsole.ainput(prompt="Type command or `help` for list commands\n")

            await self.process_input(_input)
            await asyncio.sleep(0)

    async def process_input(self, _input):
            if _input == "help":
                await print_help()
            elif _input == "quit":
                self.running = False
            else:
                print(f"There is no command with name: {_input}")
                await print_help()

    async def stop(self):
        self.running = False
        await asyncio.sleep(0)


async def print_help():
    print(f"Following commands are available: get_tasks")


@click.command()
@click.option("--config", help="Your .env file location")
def main(config):
    """ CorpoBot is application which helps you automate boring tasks at work. """
    if not config:
        print("No .env file specified! Goodbye!")
        return
    print(f"Welcome to CorpoBot ! v.{CORPOBOT_VERION}")
    app = Application()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run())
    loop.close()


if __name__ == "__main__":
    sys.exit(main())
