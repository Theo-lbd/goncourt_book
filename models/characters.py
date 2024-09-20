# -*- coding: utf-8 -*-

"""
Modèle pour les personnages
"""

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Character:
    """
    Classe représentant un personnage avec son nom et un ID optionnel.
    """
    id: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self) -> str:
        """
        Représentation en chaîne de caractères de l'objet Character.

        :return: Une chaîne décrivant le personnage
        """
        return f"Character(name={self.name})"
