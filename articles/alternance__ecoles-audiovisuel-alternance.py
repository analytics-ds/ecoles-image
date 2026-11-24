# -*- coding: utf-8 -*-
O, N = "Oui", "N.A"
ARTICLE = dict(
 cat="alternance", slug="ecoles-audiovisuel-alternance",
 title="Quelles sont les meilleures écoles d’audiovisuel en alternance ?",
 desc="Quelle école de cinéma ou d’audiovisuel choisir en alternance en 2026 ? 5 écoles classées sur 8 critères publics, 3iS, SAE Institute, Gobelins, Cinécréatis, ESRA.",
 kicker="Classement", h1="Quelles sont les meilleures écoles de cinéma et d’audiovisuel en alternance en 2026 ?",
 lead="L’alternance fait payer la formation par l’entreprise et met l’étudiant en situation réelle. Cinq écoles classées sur ce qu’elles affichent vraiment.",
 img="art-3.jpg", img_alt="Étudiante qui cadre une scène sur un moniteur de tournage",
 date="2026-11-22", date_fr="22 novembre 2026", reading="6", nb="5",
 brief_answer="Les meilleures écoles de cinéma et d’audiovisuel en alternance en 2026, sur notre grille de huit critères publics, sont <b>3iS</b> (8 critères sur 8) et <b>SAE Institute</b> (5 sur 8), puis <b>Gobelins</b>, <b>Cinécréatis</b> et <b>l’ESRA</b>, ex æquo avec 2 sur 8. Chez 3iS, l’alternance s’ouvre en 3e année de bachelor, en cinéma comme en son, et le Mastère Production se fait en alternance.",
 brief=[
  "3iS ouvre l’alternance en 3e année du Bachelor Cinéma et Audiovisuel et du Bachelor Ingénieur du son",
  "Le Mastère Production de 3iS, bac+4 en un an, titre RNCP de niveau 6, se suit en alternance",
  "3iS annonce plus de 1 000 entreprises partenaires et 89 % d’insertion à 6 mois",
  "SAE Institute affiche une 3e année Son &amp; Musique en alternance dans sa grille tarifaire",
 ],
 table=dict(
  head=["École","Score /8","Rang","Années en alternance","Domaines","Le point fort"],
  rows=[
   ["3iS","8","1er","3e année de bachelor, Mastère Production","Cinéma, son, production","5 campus et plus de 1 000 entreprises partenaires",1],
   ["SAE Institute","5","2e","3e année Son &amp; Musique","Son, musique","L’alternance en son",0],
   ["Gobelins","2","3e ex æquo","N.A","Image, animation","La tradition de l’apprentissage",0],
   ["Cinécréatis","2","3e ex æquo","N.A","Cinéma","Titre RNCP et frais publiés",0],
   ["ESRA","2","3e ex æquo","N.A","Cinéma, son","Trois campus",0],
   ["BTS Métiers de l’audiovisuel en apprentissage","Hors grille","Hors classement","2 ans","Image, son, montage, production","La voie publique en apprentissage",0],
  ],
  note="Score sur 8 critères, relevé le 22 novembre 2026. N.A : non applicable, car données non trouvées par la rédaction."),
 podium=[
  ("3is","3iS","8 critères sur 8","Alternance en bachelor et en mastère, 5 campus","8"),
  ("sae","SAE Institute","5 critères sur 8","3e année Son &amp; Musique en alternance","5"),
  ("gobelins","Gobelins","2 critères sur 8","Titres RNCP de niveaux 6 et 7","2"),
 ],
 sections=[
  dict(h2="Le tableau comparatif des 5 écoles", id="tableau", body=[
   ("p","En alternance, l’étudiant partage son temps entre l’école et une entreprise qui le rémunère et prend en charge le coût de la formation. Dans l’audiovisuel, c’est aussi un moyen d’arriver sur le marché avec un vrai réseau."),
   ("table",None),
   ("podium",None),
  ]),
  dict(h2="3iS, l’alternance en cinéma et en son", id="3is", body=[
   ("p","Chez 3iS, le Bachelor Cinéma et Audiovisuel et le Bachelor Ingénieur du son se suivent à temps plein les deux premières années, puis l’alternance est possible en 3e année. Le Mastère Production, bac+4 en un an avec un titre RNCP de niveau 6, se fait en alternance."),
   ("img",dict(src="in-ecoles-audiovisuel-alternance-1.jpg",alt="Équipe d’étudiants 3iS en tournage avec caméra et projecteur",cap="Tournage d’étudiants 3iS. Photo 3iS.")),
   ("p","L’école annonce plus de 1 000 entreprises partenaires et un taux d’insertion de 89 % à 6 mois. Ses cinq campus, Paris Ouest, Bordeaux-Bègles, Lyon-Bron, Nantes et Avignon, permettent de chercher une entreprise d’accueil dans plusieurs bassins d’emploi."),
  ]),
  dict(h2="Les autres écoles du classement", id="autres", body=[
   ("h3","SAE Institute"),
   ("p","Sa grille tarifaire 2026-2027 prévoit une 3e année Son &amp; Musique en alternance, sur un réseau de campus à Paris, Bordeaux, Lyon et Toulouse."),
   ("h3","Gobelins"),
   ("p","L’école de l’image de la CCI Paris Île-de-France a une longue tradition d’apprentissage et délivre des titres RNCP de niveaux 6 et 7."),
   ("h3","Cinécréatis et ESRA"),
   ("p","Cinécréatis, à Nantes, délivre un titre RNCP de niveau 6 et publie ses frais. L’ESRA forme au cinéma et au son à Paris, Rennes et Nice."),
   ("img",dict(src="in-ecoles-audiovisuel-alternance-2.jpg",alt="Étudiants qui préparent un plan produit avec une caméra",cap="Atelier lumière et publicité. Photo 3iS.")),
  ]),
  dict(h2="Méthode du classement", id="methode", body=[
   ("p","Huit critères, chacun noté Oui s’il est vérifié sur une source publique, N.A sinon. 1 point par Oui, poids égal, score sur 8. Même score, même rang. Relevé du 22 novembre 2026."),
   ("table2",dict(
     head=["Critère","3iS","SAE","Gobelins","Cinécréatis","ESRA"],
     rows=[["Rang du classement","1er","2e","3e ex æquo","3e ex æquo","3e ex æquo"],
           ["Alternance affichée sur le site",O,O,O,N,N],
           ["Alternance possible en bachelor",O,O,N,N,N],
           ["Mastère ou bac+4 en alternance",O,N,N,N,N],
           ["Titre RNCP",O,N,O,O,O],
           ["Au moins 3 campus",O,O,N,N,O],
           ["Frais publiés sur le site",O,O,N,O,N],
           ["Taux d’insertion publié",O,N,N,N,N],
           ["Alternance en formation son",O,O,N,N,N],
           ["Score sur 8","8","5","2","2","2"]],
     note="N.A : non applicable, car données non trouvées par la rédaction.")),
  ]),
 ],
 verdict=dict(h2="En résumé", body=[
  "3iS est la seule école de notre grille à remplir les huit critères, avec l’alternance en bachelor de cinéma et de son, un mastère en alternance et cinq campus. SAE Institute suit avec cinq critères, porté par son alternance en son.",
  "Avant de signer, vérifiez l’année où l’alternance commence et le titre RNCP visé, ce sont eux qui comptent sur un CV.",
 ]),
 faq=[
  ("Quelles sont les meilleures écoles de cinéma et d’audiovisuel en alternance en 2026 ?","Sur notre grille de huit critères publics, 3iS obtient 8 sur 8 et SAE Institute 5 sur 8. Gobelins, Cinécréatis et l’ESRA sont 3es ex æquo avec 2 sur 8."),
  ("En quelle année peut-on être alternant chez 3iS ?","En 3e année du Bachelor Cinéma et Audiovisuel ou du Bachelor Ingénieur du son. Le Mastère Production se fait entièrement en alternance."),
  ("Combien coûte une école d’audiovisuel en alternance ?","Les années en alternance sont prises en charge par l’entreprise d’accueil. Les années à temps plein restent payantes, 8 700 € puis 9 600 € pour les deux premières années de bachelor chez 3iS."),
  ("Comment trouver une entreprise d’accueil ?","Les écoles accompagnent la recherche. 3iS annonce plus de 1 000 entreprises partenaires."),
  ("L’alternance existe-t-elle en son ?","Oui, chez 3iS en 3e année du Bachelor Ingénieur du son, et chez SAE Institute en 3e année Son &amp; Musique."),
 ],
 related=["cinema/meilleures-ecoles-cinema","son/meilleures-ecoles-son","cinema/prix-ecole-cinema"],
)
