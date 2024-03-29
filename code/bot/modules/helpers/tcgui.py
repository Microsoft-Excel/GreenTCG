"""Contains discord.ui views to let the user interact with the bot ui."""

import discord
from discord import ui

from modules.helpers import embeds

class OpenChallenge(ui.View):

    def __init__(self, *, challenger: discord.User, accept_callback, cancel_callback):
        super().__init__()
        self.challenger = challenger
        self.accept_callback = accept_callback
        self.cancel_callback = cancel_callback

    @ui.button(label='Accept', style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.challenger.id:
            await interaction.response.send_message(f"You can't accept your own challenge!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.accept_callback(interaction)
        self.stop()

    @ui.button(label='Cancel', style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.challenger.id:
            await interaction.response.send_message(f"I'm sorry, only {self.challenger.display_name} can cancel to this challenge!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.cancel_callback(interaction)
        self.stop()

class ClosedChallenge(ui.View):

    def __init__(self, *, challenger: discord.User, opponent: discord.User, accept_callback, decline_callback, cancel_callback):
        super().__init__()
        self.challenger = challenger
        self.opponent = opponent
        self.accept_callback = accept_callback
        self.decline_callback = decline_callback
        self.cancel_callback = cancel_callback

    @ui.button(label='Accept', style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.opponent.id:
            await interaction.response.send_message(f"I'm sorry, only {self.opponent.display_name} can respond to this challenge!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.accept_callback(interaction)
        self.stop()

    @ui.button(label='Decline', style=discord.ButtonStyle.danger)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.opponent.id:
            await interaction.response.send_message(f"I'm sorry, only {self.opponent.display_name} can respond to this challenge!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.decline_callback(interaction)
        self.stop()

    @ui.button(label='Cancel', style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.challenger.id:
            await interaction.response.send_message(f"I'm sorry, only {self.challenger.display_name} can cancel to this challenge!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.cancel_callback(interaction)
        self.stop()

class OngoingMatch(ui.View):

    def __init__(self, *, players: "tuple[discord.User, discord.User]", lobby_code, end_match_callback):
        super().__init__()
        self.players = players
        self.lobby_code = lobby_code
        self.end_match_callback = end_match_callback

        self.add_item(ui.Button(label="Join Match", url=f"https://playingcards.io/{lobby_code}"))
    
    @ui.button(label="End Match", style=discord.ButtonStyle.danger)
    async def end_match(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.id in map(lambda player : player.id, self.players):
            await interaction.response.send_message(f"I'm sorry, only {self.players[0].display_name} or {self.players[1].display_name} can end this match!", ephemeral=True)
            return
        await interaction.response.defer()
        await self.end_match_callback(interaction)
        self.stop()

# Card Creation
# =======================================================================================================================

class CreateFlairwarrior(ui.Modal, title="Creating a new Flairwarrior card!"):
    card_name = ui.TextInput(label="Card Name", required=True)
    atk = ui.TextInput(label = "Card ATK", required=True)
    hp = ui.TextInput(label = "Card HP", required=True)
    desc1 = ui.TextInput(label="Passive Ability", required=False)
    desc2 = ui.TextInput(label="Activated Ability", required=False)

    def __init__(self, card_color, modal_callback):
        super().__init__()
        self.card_type="Flairwarrior"
        self.card_color=card_color

        self.modal_callback = modal_callback

    async def on_submit(self, interaction: discord.Interaction):
        await self.modal_callback(self, interaction)
    
class CreateEvent(ui.Modal, title="Creating a new Event card!"):
    card_name = ui.TextInput(label="Card Name", required=True)
    desc1 = ui.TextInput(label="Card Description", required=True)

    def __init__(self, card_color, modal_callback):
        super().__init__()
        self.card_type="Event"
        self.card_color=card_color
        self.desc2 = ''
        self.atk=0
        self.hp=0

        self.modal_callback = modal_callback

    async def on_submit(self, interaction: discord.Interaction):
        await self.modal_callback(self, interaction)

class CreateRole(ui.Modal, title="Creating a new Role card!"):
    card_name = ui.TextInput(label="Card Name", required=True)
    desc1 = ui.TextInput(label="Card Description", required=True)

    def __init__(self, card_color, modal_callback):
        super().__init__()

        self.card_type="Role"
        self.card_color=card_color
        self.desc2 = ''
        self.atk=0
        self.hp=0

        self.modal_callback = modal_callback

    async def on_submit(self, interaction: discord.Interaction):
        await self.modal_callback(self, interaction)