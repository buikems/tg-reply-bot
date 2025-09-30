import re
from telethon import TelegramClient, events

api_id = 123456
api_hash = "your_api_hash_here"

client = TelegramClient("session_name", api_id, api_hash)

# Allowed groups (replace with your 6 group IDs)
allowed_groups = [
    -4866948235,  # kems kems
    -1002858440892,  # hunters
    -1002463164095,  # openspace
    -1002338960004,  # x lambo
    -1002813798895,  # pea demo
    -1002729739716   # Prime Engagement Agency (PEA)
]

auto_reply = "up"

# Keywords
people_keywords = ["raider", "raiders", "guy", "guys", "person", "people", "replacement", "replacements"]
job_keywords = ["job", "demo", "team"]

@client.on(events.NewMessage)
async def handler(event):
    if event.chat_id not in allowed_groups:
        return  # Ignore other chats

    text = event.raw_text.lower()
    
    # Check if message contains "need" and a number
    if "need" in text and re.search(r"\d+", text):
        # Check for people keywords
        if any(word in text for word in people_keywords):
            # Check for job/demo/team keywords
            if any(word in text for word in job_keywords):
                await event.reply(auto_reply)

client.start()
print("Userbot running...")
client.run_until_disconnected()
