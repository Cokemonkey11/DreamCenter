import enum

import pygame as pg

class Sprite(pg.sprite.Sprite):
    @classmethod
    def create_from_tile(
        cls,
        index,
        groups,
        image_tiles=IMAGE_SPRITES,
        flipped_x=False,
        flipped_y=False,
        **kwargs,
    ):
        image = image_tiles[(flipped_x, flipped_y, index)]
        rect = image.get_rect()
        return cls(
            image=image,
            image_tiles=image_tiles,
            index=index,
            groups=groups,
            rect=rect,
            **kwargs,
        )

    @classmethod
    def create_from_surface(
        cls,
        groups,
        surface,
        **kwargs,
    ):
        rect = surface.get_rect()
        return cls(
            groups=groups,
            image=surface,
            index=None,
            rect=rect,
            **kwargs,
        )

    def __init__(
        self,
        groups,
        image_tiles=None,
        index=None,
        rect=None,
        image=None,
        orientation=0,
        position=(0,0),
        flipped_x=False,
        flipped_y=False,
    ):
        super().__init__(groups)
        self.image = image
        self.image_tiles = image_tiles
        self.index = index
        self.rect = rect
        self.orientation = orientation
        self.flipped_x = flipped_x
        self.flipped_y = flipped_y
        if self.image is not None:
            self.mask = pg.mask.from_surface(self.image)
            self.surface = self.image.copy()
            self.rotate(self.orientation)
        if self.rect is not None and position is not None:
            self.move(position)

    def set_sprite_index(self, index):
        self.image = self.image_sprites[(self.flipped_x, self.flipped_y, index)]
        self.surface = self.image.copy()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image)
        self.index = index
        self.rotate(self.orientation)

    def move(self, position, center: bool = True):
        if center:
            self.rect.center = position
        else:
            self.rect.topleft = position

    def rotate(self, angle):
        if angle == self._last_angle:
            return
        new_image = pg.transform.rotate(self.surface, angle % 360)
        new_rect = new_image.get_rect(center=self.rect.center)
        self.image = new_image
        self.rect = new_rect
        self.mask = pg.mask.from_surface(self.image)
        self._last_angle = angle

class Layer(enum.IntEnum):

    background = 0
    enemy = 20
    debris = 25
    projectile = 30

class Background(Sprite):
    """
    Default background sprite. Does not rotate
    """

    _layer = Layer.background

    def update(self):
        pass

