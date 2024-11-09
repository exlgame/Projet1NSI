import re
import time

import pygame
import pandas as pd

from player import Player
from screen import Screen

class Dialogue:
    def __init__(self, player: Player, screen: Screen):
        self.player = player
        self.screen = screen

        self.number: int | None = None
        self.id: int | None = None


        self.active: bool = False

        self.speakers: list[str] = []
        self.texts: list[str] = []

        self.dialogue_screen : DialogueScreen | None = None
        self.dialogue_data: DialogueData | None = None
    def load_data(self, number:int, id: int):
        self.player.can_move = False
        self.number = number
        self.id = id

        self.dialogue_data = DialogueData(number, id)
        self.active = True

        self.dialogue_screen = DialogueScreen(self.screen, dialogue_data=self.dialogue_data)

    def update(self):
        if self.active:
            if self.dialogue_screen.finished:
                pass

def format_text(text: str, line_length:int = 100, max_lines: int = 10) -> str:
    words = text.split()
    formatted_line = []
    current_line: str = ""

    for word in words:
        if len(current_line) + len(word) + 1  <= line_length:
            current_line += (word + "")
        else:
            formatted_line.append(current_line.strip())
            current_line = ""
            if len(formatted_line) >= max_lines -1:
                break

    if len(formatted_line) < max_lines:
        formatted_line.append(current_line.strip())
    if len(formatted_line) > max_lines:
        formatted_line= formatted_line[:max_lines]
    return "\n".join(formatted_line)

class DialogueData:
    def __init__(self, number: int, id: int):
        self.speaker_name: str = ""
        self.speaker_image: str = ""
        self.text: str = ""

        self.load_data(number, id)

    def load_data(self, number: int, id: int):
        file_path = f"../assets/dialogues/{number}.csv"

        df = pd.read_csv(file_path)

        i = id
        column_name = "fr"

        if i in df.index and column_name in df.columns:
            value = df.loc[i, column_name]
        else:
            value = "error"
            print(f"line {i} or column {column_name} not found")

    def extract_data(self,string: str):
        pattern = r':\[name=(.*?);face=(.*?)\]:(.*)'

        match = re.match(pattern,string)

        if match:
            self.speaker_name = match.group(1).strip()
            self.speaker_image = match.group(2).strip().split(',')
            self.text = format_text(match.group(3).strip())

    def __str__(self):
        return (f"Speaker name: {self.speaker_name},\n"
                f"Speaker image: {self.speaker_image},\n"
                f"Text: {self.text}")

class DialogueScreen:
    def __init__(self, screen: Screen, dialogue_data: DialogueData, speed: int = 1) -> None:
        self.screen: screen = Screen
        self.dialogue_data: DialogueData = dialogue_data
        self.speed: int = 1

        self.font: pygame.font.Font = pygame.font.Font("../assets/fonts/OakSans-Regular.ttf", 22)
        self.surface: pygame.Surface = pygame.Surface((1280, 131), pygame.SRCALPHA)
        self.background = pygame.image.load("../assets/interfaces/dialogues/message_box_0.png").convert_alpha()
        self.background_name = pygame.image.load("../assets/interfaces/dialogues/name_box_0.png").convert_alpha()

        self.speaker_name = self.font.render(self.dialogue_data.speaker_name,True,(225, 225, 225))

        self.time_wait = time.time()
        self.lines = self.dialogue_data.text.split("\n")

        self.lines_index = 0
        self.lines_offset = [0 for _ in range(len(self.lines))]

        self.y_offset = 0
        self.line_wait = {}

    def update(self):
        wait_time = self.speed * (1/60)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.background, (0,0))

        for index, line in enumerate(self.lines):
            if index > self.lines_index:
                break
            wait_match = re.search(r'\[WAIT (\d+)]', line)
            if wait_match:
                match = re.finditer(r'\[WAIT (\d+)]', line)
                for m in match:
                    self.line_wait[m.start()] = int(m.group(1))/60