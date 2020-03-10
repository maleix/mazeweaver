"""
Generic and short scenes
"""
import sys
import pygame


from params import SCREEN_WIDTH, SCREEN_HEIGTH
from utils import (
    rgb,
    draw_grid,
    play_sound,
    play_song,
    queue_song,
)

class SceneBase:
    """ Main class for scenes """

    def __init__(self, screen):
        self.next = self
        self.screen = screen

    def process_input(self, events, pressed_keys):
        """ User input that changes the game status """
        print("uh-oh, you didn't override this in the child class")

    def update(self):
        """ Updates logic game in each iteration """
        print("uh-oh, you didn't override this in the child class")

    def render_once(self):
        """ Draws graphics that only need to be printed once for performance """
        print("uh-oh, you didn't override this in the child class")

    def render(self):
        """ Draws graphics """
        print("uh-oh, you didn't override this in the child class")

    def switch_to_scene(self, next_scene):
        """ Changes to another scene """
        self.screen.fill(rgb("black"))
        self.next = next_scene


class TitleScene(SceneBase):
    """ Title Menu with options """

    def __init__(self, screen):
        SceneBase.__init__(self, screen)
        self.title_font = pygame.font.Font("resources/fonts/Retro.ttf", 110)
        self.options_font = pygame.font.Font("resources/fonts/Retro.ttf", 75)
        play_song("resources/songs/bgm_menu.mp3")
        self.menu = ["START", "INSTRUCTIONS", "QUIT"]
        self.selected = 0
        self.rendered_once = False

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.selected > 0:
                        self.selected -= 1
                        play_sound("resources/sounds/beep.wav")
                elif event.key == pygame.K_DOWN:
                    if self.selected < len(self.menu) - 1:
                        self.selected += 1
                        play_sound("resources/sounds/beep.wav")
                if event.key == pygame.K_RETURN:
                    if self.menu[self.selected] == "START":
                        play_song("resources/songs/retrofunk.mp3")
                        queue_song("resources/songs/lasvegas.mp3") # TODO: ain't working
                        self.switch_to_scene(TransitionScene(self.screen, 0))
                    elif self.menu[self.selected] == "INSTRUCTIONS":
                        self.switch_to_scene(InstructionsScene(self.screen))
                    elif self.menu[self.selected] == "QUIT":
                        pygame.quit()
                        sys.exit()

    def update(self):
        pass

    def render_once(self):
        self.screen.fill(rgb("black"))
        draw_grid(self.screen, 10, 10, "blue")
        title = self.title_font.render("MazeWeaver", 0, rgb("yellow"))
        title_rect = title.get_rect()
        self.screen.blit(title, (SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        pygame.display.update()

    def render(self):
        if not self.rendered_once:
            self.render_once()
            self.rendered_once = True

        rects_to_draw = []
        for i, option in enumerate(self.menu):
            if i == self.selected:
                text = self.options_font.render(option, 0, rgb("white"))
            else:
                text = self.options_font.render(option, 0, rgb("gray"))

            rects_to_draw.append(
                self.screen.blit(
                    text, (SCREEN_WIDTH / 2 - (text.get_rect()[2] / 2), (i * 60) + 300)
                )
            )

        pygame.display.update(rects_to_draw)


class InstructionsScene(SceneBase):
    """ Class to show instructions to the player """

    def __init__(self, screen):
        SceneBase.__init__(self, screen)
        self.font = pygame.font.Font("resources/fonts/Retro.ttf", 50)
        self.rendered_once = False
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = 0
        self.can_exit = False

    def process_input(self, events, pressed_keys):
        if (
            pressed_keys[pygame.K_ESCAPE]
            or pressed_keys[pygame.K_RETURN]
            or pressed_keys[pygame.K_SPACE]
        ):
            if self.can_exit:
                self.switch_to_scene(TitleScene(self.screen))

    def update(self):
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        # Wait only a bit to prevent instant return, so the previous keys are refreshed
        if self.seconds > 0.2:
            self.can_exit = True

    def render_once(self):
        self.screen.fill(rgb("black"))
        draw_grid(self.screen, 10, 10, "blue")
        text = [
            "Try to get to the red square with any block!",
            " ",
            " ",
            "Controls: ",
            "-------------",
            "1 2 3: select block",
            "Arrows: move the block",
            "R: to reset the level",
        ]

        for i, line in enumerate(text):
            linefont = self.font.render(line, 0, rgb("white"))
            self.screen.blit(
                linefont,
                (SCREEN_WIDTH / 2 - (linefont.get_rect()[2] / 2), i * 40 + 120),
            )

        pygame.display.update()

    def render(self):
        if not self.rendered_once:
            self.render_once()
            self.rendered_once = True


class TransitionScene(SceneBase):
    """ Class to present the following level """

    def __init__(self, screen, next_level):
        SceneBase.__init__(self, screen)
        self.next_level = next_level
        self.font = pygame.font.Font("resources/fonts/Retro.ttf", 90)
        self.rendered_once = False
        self.start_ticks = pygame.time.get_ticks()  # starter tick
        self.seconds = 0
        self.can_exit = False
        # play_song(SONGS[self.next_level])

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        # Wait only a bit so the previous keys are refreshed
        if self.seconds > 1.5:
            from game import GameScene
            self.switch_to_scene(GameScene(self.screen, self.next_level))

    def render_once(self):
        self.screen.fill(rgb("black"))
        draw_grid(self.screen, 10, 10, "blue")
        text = "Level " + str(self.next_level + 1)
        linefont = self.font.render(text, 0, rgb("white"))
        self.screen.blit(
            linefont,
            (
                SCREEN_WIDTH / 2 - (linefont.get_rect()[2] / 2),
                (SCREEN_HEIGTH / 2 - (linefont.get_rect()[2] / 2)),
            ),
        )
        pygame.display.update()

    def render(self):
        if not self.rendered_once:
            self.render_once()
            self.rendered_once = True


class WinScene(SceneBase):
    """ Class to present the following level """

    def __init__(self, screen):
        SceneBase.__init__(self, screen)
        self.font = pygame.font.Font("resources/fonts/Retro.ttf", 75)
        self.rendered_once = False

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render_once(self):
        self.screen.fill(rgb("black"))
        draw_grid(self.screen, 10, 10, "blue")
        text = [
                    "Congratulations!",
                    "You have passed all levels"
                ]
        for i, line in enumerate(text):
            linefont = self.font.render(line, 0, rgb("white"))
            self.screen.blit(
                linefont,
                (SCREEN_WIDTH / 2 - (linefont.get_rect()[2] / 2), i * 120 + 115),
            )
            print(i)
        pygame.display.update()

    def render(self):
        if not self.rendered_once:
            self.render_once()
            self.rendered_once = True
