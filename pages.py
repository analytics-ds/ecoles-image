# -*- coding: utf-8 -*-
"""Pages fixes. À adapter : le nom du média et le secteur. Pas de coordonnées réelles inventées."""
import config as C

PAGES = [
 dict(slug="a-propos", title=f"Qui sommes-nous, la rédaction {C.NOM}", desc=f"{C.NOM}, média comparateur. Qui écrit, comment nous relevons les données, comment nous classons.",
  h1=f"Qui sommes-nous", lead=C.BASELINE,
  sections=[
   ("Ce que nous faisons", [f"{C.NOM} compare des {C.UNIT} sur des critères publics et identiques d'une fiche à l'autre. Chaque comparatif indique la date de relevé, le périmètre comparé et la grille de notation.",
                            "La rédaction suit les écoles de cinéma, d’audiovisuel et de son, de leurs journées portes ouvertes à leurs festivals de fin d’études. Elle compare les diplômes, les campus, l’alternance et les frais, et met chaque classement à jour quand une école publie de nouveaux chiffres."]),
   ("Comment nous notons", [f"Huit critères vérifiables sur une source publique, notés Oui ou N.A, 1 point par Oui, poids égal. Même score, même rang. La grille est publiée dans chaque classement avec la date du relevé."]),
   ("Contact", ["Pour signaler une erreur, demander une mise à jour ou proposer un sujet, écrivez à la rédaction via le formulaire de la newsletter. Nous répondons sous cinq jours ouvrés."]),
  ]),
 dict(slug="mentions-legales", title=f"Mentions légales, {C.NOM}", desc=f"Mentions légales du site {C.NOM}.",
  h1="Mentions légales", lead="Informations légales relatives à l'édition et à l'hébergement du site.",
  sections=[
   ("Éditeur", [f"Le site {C.NOM} est édité par sa rédaction. Directeur de la publication : la rédaction {C.NOM}."]),
   ("Hébergement", ["Le site est hébergé par GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis."]),
   ("Propriété intellectuelle", ["Les textes et la structure du site sont la propriété de l'éditeur. Les logos et marques cités appartiennent à leurs propriétaires respectifs et sont reproduits à des fins d'identification des produits comparés. Les photographies sont utilisées sous licence libre, la source de chaque visuel est conservée par la rédaction."]),
   ("Données personnelles", ["Le site ne dépose aucun cookie de suivi et ne collecte aucune donnée personnelle en dehors de l'adresse email volontairement transmise pour la newsletter."]),
  ]),
]
