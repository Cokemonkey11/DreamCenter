from dataclasses import dataclass
from dreamcenter.sprites import SpriteManager
from pygame import Vector2 as Vector
from dreamcenter.constants import TILE_WIDTH
from dreamcenter.enumeration import AnimationState
import pygame as pg


@dataclass
class PlayerGroup:
    """
    Used to manage actions related to the player and player sprite
    """
    sprite_manager: SpriteManager
    player = None
    empty_hearts = []
    half_hearts = []
    movement_directions = {"top": False, "bottom": False, "left": False, "right": False}
    firing = False

    def spawn_player(self) -> None:
        """
        Creates player sprite and assigns to player variable inside class
        """
        self.player = self.sprite_manager.create_player()

    def move_player(self) -> None:
        """
        Uses movement_directions to determine which keys are pressed
        Scales to length based on player speed and moves player
        """
        move = Vector(
            self.movement_directions["right"] - self.movement_directions["left"],
            self.movement_directions["bottom"] - self.movement_directions["top"]
        )

        if move.length_squared() > 0:
            self.player.animation_state = AnimationState.walking
            move.scale_to_length(self.player.speed)
            self.player.position += move
        else: self.player.animation_state = AnimationState.stopped

    def fire_projectile(self) -> None:
        """
        Checks if player is holding mouse and able to fire
        Creates projectile based on player stats if able
        """
        if self.player.cooldown_remaining == 0 and self.firing is True:
            self.sprite_manager.create_projectile(
                self.player.position,
                pg.mouse.get_pos(),
                damage=self.player.damage,
                max_distance=self.player.range
            )
            self.player.cooldown_remaining = self.player.cooldown

    def update(self):
        self.move_player()
        self.fire_projectile()

    def spawn_default_hearts(self):
        for i in range(int(self.player.health / 2)):
            self.empty_hearts.append(
                self.sprite_manager.create_health(
                    ((i * TILE_WIDTH + TILE_WIDTH/2), TILE_WIDTH/2),
                    index="empty_heart"
                )
            )
            self.half_hearts.append(
                self.sprite_manager.create_health(
                    ((i * TILE_WIDTH) + TILE_WIDTH / 4, TILE_WIDTH / 2),
                    index="half_heart"
                )
            )
            self.half_hearts.append(
                self.sprite_manager.create_health(
                    ((i * TILE_WIDTH) + TILE_WIDTH / 1.35, TILE_WIDTH / 2),
                    index="half_heart",
                    flipped_x=True
                )
            )

        for i in range(len(self.half_hearts)):
            if i % 2 == 0:
                self.half_hearts[i].flipped_y = True

    def take_damage(self, damage):
        self.player.health -= damage
        self.half_hearts.pop().kill()
