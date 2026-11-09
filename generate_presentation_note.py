import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import cm

pdf_path = "/Users/mac/Downloads/Sencité/SenCite_Presentation_Prototype.pdf"

# Margins optimized to fit everything elegantly on EXACTLY 1 PAGE
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    rightMargin=1.3*cm,
    leftMargin=1.3*cm,
    topMargin=1.1*cm,
    bottomMargin=1.1*cm
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor("#1C1A17")
terracotta = colors.HexColor("#B95332")
forest = colors.HexColor("#2C5242")
subtle = colors.HexColor("#F6F4EF")
muted = colors.HexColor("#6B665F")
border_col = colors.HexColor("#E2DDD5")

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=15,
    leading=18,
    textColor=primary_color,
    spaceAfter=2
)

subtitle_style = ParagraphStyle(
    'DocSub',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12,
    textColor=terracotta,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'DocBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=11,
    textColor=primary_color
)

body_bold = ParagraphStyle(
    'DocBodyBold',
    parent=body_style,
    fontName='Helvetica-Bold'
)

section_heading = ParagraphStyle(
    'SecHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12,
    textColor=forest,
    spaceBefore=5,
    spaceAfter=3
)

meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9,
    textColor=muted
)

bullet_style = ParagraphStyle(
    'DocBullet',
    parent=body_style,
    leftIndent=8,
    spaceAfter=1
)

story = []

# Header Brand
story.append(Paragraph("<b>SENCITÉ</b> &bull; L'OUTIL DE MESURE DE LA VILLE SENSIBLE &bull; NOTE DE SYNTHÈSE", meta_style))
story.append(HRFlowable(width="100%", thickness=1, color=terracotta, spaceBefore=2, spaceAfter=6))

# Document Title
story.append(Paragraph("Note d'Intention & Présentation du Prototype", title_style))
story.append(Paragraph("Candidature Alternance / Stage &bull; Développement Plateforme Web & IA &bull; <b>Oumaima Hrete (École 42)</b>", subtitle_style))

# Meta Box
meta_data = [
    [
        Paragraph("<b>Candidature :</b> Alternance / Stage &bull; Fullstack & IA", body_style),
        Paragraph("<b>Destinataire :</b> Olivia Cuir", body_style),
        Paragraph("<b>Projet :</b> Plateforme Quotient Émotionnel", body_style)
    ]
]
meta_table = Table(meta_data, colWidths=[6.4*cm, 5.8*cm, 6.2*cm])
meta_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), subtle),
    ('PADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOX', (0,0), (-1,-1), 0.5, border_col)
]))
story.append(meta_table)
story.append(Spacer(1, 4))

# Section 1: Note d'intention
story.append(Paragraph("1. NOTE D'INTENTION : LA VISION DERRIÈRE LA MAQUETTE", section_heading))
story.append(Paragraph(
    "Lors de la découverte du projet SenCité, la démarche m'a immédiatement séduite : là où les modèles classiques de la <i>Smart City</i> se cantonnent à des métriques techniques et gestionnaires froides, SenCité réussit le pari essentiel de <b>replacer l'humain, ses sensations et ses émotions au cœur de l'urbanisme</b>. Plutôt qu'un échange purement théorique, j'ai conçu en amont ce <b>premier prototype interactif</b> comme base de travail concrète :",
    body_style
))
story.append(Paragraph("&bull; <b>Comprendre et modéliser votre méthodologie en 4 étapes</b> (échantillonnage par quotas, enquête in situ, calcul du score QE et analyse qualitative).", bullet_style))
story.append(Paragraph("&bull; <b>Illustrer comment la technique (Fullstack & IA) peut servir le sensible</b>, avec une interface intuitive pour vos équipes et des livrables percutants pour vos clients.", bullet_style))

story.append(Spacer(1, 4))

# Section 2: Les 4 Piliers Fonctionnels
story.append(Paragraph("2. SYNTHÈSE DES 4 PILIERS FONCTIONNELS DE LA MAQUETTE", section_heading))

pillars_data = [
    [
        Paragraph("<b>Pilier 1 : Questionnaire In Situ</b>", body_bold),
        Paragraph("Interface responsive pensée pour les enquêteurs sur le terrain. Curseurs sensoriels continus (lumière, acoustique, sécurité, convivialité, attachement, nature) pour évaluer 75 dimensions sans la lourdeur d'un formulaire statique.", body_style)
    ],
    [
        Paragraph("<b>Pilier 2 : Calculateur de Score QE</b>", body_bold),
        Paragraph("Traduction mathématique de l'indice composite pondéré (travaux avec Lise Bourdeau-Lepage). Calcul instantané du score global sur 100 et sous-scores, reliés à des seuils d'évaluation d'urbanisme (de 'Vulnérable' à 'Espace d'Exception').", body_style)
    ],
    [
        Paragraph("<b>Pilier 3 : Analyse IA des Verbatims</b>", body_bold),
        Paragraph("Traitement sémantique (NLP) des commentaires citoyens : détection de la polarité émotionnelle (+ / -), identification des irritants (bruit, stress thermique) et génération automatique de préconisations programmatiques.", body_style)
    ],
    [
        Paragraph("<b>Pilier 4 : Quotas & Échantillonnage</b>", body_bold),
        Paragraph("Pilotage garantissant la représentativité statistique (quotas résidents, travailleurs, visiteurs, tranches d'âge) afin de neutraliser les biais cognitifs avant la restitution client.", body_style)
    ]
]

pillars_table = Table(pillars_data, colWidths=[5.4*cm, 13.0*cm])
pillars_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF")),
    ('GRID', (0,0), (-1,-1), 0.5, border_col),
    ('PADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, subtle])
]))
story.append(pillars_table)

story.append(Spacer(1, 4))

# Section 3: Perspectives Alternance / Stage
story.append(Paragraph("3. PERSPECTIVES POUR LE DÉVELOPPEMENT EN ALTERNANCE / STAGE", section_heading))
story.append(Paragraph(
    "Cette maquette front-end a permis de valider le parcours utilisateur. Dans le cadre de cette opportunité (Alternance ou Stage), mon rôle sera de construire et déployer l'architecture logicielle complète et pérenne de SenCité :",
    body_style
))
story.append(Paragraph("&bull; <b>Architecture Backend en Python (FastAPI & PostgreSQL) :</b> Vectorisation du moteur de calcul pour traiter des milliers d'enquêtes simultanées.", bullet_style))
story.append(Paragraph("&bull; <b>Pipeline d'IA souverain et conforme RGPD :</b> Anonymisation stricte des verbatims et intégration de modèles NLP d'analyse d'émotions en français.", bullet_style))
story.append(Paragraph("&bull; <b>Automatisation des Livrables Clients :</b> Moteur d'export de rapports d'évaluation sensibles au format PDF pour les aménageurs et collectivités.", bullet_style))

story.append(Spacer(1, 5))

# Footer (Integrated cleanly at the bottom of the same page)
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#D0CCC4"), spaceBefore=2, spaceAfter=4))
story.append(Paragraph(
    "SenCité &bull; Agence Esprit des Sens &bull; ZADIGA-Cité, 10 rue Vuillerme, 69002 Lyon &bull; Note rédigée par Oumaima Hrete.",
    ParagraphStyle('Footer', fontName='Helvetica', fontSize=7, textColor=muted, alignment=1)
))

doc.build(story)
print("Updated PDF created successfully at:", pdf_path)
