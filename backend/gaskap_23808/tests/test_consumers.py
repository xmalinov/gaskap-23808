import pytest
from rest_framework.test import APITestCase
from channels.testing import WebsocketCommunicator
from gaskap_23808.routing import application


class ChatConsumerTest(APITestCase):
    @pytest.mark.asyncio
    async def test_send_and_receive(self):
        communicator = WebsocketCommunicator(application, "/api/chats/test/")
        connected, subprotocol = await communicator.connect()
        print("=== Connected ===", connected)
        self.assertTrue(connected)
