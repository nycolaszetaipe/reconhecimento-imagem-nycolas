# =============================================================
#  entities.py — Entidades do jogo: Nave, Projétil, Asteroide
# =============================================================

import pygame
import math
import random
from settings import *


class Ship:
    """Nave controlada pelo jogador."""

    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - SHIP_Y_OFFSET
        self.cooldown = 0           # contador de cooldown do disparo
        self.alive = True

    # ── Atualização ──────────────────────────────────────────
    def update(self, keys):
        # Movimento horizontal
        if keys[pygame.K_LEFT]:
            self.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += SHIP_SPEED

        # Limita nas bordas da tela
        half = SHIP_WIDTH // 2
        self.x = max(half, min(WIDTH - half, self.x))

        # Cooldown do disparo
        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self):
        """Retorna um Bullet se o cooldown permitir, ou None."""
        if self.cooldown == 0:
            self.cooldown = BULLET_COOLDOWN
            return Bullet(self.x, self.y - SHIP_HEIGHT)
        return None

    # ── Renderização ─────────────────────────────────────────
    def draw(self, surface):
        # Triângulo apontando para cima
        tip    = (self.x,                        self.y - SHIP_HEIGHT)
        left   = (self.x - SHIP_WIDTH // 2,      self.y)
        right  = (self.x + SHIP_WIDTH // 2,      self.y)
        pygame.draw.polygon(surface, CYAN,  [tip, left, right])
        pygame.draw.polygon(surface, WHITE, [tip, left, right], 2)

        # Chama de propulsão (pequeno triângulo embaixo)
        flame_tip   = (self.x,           self.y + 12)
        flame_left  = (self.x - 8,       self.y)
        flame_right = (self.x + 8,       self.y)
        pygame.draw.polygon(surface, ORANGE, [flame_tip, flame_left, flame_right])

    # ── Colisão ──────────────────────────────────────────────
    def get_rect(self):
        """Retorna um Rect aproximado para detecção de colisão."""
        return pygame.Rect(
            self.x - SHIP_WIDTH // 2,
            self.y - SHIP_HEIGHT,
            SHIP_WIDTH,
            SHIP_HEIGHT
        )


# ─────────────────────────────────────────────────────────────

class Bullet:
    """Projétil disparado pela nave."""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.active = True

    def update(self):
        self.y -= BULLET_SPEED
        if self.y < -BULLET_RADIUS:
            self.active = False

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), BULLET_RADIUS)
        # Brilho interno
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), BULLET_RADIUS - 2)

    def get_rect(self):
        return pygame.Rect(
            self.x - BULLET_RADIUS,
            self.y - BULLET_RADIUS,
            BULLET_RADIUS * 2,
            BULLET_RADIUS * 2
        )


# ─────────────────────────────────────────────────────────────

class Asteroid:
    """Asteroide que cai do topo da tela."""

    # Pontos do polígono irregular (offsets em ângulos distribuídos)
    _ANGLES = [i * (360 / 10) for i in range(10)]

    def __init__(self):
        self.radius = random.randint(ASTEROID_RADIUS_MIN, ASTEROID_RADIUS_MAX)
        self.x = float(random.randint(self.radius, WIDTH - self.radius))
        self.y = float(-self.radius)
        self.speed = random.uniform(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
        self.active = True
        self.rotation = 0
        self.rot_speed = random.uniform(-2, 2)

        # Gera variações de raio para aparência rochosa
        self._offsets = [random.uniform(0.7, 1.0) for _ in self._ANGLES]

    def update(self):
        self.y += self.speed
        self.rotation = (self.rotation + self.rot_speed) % 360
        if self.y - self.radius > HEIGHT:
            self.active = False   # será tratado como game over em game.py

    def draw(self, surface):
        points = []
        for i, angle in enumerate(self._ANGLES):
            rad = math.radians(angle + self.rotation)
            r   = self.radius * self._offsets[i]
            px  = self.x + r * math.cos(rad)
            py  = self.y + r * math.sin(rad)
            points.append((px, py))

        pygame.draw.polygon(surface, GRAY,  points)
        pygame.draw.polygon(surface, WHITE, points, 2)

    def collides_with(self, other_rect):
        """Colisão círculo × rect (aproximação simples)."""
        closest_x = max(other_rect.left, min(self.x, other_rect.right))
        closest_y = max(other_rect.top,  min(self.y, other_rect.bottom))
        dx = self.x - closest_x
        dy = self.y - closest_y
        return (dx * dx + dy * dy) <= (self.radius * self.radius)

    def reached_bottom(self):
        return self.y - self.radius > HEIGHT
