import discord
import re
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent for reading message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {message.author.mention}!')

    if message.content.startswith('Abelard'):
        await message.channel.send(f'Um almofadinha claramente homossexual')

    if message.content.startswith('Jacques'):
        await message.channel.send(f'Maluco do caralho')

    if message.content.startswith('Sal'):
        await message.channel.send(f'Botafogo é merda')

    if message.content.startswith('Maskelyne'):
        await message.channel.send(f'Contemplem o mago')



    # Updated code to handle the bxd pattern for rolling x number of 6-sided dice, quote the command, and bold ones, fives, and sixes
    match = re.match(r"^b(\d+)$", message.content)
    if match:
        dice_count = int(match.group(1))
        # Ensure the dice count is reasonable to prevent abuse
        if 1 <= dice_count <= 100:
            rolls = [random.randint(1, 6) for _ in range(dice_count)]
            # Apply bold formatting to ones, fives, and sixes
            bold_rolls = ['**1**' if roll == 1 else '**5**' if roll == 5 else '**6**' if roll == 6 else str(roll) for roll in rolls]
            successes = sum(1 for roll in rolls if roll >= 5)
            failures = sum(1 for roll in rolls if roll == 1)
            total = successes - failures
            response = (
                f"{message.author.mention} requested:\n"
                f"Command: `{message.content}`\n"
                f"Rolls: {', '.join(bold_rolls)}\n"
                f"Successes: {successes}\n"
                f"Failures: {failures}\n"
                f"Total: {total}"
            )
            # Log the dice roll results
            logging.info(f"Dice Roll by {message.author}: {response}")
            await message.channel.send(response)
        else:
            await message.channel.send("Dado pra caralho vai se fuder")



# Remember to replace the token with a valid one before running
client.run('MTIyNDA1NDUzMjU1Njg0OTIyMw.GQQbQU.Rbe3D5DVHOVedMtbH5y12WGr80HKl99A_tlHLs')

