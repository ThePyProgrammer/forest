## Pygame
from forest._importable import LazyImport

pygame = LazyImport("import pygame", "PACKAGE pygame — Free and Open Source library for making multimedia applications like games built on top of the excellent SDL library, derived from 'import pygame', from https://github.com/pygame/pygame, Documentation: https://www.pygame.org/docs/")
mixer = LazyImport("from pygame import mixer", "SUBPACKAGE pygame.mixer — Pygame module for loading and playing sounds, derived from 'from pygame import mixer', from https://github.com/pygame/pygame, Documentation: https://www.pygame.org/docs/ref/mixer.html")
