# =============================================================
#  game.py — Loop principal, estados e lógica de colisão
# =============================================================

import pygame
import random
from settings import *
from entities import Ship, Bullet, Asteroid


class Game:
    """Gerencia o loop principal e os estados do jogo."""

    STATE_PLAYING   = "playing"
    STATE_GAME_OVER = "game_over"

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock  = pygame.time.Clock()

        # Fontes estilo retrô (monospace se disponível)
        self.font_large = pygame.font.SysFont("Courier New", 48, bold=True)
        self.font_med   = pygame.font.SysFont("Courier New", 28, bold=True)
        self.font_small = pygame.font.SysFont("Courier New", 20)

        self._reset()

    # ── Reset ────────────────────────────────────────────────
    def _reset(self):
        self.state     = self.STATE_PLAYING
        self.score     = 0
        self.ship      = Ship()
        self.bullets   = []
        self.asteroids = []
        self.frame     = 0
        self._spawn_timer = 0

    # ── Loop principal ───────────────────────────────────────
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self._handle_event(event)

            if self.state == self.STATE_PLAYING:
                keys = pygame.key.get_pressed()
                self._update(keys)

            self._draw()
            pygame.display.flip()
            self.frame += 1

        pygame.quit()

    # ── Eventos ──────────────────────────────────────────────
    def _handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == self.STATE_PLAYING:
                if event.key == pygame.K_SPACE:
                    bullet = self.ship.shoot()
                    if bullet:
                        self.bullets.append(bullet)

            elif self.state == self.STATE_GAME_OVER:
                if event.key == pygame.K_r:
                    self._reset()

    # ── Atualização ──────────────────────────────────────────
    def _update(self, keys):
        # Nave
        self.ship.update(keys)

        # Projéteis
        for b in self.bullets:
            b.update()
        self.bullets = [b for b in self.bullets if b.active]

        # Spawn de asteroides (rate diminui com a pontuação)
        spawn_rate = max(20, ASTEROID_SPAWN_RATE - self.score // 30)
        self._spawn_timer += 1
        if self._spawn_timer >= spawn_rate:
            self.asteroids.append(Asteroid())
            self._spawn_timer = 0

        # Asteroides
        for a in self.asteroids:
            a.update()

        # ── Colisões ─────────────────────────────────────────
        self._check_collisions()

        # Remove asteroides inativos (acertados por projéteis)
        asteroids_alive = []
        for a in self.asteroids:
            if not a.active:
                continue
            if a.reached_bottom():
                # Asteroide chegou ao fundo → Game Over
                self.state = self.STATE_GAME_OVER
                return
            asteroids_alive.append(a)
        self.asteroids = asteroids_alive

    def _check_collisions(self):
        ship_rect = self.ship.get_rect()

        for asteroid in self.asteroids:
            if not asteroid.active:
                continue

            # Projétil × Asteroide
            for bullet in self.bullets:
                if not bullet.active:
                    continue
                if asteroid.collides_with(bullet.get_rect()):
                    asteroid.active = False
                    bullet.active   = False
                    self.score     += SCORE_PER_HIT
                    self._spawn_explosion(asteroid.x, asteroid.y)
                    break

            # Nave × Asteroide
            if asteroid.active and asteroid.collides_with(ship_rect):
                self.state = self.STATE_GAME_OVER
                return

    # ── Explosão (visual simples) ─────────────────────────────
    def _spawn_explosion(self, x, y):
        """Armazena posição para efeito de flash no próximo frame."""
        if not hasattr(self, "_explosions"):
            self._explosions = []
        self._explosions.append({"x": x, "y": y, "timer": 8})

    # ── Desenho ──────────────────────────────────────────────
    def _draw(self):
        self.screen.fill(BLACK)
        self._draw_stars()

        if self.state == self.STATE_PLAYING:
            self._draw_game()
        else:
            self._draw_game()           # mantém cena ao fundo
            self._draw_game_over()

    def _draw_stars(self):
        """Fundo estrelado determinístico (seed fixo por frame par)."""
        rng = random.Random(42)
        for _ in range(80):
            sx = rng.randint(0, WIDTH)
            sy = rng.randint(0, HEIGHT)
            br = rng.randint(80, 200)
            self.screen.set_at((sx, sy), (br, br, br))

    def _draw_game(self):
        # Entidades
        self.ship.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        for a in self.asteroids:
            a.draw(self.screen)

        # Explosões
        if hasattr(self, "_explosions"):
            remaining = []
            for exp in self._explosions:
                alpha = int(255 * (exp["timer"] / 8))
                r = max(0, min(255, alpha))
                pygame.draw.circle(
                    self.screen,
                    (r, r // 2, 0),
                    (int(exp["x"]), int(exp["y"])),
                    int(20 * exp["timer"] / 8)
                )
                exp["timer"] -= 1
                if exp["timer"] > 0:
                    remaining.append(exp)
            self._explosions = remaining

        # HUD — Pontuação
        score_surf = self.font_med.render(f"SCORE: {self.score:05d}", True, GREEN)
        self.screen.blit(score_surf, (16, 12))

        # Linha separadora do HUD
        pygame.draw.line(self.screen, DARK_GRAY, (0, 46), (WIDTH, 46), 1)

    def _draw_game_over(self):
        # Painel semitransparente
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        self.screen.blit(overlay, (0, 0))

        # Textos
        title_surf  = self.font_large.render("GAME  OVER", True, RED)
        score_surf  = self.font_med.render(f"PONTUAÇÃO FINAL: {self.score:05d}", True, WHITE)
        restart_surf = self.font_small.render("[ R ]  para reiniciar", True, GRAY)

        cx = WIDTH // 2

        self.screen.blit(title_surf,   title_surf.get_rect(center=(cx, HEIGHT // 2 - 60)))
        self.screen.blit(score_surf,   score_surf.get_rect(center=(cx, HEIGHT // 2 + 10)))
        self.screen.blit(restart_surf, restart_surf.get_rect(center=(cx, HEIGHT // 2 + 60)))

        # Borda piscante
        t = pygame.time.get_ticks() // 500 % 2
        if t == 0:
            pygame.draw.rect(self.screen, RED, (10, 10, WIDTH - 20, HEIGHT - 20), 3)
