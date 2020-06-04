from unittest import mock
from unittest import IsolatedAsyncioTestCase
from corpobot.main import Application


class TestUserInput(IsolatedAsyncioTestCase):

    @mock.patch("corpobot.main.print_help")
    async def test_print_help(self, print_help):
        app = Application()
        await app.process_input("help")
        self.assertTrue(print_help.called)
