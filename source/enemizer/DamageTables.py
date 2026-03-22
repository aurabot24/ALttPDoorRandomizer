from pathlib import Path
from ...Utils import load_cached_yaml


class DamageTable:
    def __init__(self):
        self.damage_table = load_cached_yaml([Path(__file__).resolve().parent, 'damage_table.yaml'])
        self.enemy_damage = load_cached_yaml([Path(__file__).resolve().parent, 'enemy_damage_table.yaml'])

