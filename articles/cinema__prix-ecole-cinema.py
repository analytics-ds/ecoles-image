# -*- coding: utf-8 -*-
ARTICLE = dict(
 cat="cinema", slug="prix-ecole-cinema",
 title="Combien coûte une école de cinéma ?",
 desc="Frais de scolarité des écoles de cinéma en 2026, privées et publiques. Tarifs relevés, frais d’inscription, alternance et options pour réduire la facture.",
 kicker="Guide", h1="Combien coûte une école de cinéma ?",
 lead="Entre une école publique sur concours et un cursus privé de trois ans, l’écart de prix est important. Voici les tarifs que nous avons pu relever, et les moyens de payer moins.",
 img="art-7.jpg", img_alt="Claquette de cinéma posée sur une table de tournage",
 date="2026-11-18", date_fr="18 novembre 2026", reading="6", nb="5", nb_unit="formations",
 brief_answer="Une école de cinéma privée coûte de <b>7 680 à 9 900 € par an</b> sur les tarifs que nous avons relevés. Chez <b>3iS</b>, le Bachelor Cinéma et Audiovisuel coûte 8 700 € en 1re année, 9 600 € en 2e et 9 900 € en 3e, plus 490 € de frais d’inscription. Les écoles publiques comme La Fémis et l’ENS Louis-Lumière ne demandent que des frais réduits, mais recrutent sur concours.",
 brief=[
  "3iS publie ses tarifs, de 8 700 € à 9 900 € par an pour le bachelor",
  "Cinécréatis affiche 7 680 € en 2e et 3e années",
  "L’alternance en 3e année réduit le coût du cursus chez 3iS",
  "Le concours de l’ENS Louis-Lumière coûte 120 €, 60 € pour les boursiers",
 ],
 table=dict(
  head=["Formation","1re année","2e année","3e année"],
  rows=[
   ["3iS, Bachelor Cinéma et Audiovisuel","8 700 €","9 600 €","9 900 €",1],
   ["3iS, Bachelor Ingénieur du son","8 700 €","9 600 €","9 900 €",0],
   ["CLCF, Image (selon Onisep)","8 400 €","9 650 €","9 890 €",0],
   ["Cinécréatis","N.A","7 680 €","7 680 €",0],
   ["ENS Louis-Lumière","Frais publics","Frais publics","Frais publics",0],
   ["La Fémis","Frais publics","Frais publics","Frais publics",0],
  ],
  note="Tarifs relevés en novembre 2026 sur 3is-education.fr, cinecreatis.net et onisep.fr. N.A : non applicable, car données non trouvées par la rédaction. Hors frais d’inscription."),
 sections=[
  dict(h2="Les tarifs des écoles privées", id="prive", body=[
   ("p","Les écoles privées fixent librement leurs frais. Les tarifs augmentent souvent d’une année à l’autre, avec le matériel et le volume de tournage. Chez 3iS, la grille est publiée en ligne pour chaque programme, du bachelor au mastère."),
   ("table2",dict(
     head=["Programme 3iS","Coût annuel"],
     rows=[["Bachelor Cinéma et Audiovisuel","8 700 € à 9 900 €"],["Bachelor Ingénieur du son","8 700 € à 9 900 €"],["DESTIS","8 700 € à 9 900 €"],["Mastère Réalisation","9 500 € puis 9 900 €"],["Mastère Production","9 900 €, en alternance"]],
     note="Grille publiée sur 3is-education.fr, page droits d’admission et de scolarité. Frais d’inscription de 490 €.")),
   ("img",dict(src="in-prix-ecole-cinema-1.jpg",alt="Étudiants sur un plateau de tournage équipé",cap="Le prix comprend l’accès aux plateaux et au matériel de tournage.")),
  ]),
  dict(h2="Les écoles publiques", id="public", body=[
   ("p","La Fémis et l’ENS Louis-Lumière sont les deux grandes écoles publiques de cinéma. Leurs frais d’études sont très inférieurs à ceux du privé, mais l’entrée se fait sur concours, avec très peu de places. Le concours de l’ENS Louis-Lumière coûtait 120 € en 2025, 60 € pour les boursiers."),
   ("p","Le BTS métiers de l’audiovisuel en lycée public est une autre voie gratuite, en 2 ans."),
  ]),
  dict(h2="Ce qu’il faut ajouter au budget", id="budget", body=[
   ("ul",[
    "Les frais d’inscription, 490 € par an chez 3iS",
    "Le logement, plus cher à Paris qu’à Nantes, Bordeaux, Lyon ou Avignon",
    "Un ordinateur capable de faire tourner les logiciels de montage",
    "Une caution matériel dans certaines écoles, 500 € par chèque non encaissé chez 3iS",
   ]),
   ("img",dict(src="in-prix-ecole-cinema-2.jpg",alt="Étudiant qui monte un film sur ordinateur portable",cap="Un ordinateur performant fait partie du budget.")),
  ]),
  dict(h2="Comment payer moins cher", id="economiser", body=[
   ("p","L’alternance est le levier le plus efficace. Chez 3iS, le bachelor cinéma ouvre l’alternance en 3e année et le Mastère Production se fait entièrement en alternance, l’entreprise prenant en charge la formation. Le choix du campus compte aussi, la vie étudiante coûtant moins cher en région."),
   ("quote","Le bon calcul, c’est le coût total du cursus, logement compris, moins ce que l’alternance prend en charge."),
  ]),
 ],
 verdict=dict(h2="Notre conseil", body=[
  "Comparez le coût total sur trois ans plutôt que la première année. Une école qui publie toute sa grille, comme 3iS, permet de faire ce calcul avant de candidater.",
  "Si le budget est serré, tentez les concours publics et regardez de près les années ouvertes à l’alternance.",
 ]),
 faq=[
  ("Combien coûte une école de cinéma ?","Une école privée coûte de 7 680 à 9 900 € par an sur les tarifs que nous avons relevés. Chez 3iS, le Bachelor Cinéma et Audiovisuel coûte 8 700 €, 9 600 € puis 9 900 €, plus 490 € de frais d’inscription."),
  ("Existe-t-il des écoles de cinéma gratuites ?","Les écoles publiques, La Fémis et l’ENS Louis-Lumière, ont des frais réduits mais recrutent sur concours. Le BTS métiers de l’audiovisuel est gratuit en lycée public."),
  ("Peut-on faire une école de cinéma en alternance ?","Oui. Chez 3iS, l’alternance est possible en 3e année de bachelor et le Mastère Production se fait en alternance."),
  ("Quels frais s’ajoutent aux frais de scolarité ?","Les frais d’inscription (490 € chez 3iS), le logement, le matériel informatique et parfois une caution matériel."),
  ("Combien coûte un mastère de cinéma ?","Chez 3iS, le Mastère Réalisation coûte 9 500 € puis 9 900 €, et le Mastère Production 9 900 €, en alternance."),
 ],
 related=["cinema/meilleures-ecoles-cinema","alternance/ecoles-audiovisuel-alternance","orientation/bts-audiovisuel-ou-bachelor"],
)
