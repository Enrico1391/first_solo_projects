from pathlib import Path

import pygame.font

from scoreboard import Scoreboard


class Buttons:
    """A class to build buttons for the game."""

    def __init__(self, s_penguin, msg):
        """Initialize button attributes."""
        self.s_penguin = s_penguin
        self.screen = s_penguin.screen
        self.screen_rect = self.screen.get_rect()
        self.sb = Scoreboard(self.s_penguin)
        self.settings = s_penguin.settings
        self.msg = msg

        # Constants for the credits and hotkeys buttons.
        self._credits_or_hotkeys_colors()
    
    def _set_button_properties(
            self, button_color, width=50 , height=20,
            font_size=48, text_color=(255, 255, 255)):
        """Set the dimensions and properties of the button."""
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size, bold=False, italic=True)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def make_play_button(self):
        """Make the Play button."""
        self._set_button_properties((255, 165, 0), width=200, height=50)

        # Center the object on the screen.
        self.rect.center = self.screen_rect.center
        
        # Render the message into an image.
        self._prep_msg()
    
    def make_pause_button(self):
        """Make the Pause button."""
        self._set_button_properties((0, 102, 204), font_size=20)

        # Place the button on the top right of the screen.
        self.rect.right = self.screen_rect.right
        
        # Render the message into an image.
        self._prep_msg()
    
    def make_menu_button(self):
        """Make the Menu button."""
        self._set_button_properties((0, 128, 0), font_size=20)

        # Place the button below the Pause button.
        self.rect.top = self.height
        self.rect.right = self.screen_rect.right
        
        # Render the message into an image.
        self._prep_msg()
    
    def make_difficulty_button(self):
        """Make the Difficulty button."""
        self._set_button_properties((34, 139, 34), font_size=14)

        # Place the button below the Menu button.
        self.rect.top = self.height * 2
        self.rect.right = self.screen_rect.right
        
        # Render the message into an image.
        self._prep_msg()

    def make_easy_difficulty_button(self, highlighted=False):
        """Make the Easy difficulty button."""
        # Highlight it only if the user clicks the button.
        if highlighted:
            self._set_button_properties((100, 100, 150), width=200, height=50)
        else:
            self._set_button_properties((235, 135, 0), width=200, height=50)

        # Center the object on the screen below the Play button.
        self.rect.top = (self.screen_rect.height/2) + (self.rect.height/2)
        self.rect.centerx = self.screen_rect.centerx
        
        # Render the message into an image.
        self._prep_msg()

    def make_medium_difficulty_button(self, highlighted=False):
        """Make the Medium difficulty button."""
        # Highlight it only if the user clicks the button.
        if highlighted:
            self._set_button_properties((100, 100, 150), width=200, height=50)
        else:
            self._set_button_properties((215, 105, 0), width=200, height=50)

        # Center the object on the screen below the Easy button.
        self.rect.top = (
            (self.screen_rect.height/2) 
            + (self.rect.height) 
            + (self.rect.height/2)
        )
        self.rect.centerx = self.screen_rect.centerx
        
        # Render the message into an image.
        self._prep_msg()

    def make_hard_difficulty_button(self, highlighted=False):
        """Make the Hard difficulty button."""
        # Highlight it only if the user clicks the button.
        if highlighted:
            self._set_button_properties((100, 100, 150), width=200, height=50)
        else:
            self._set_button_properties((195, 75, 0), width=200, height=50)

        # Center the object on the screen below the Medium button.
        self.rect.top = (
            (self.screen_rect.height/2) 
            + (self.rect.height*2) 
            + (self.rect.height/2)
        )
        self.rect.centerx = self.screen_rect.centerx
        
        # Render the message into an image.
        self._prep_msg()
    
    def make_scoreboard_button(self):
        """Make a button to use as background for the Scoreboard."""
        self._set_button_properties(
            (220, 220, 220), 
            width=self.settings.screen_width, 
            height=(self.sb.score_rect.height + 30)
        )

        # Place the object on the bottom of the screen.
        self.rect.bottom = self.screen_rect.bottom
        
        # Render the message into an image.
        self._prep_msg()

    def make_hotkeys_button(self):
        """Make the Hotkeys button."""
        self._set_button_properties((17, 112, 17), font_size=15)

        # Place the button below the Difficulty button.
        self.rect.top = self.height * 3
        self.rect.right = self.screen_rect.right
        
        # Render the message into an image.
        self._prep_msg()

    def make_credits_button(self):
        """Make the Credits button."""
        self._set_button_properties((0, 85, 0), font_size=15)

        # Place the button below the Hotkeys button.
        self.rect.top = self.height * 4
        self.rect.right = self.screen_rect.right
        
        # Render the message into an image.
        self._prep_msg()
    
    def make_credits_display_button(self, ai_game, show_credits=True):
        """Make a button and use it as a screen where to display the credits."""
        self._set_button_properties(
            (255, 255, 255), width=ai_game.settings.screen_width, 
            height=ai_game.settings.screen_height, font_size=0, 
            text_color=(0, 0, 0))

        # Place the button at the center of the screen.
        self.rect.center = self.screen_rect.center

        self._read_credits_or_hotkeys(show_credits)

    def _read_credits_or_hotkeys(self, show_credits=True):
        """Read the content from credits.txt or hotkeys.txt and display it."""
        if show_credits:
            path = Path('txt_files/credits.txt')
        elif not show_credits:
            path = Path('txt_files/hotkeys.txt')

        content = path.read_text()
        lines = content.splitlines()
        self._render_credits_or_hotkeys(lines, show_credits)
    
    def _render_credits_or_hotkeys(self, lines, show_credits):
        """Render the credits or hotkeys on the button surface."""
        if show_credits:
            font = pygame.font.SysFont('Tahoma', 8, bold=True)
            colored_lines = self._colorize_credits_lines(lines)
        elif not show_credits:
            font = pygame.font.SysFont('DejaVu Sans', 15, bold=True)
            colored_lines = self._colorize_hotkeys_lines(lines)
        
        surface = self._make_surface(font, colored_lines)
        self._prep_credits_or_hotkeys(surface)
    
    def _credits_or_hotkeys_colors(self):
        """Store constants for the colors used in the credits or hotkeys."""
        # Credits colors.
        self.ARTIST_COLOR = (200, 100, 0)
        self.SOUND_COLOR = (0, 150, 150)
        self.IMAGE_COLOR = (0, 128, 0)

        # Hotkeys colors.
        self.KEYS = (0, 128, 0)
    
    def _colorize_credits_lines(self, lines):
        """Colorize the credits' lines based on keywords."""
        colored_lines = [
            (line, self.ARTIST_COLOR if 'artist' in line.lower() 
            else self.SOUND_COLOR if 'SOUND' in line 
            else self.IMAGE_COLOR if 'image' in line.lower()
            else self.text_color) 
            for line in lines
        ]
        
        return colored_lines
    
    def _colorize_hotkeys_lines(self, lines):
        """Colorize the hotkeys' lines based on keywords."""
        colored_lines = [(line, self.KEYS if ' keys' in line.lower() 
                else self.text_color) for line in lines]

        return colored_lines
    
    def _make_surface(self, font, colored_lines):
        """Create a surface to hold the rendered lines."""
        max_line_width = 0
        total_height = 0
        
        # Render each line.
        rendered_lines = [font.render(line, True, color, self.button_color) 
                for line, color in colored_lines]
        
        # Update dimensions.
        for line in rendered_lines:
            total_height += line.get_height()
            max_line_width = max(max_line_width, line.get_width())

        # Create a surface to hold all the rendered lines.
        surface = pygame.Surface(
            (max_line_width, total_height), pygame.SRCALPHA)
    
        # Blit each line onto the surface.
        y = 0
        for rendered_line in rendered_lines:
            surface.blit(rendered_line, (0, y))
            y += rendered_line.get_height()
        
        return surface
    
    def _prep_credits_or_hotkeys(self, surface):
        """Turn the credits or hotkeys into a rendered image."""
        self.msg_image = surface
        self.msg_image_rect = surface.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _prep_msg(self):
        """Generate the message and center it on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, 
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and text on the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)