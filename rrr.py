from telethon import TelegramClient, events

api_id = 20298721           # your API ID
api_hash = "7b406803e5ea47aeddf12f9d9ffc4e2d"  # your API Hash

client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage)
async def print_chat_id(event):
    # Only print the chat ID for this group
    print(f"Chat name: {event.chat.title if event.chat else 'Private Chat'}")
    print(f"Chat ID: {event.chat_id}")

client.start()
client.run_until_disconnected()
