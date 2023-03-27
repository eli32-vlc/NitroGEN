import random
import time
import string
from discord_webhook import DiscordWebhook

for i in range(100):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1090025944238006302/_fOmQE_TivnnCyy1eVOZdX6XXdd5q1-g2CCy1VzOvCtiZ99QeEp02o8i5D7PQ8xoy7Z1', content='discord.gift/'+code)
    response = webhook.execute()
    time.sleep(1)