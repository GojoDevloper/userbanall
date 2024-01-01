import modules.client, modules.ping, modules.banall

client = modules.client.client

with client as gojo:
    gojo.add_event_handler(modules.ping.runping)

with client as gojo:
    gojo.add_event_handler(modules.banall.runfba)

client.start()
print("Gojo Started")
client.run_until_disconnected()