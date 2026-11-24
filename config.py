# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Écoles de l’image"                       # OBLIGATOIRE nom du média, tel qu'affiché
SLUG = "ecoles-image"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#4338CA"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "1"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "écoles"                          # OBLIGATOIRE ce que l'on compare : marques, contrats, opérateurs, box, écoles...
UNIT_ONE = "école"                       # singulier
CTA = "Comparer 2 écoles"                # OBLIGATOIRE bouton du header et des encarts
CTA_LONG = "Comparer deux écoles"        # lien texte du hero
BASELINE = "Le guide des écoles de cinéma, d’audiovisuel et de son. Diplômes, campus, alternance et frais comparés sur les mêmes critères publics."  # pied de page
TAGLINE_FOOTER = "Le média des études de cinéma, d’audiovisuel et de son."
AUTHOR = "La rédaction Écoles de l’image"
AUTHOR_INITIAL = "É"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("3iS", "cinema/"), ("ESRA", "cinema/"), ("ENS Louis-Lumière", "son/"), ("SAE Institute", "son/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email par semaine, avec les classements mis à jour, les dates de journées portes ouvertes et nos nouveaux guides d’orientation."
NEWSLETTER_NOTE = "Désinscription en un clic."
ASIDE_NEWS_P = "Les classements mis à jour et les dates de portes ouvertes, un email par semaine."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce comparatif repose sur des données publiques, vérifiables une par une."
METHOD_ITEMS = [
 "Chaque classement repose sur 8 critères vérifiables sur une source publique, notés Oui ou N.A, 1 point par Oui, poids égal",
 "Les frais de scolarité sont relevés sur les pages tarifs officielles des écoles, à la date indiquée",
 "Les diplômes sont vérifiés au Répertoire national des certifications professionnelles (France Compétences)",
 "Les taux d’insertion sont ceux que les écoles publient elles-mêmes sur leur site",
 "N.A signifie non applicable, car données non trouvées par la rédaction. Deux écoles à égalité de points sont classées ex æquo",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Formation", "bachelor en 3 ans, formation son"),
 ("Diplôme", "titre RNCP ou diplôme d’État, réseau Cilect"),
 ("Accès", "au moins 3 campus, alternance"),
 ("Transparence", "frais et insertion publiés"),
 ("Note globale", "part des 8 critères vérifiés"),
]

# Liens internes supplémentaires pour linkify : (fragment de titre présent dans le libellé du lien, chemin).
# Les titres complets des articles publiés sont branchés automatiquement.
EXTRA_LINKS = []

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap"
COMPARED = "comparées"                  # accord du participe dans l en-tête d article : comparées (marques), comparés (comptes, contrats)

DISCLAIMER = "Ce classement est établi sous la responsabilité éditoriale de la rédaction Écoles de l’image. Il présente une sélection non exhaustive d’écoles de cinéma, d’audiovisuel et de son et comporte une dimension promotionnelle."
