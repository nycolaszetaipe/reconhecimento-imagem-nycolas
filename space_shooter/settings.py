# =============================================================
#  settings.py — Constantes e configurações globais
# =============================================================

# ── Tela ─────────────────────────────────────────────────────
WIDTH  = 800
HEIGHT = 600
FPS    = 60
TITLE  = "Space Shooter — Estilo Atari"

# ── Cores (paleta estilo Atari) ───────────────────────────────
BLACK       = (0,   0,   0)
WHITE       = (255, 255, 255)
CYAN        = (0,   255, 255)
YELLOW      = (255, 255, 0)
GREEN       = (0,   255, 0)
RED         = (255, 68,  68)
GRAY        = (170, 170, 170)
DARK_GRAY   = (60,  60,  60)
ORANGE      = (255, 165, 0)

# ── Nave ─────────────────────────────────────────────────────
SHIP_SPEED       = 6        # pixels por frame
SHIP_WIDTH       = 40       # largura do triângulo
SHIP_HEIGHT      = 30       # altura do triângulo
SHIP_Y_OFFSET    = 60       # distância do fundo da tela
BULLET_COOLDOWN  = 20       # frames entre disparos

# ── Projétil ─────────────────────────────────────────────────
BULLET_SPEED  = 10
BULLET_RADIUS = 4

# ── Asteroides ───────────────────────────────────────────────
ASTEROID_SPEED_MIN  = 2
ASTEROID_SPEED_MAX  = 5
ASTEROID_RADIUS_MIN = 15
ASTEROID_RADIUS_MAX = 35
ASTEROID_SPAWN_RATE = 60    # frames entre cada novo asteroide (diminui com pontuação)

# ── Pontuação ────────────────────────────────────────────────
SCORE_PER_HIT = 10
