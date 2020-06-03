import sys
import aioconsole
import asyncio
import click


CORPOBOT_VERION = "0.1"


async def get_input():
    while True:
        _input = await aioconsole.ainput(prompt="Type command or `help` for list commands\n")

        if _input == "help":
            await print_help()
        else:
            print(f"There is no command with name: {_input}")
            await print_help()


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
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_input())
    loop.close()


if __name__ == "__main__":
    sys.exit(main())
