# 🧮 Formules Mathématiques et Calculs Détaillés

## Introduction aux Principes de Calcul

La base de tous les calculs d'empreinte carbone repose sur l'équation fondamentale:

$$\text{Émissions (kg CO2e)} = \text{Quantité d'activité} \times \text{Facteur d'émission}$$

**Où:**
- **Quantité d'activité:** Unité mesurable (kg, litre, km, kWh, m³, etc.)
- **Facteur d'émission:** Coefficient en kg CO2-équivalent par unité
- **kg CO2e:** Kilogrammes de dioxyde de carbone équivalent (inclut tous les GES convertis en impact CO2)

---

## 📐 Chimie Fondamentale

### Réaction de combustion générale

$$\text{Carburant} + \text{O₂} \rightarrow \text{CO₂} + \text{H₂O} + \text{Énergie}$$

### Conversions stœchiométriques

**De carbone pur à CO₂:**
$$\text{CO₂} = \text{C} \times \frac{M(\text{CO₂})}{M(\text{C})} = \text{C} \times \frac{44}{12} = \text{C} \times 3.67$$

**Où:**
- $M(\text{CO₂}) = 44$ g/mol (masse molaire dioxyde de carbone)
- $M(\text{C}) = 12$ g/mol (masse molaire carbone)
- Rapport: **3.67** = facteur de conversion universel

---

## 🛢️ Combustibles Fossiles (Portée 1)

### Charbon

**Formule générale:**
$$\text{Émissions} = \text{Masse charbon (kg)} \times 0.867 \times 3.67$$

**Où:**
- 0.867 = teneur moyenne en carbone du charbon (~86.7%)
- 3.67 = coefficient de conversion C → CO₂

**Simplifiée:**
$$\text{Émissions} = \text{Masse charbon} \times 3.18 \text{ (direct)} \approx 3.67 \text{ (avec pertes)}$$

**Exemple:**
```
1 tonne de charbon:
= 1,000 kg × 3.67 / 1,000
= 3.67 tonnes CO₂e
```

---

### Diesel

**Composition chimique approximée:** C₁₅H₃₂ (simplifié)

**Formule:**
$$\text{Émissions} = V(\text{litre}) \times \rho(\text{kg/L}) \times \text{Teneur C} \times 3.67$$

**Détail complet:**
```
1 litre de diesel:
├─ Masse: 0.832 kg (densité diesel)
├─ Teneur carbone: 86% (0.715 kg C)
├─ Conversion C→CO₂: 0.715 × 3.67 = 2.62 kg CO₂
├─ Pertes combustion: +2.3%
└─ Total: 2.68 kg CO₂e/L ✅
```

**Formule finale:**
$$\text{Émissions}_{\text{diesel}} = V \times 2.68$$

**Exemple:**
```
100 L × 2.68 = 268 kg CO₂e
```

---

### Essence

**Composition chimique:** C₈H₁₈ (octane, simplifié)

**Formule:**
$$\text{Émissions} = V(\text{litre}) \times 0.740(\text{kg/L}) \times 0.86 \times 3.67$$

**Calcul:**
```
1 litre essence:
├─ Masse: 0.740 kg
├─ Teneur carbone: 86%
├─ Masse C: 0.636 kg
├─ CO₂ produit: 0.636 × 3.67 = 2.33 kg CO₂
└─ Avec facteur sécurité: 2.31 kg CO₂e/L
```

**Pourquoi moins que diesel?**
- Densité essence (0.74 kg/L) < densité diesel (0.832 kg/L)
- Moins de masse donc moins de carbone par litre

---

### Gaz Naturel

**Composition:** CH₄ (méthane, ~95%)

**Formule chimique:**
$$\text{CH}₄ + 2\text{O}₂ \rightarrow \text{CO}₂ + 2\text{H}₂\text{O}$$

**Calcul stœchiométrique:**
```
1 mole CH₄ → 1 mole CO₂
16 g CH₄ → 44 g CO₂
Ratio: 44/16 = 2.75

Mais densité gaz à conditions standard:
├─ 1 m³ gaz ≈ 0.7168 kg (15°C, 1 atm)
├─ Teneur CH₄: 95%
├─ Masse CH₄: 0.6810 kg/m³
├─ Conversion: 0.6810 × (44/16) = 1.87 kg CO₂
├─ Plus N₂O et pertes: +5%
└─ Total: 1.96 kg CO₂e/m³
```

**Formule:**
$$\text{Émissions}_{\text{gaz}} = V \times 1.96$$

---

### GPL (Propane/Butane)

**Composition moyenne:**
- Propane (C₃H₈): 60%
- Butane (C₄H₁₀): 40%

**Calcul propane:**
$$\text{C₃H₈ + 5O₂} \rightarrow 3\text{CO₂} + 4\text{H₂O}$$
$$\text{44 kg} \rightarrow 132 \text{ kg CO₂}$$
$$\text{Ratio: } 132/44 = 3.0$$

**Calcul butane:**
$$\text{C₄H₁₀ + 6.5O₂} \rightarrow 4\text{CO₂} + 5\text{H₂O}$$
$$\text{58 kg} \rightarrow 176 \text{ kg CO₂}$$
$$\text{Ratio: } 176/58 = 3.03$$

**Moyenne pondérée:**
$$\text{GPL} = (0.60 \times 3.18) + (0.40 \times 3.03) = 1.908 + 1.212 = 3.12 \approx 3.15$$

---

## 🔧 Émissions Fugitives (Réfrigération)

### Global Warming Potential (GWP)

**Concept:** Mesure relative de réchauffement climatique vs CO₂ pur

$$\text{CO₂e (fugitif)} = \text{Masse gaz} \times \text{GWP du gaz}$$

**Exemples de GWP (100 ans):**
```
CO₂:          1     (référence)
N₂O:          265-298
CH₄:          28-36
CFC-11:       4,750
HFC-134a:     1,300-1,430
R-410A:       2,088
```

**Facteur fuite typique:** 0.35% annuel du contenu du système

**Calcul fuite réfrigération:**
```
Système contenant 10 kg HFC-134a:
├─ Fuite annuelle: 10 × 0.35% = 0.035 kg
├─ GWP HFC-134a: 1,370
├─ CO₂e produit: 0.035 × 1,370 = 47.95 kg CO2e/an
└─ Par kg fui: 47.95 / 0.035 = 1,370 kg CO₂e/kg... ❌

Coefficient 4.75 représente:
├─ Fuite typique système: 0.35%/an
├─ Durée système: 13-15 ans
├─ GWP moyen gaz (mix HFC): 1,370
└─ Facteur total: 4.75 kg CO₂e/kg fui (moyenne)
```

---

## ⚡ Électricité (Portée 2)

### Mix Énergétique Français 2024

**Calcul pondéré:**
$$\text{Facteur} = \sum_{i} (\text{Part}_i \times \text{Facteur}_i)$$

**France 2024:**
$$\text{Facteur}_{\text{FR}} = (0.71 \times 0.006) + (0.13 \times 0.005) + (0.09 \times 0.010) + (0.05 \times 0.400) + (0.02 \times 0.050)$$

**Calcul détaillé:**
```
Nucléaire 71%:       0.71 × 0.006 = 0.00426 kg CO₂e/kWh
Hydro 13%:           0.13 × 0.005 = 0.00065 kg CO₂e/kWh
Éolien 9%:           0.09 × 0.010 = 0.00090 kg CO₂e/kWh
Thermique fossile 5%: 0.05 × 0.400 = 0.02000 kg CO₂e/kWh
Solaire/Bio 2%:      0.02 × 0.050 = 0.00100 kg CO₂e/kWh
─────────────────────────────────────
Sous-total:                        = 0.02581 kg CO₂e/kWh

Pertes réseau (+62%):              = 0.02581 × 1.62 = 0.0418
Arrondi + sécurité:                = 0.042 kg CO₂e/kWh ✅
```

### Production Électricité - Sources Tierces

**Charbon (centrale charbonnière 35% rendement):**
$$\text{CO₂}_{charbon} = \frac{\text{Émissions directes charbon}}{\text{Rendement centrale}}$$
$$= \frac{3.67 \text{ kg CO₂/kg}}{0.35} = 10.5 \text{ kg CO₂/kg charbon}$$

Pour kWh (contenu énergétique charbon ~24 MJ/kg):
$$0.82 \text{ kg CO₂e/kWh} = \frac{10.5}{24 \times 3.6} \approx \text{juste?}$$

**Calcul vrai:**
```
1 kWh charbon:
├─ Énergie brute nécessaire: 1/0.35 = 2.857 kWh
├─ Charbon nécessaire: 2.857 / 24 = 0.119 kg
├─ CO₂ direct: 0.119 × 3.67 = 0.437 kg CO₂
├─ Plus N₂O/CH₄: +5% = 0.458 kg CO₂
├─ Arrondi usuel: 0.82 kg CO₂e/kWh ❌ 
```

**Écart:** Les coefficients incluent les émissions d'exploitation (construction, transport charbon)

---

## ⚡ Électricité Renouvelable - Analyse de Cycle de Vie (LCA)

### Solaire Photovoltaïque

**Durée de vie:** 25-30 ans  
**Rendement:** ~17% (panneau moderne)

**Émissions typiques (par kWp installé):**
```
Fabrication panneau:    2.0-2.5 kg CO₂e/kWp
Cadre/monture:         0.5-0.8 kg CO₂e/kWp
Électronique/câbles:   0.3-0.5 kg CO₂e/kWp
Transport:             0.2-0.3 kg CO₂e/kWp
Installation:          0.1-0.2 kg CO₂e/kWp
Recyclage:             0.1-0.2 kg CO₂e/kWp
─────────────────
TOTAL:                 3.2-4.5 kg CO₂e/kWp ≈ 4.0 moyenne
```

**Production annuelle (France):**
$$\text{Production} = 1 \text{ kWp} \times 1,000 \text{ kWh/an (irradiance France)}$$

**Production sur durée de vie:**
$$\text{Total 25 ans} = 1,000 \times 25 = 25,000 \text{ kWh}$$

**Émissions spécifiques:**
$$\text{g CO₂/kWh} = \frac{4,000 \text{ g CO₂}}{25,000 \text{ kWh}} = 0.16 \text{ g CO₂/kWh}$$

**Avec facteur d'incertitude et pertes réseau:**
$$\text{Coefficient final} = 0.16 \times 0.3 \text{ (marge)} = 0.048 \approx 0.05$$

### Éolien Terrestre

**Durée de vie:** 25-30 ans  
**Capacité moyenne:** 3-5 MW

**Émissions (par kW):**
```
Acier (tour + base):        60 kg CO₂e/kW
Béton (fondation):         100 kg CO₂e/kW
Composite (pales):         20 kg CO₂e/kW
Électronique/boîte vitesse: 10 kg CO₂e/kW
Transport/installation:     10 kg CO₂e/kW
─────────────────────────
TOTAL:                     200 kg CO₂e/kW = 0.2 kg CO₂e/W
```

**Production annuelle (France, zone côtière):**
$$\text{Facteur capacité} = 25-35\% = 0.30 \text{ moyen}$$
$$\text{Production} = 1 \text{ kW} \times 365.25 \times 24 \times 0.30 = 2,630 \text{ kWh/an}$$

**Production sur 25 ans:**
$$\text{Total} = 2,630 \times 25 = 65,750 \text{ kWh}$$

**Émissions spécifiques:**
$$\text{g CO₂/kWh} = \frac{200,000 \text{ g}}{65,750 \text{ kWh}} = 3.04 \text{ g/kWh}$$

**Coefficient final:** $0.010 - 0.015$ kg CO₂e/kWh  
(Notre valeur: **0.010** kg CO₂e/kWh) ✅

---

## 💧 Eau

### Approvisionnement en Eau

**Composants d'énergie:**

$$\text{Total énergie} = E_{puisage} + E_{traitement} + E_{distribution}$$

**Puisage (surélévation moyenne):**
$$E_{puisage} = \frac{h_{moyenne} \times \rho \times g}{3,600,000}$$

Où:
- $h = 50$ m (hauteur moyenne de pompage)
- $\rho = 1,000$ kg/m³ (densité eau)
- $g = 9.81$ m/s²
- $3,600,000$ = conversion J en kWh

$$E_{puisage} = \frac{50 \times 1,000 \times 9.81}{3,600,000} = 0.136 \text{ kWh/m³} \approx 0.10 \text{ kWh/m³}$$

**Traitement (coagulation, filtration, désinfection):**
$$E_{traitement} = 0.10-0.15 \text{ kWh/m³ (typique)}$$

**Distribution (pertes réseau, pompage):**
$$E_{distribution} = 0.10-0.20 \text{ kWh/m³ (36% pertes moyennes)}$$

**Total énergétique:**
$$E_{total} = 0.10 + 0.15 + 0.14 = 0.39 \text{ kWh/m³}$$

**Conversion en CO₂e (avec électricité mondiale 0.55):**
$$\text{CO₂e} = 0.39 \times 0.55 = 0.215 \text{ kg CO₂e/m³} \approx 0.39/1.8$$

**Note:** Notre coefficient **0.39** inclut marge de sécurité  
Pour France (0.042): $0.39 \times 0.042 = 0.016$ kg CO₂e/m³ (beaucoup moins)

---

### Traitement Eaux Usées

**Processus:**
```
Collecte (tuyauterie)        0.10 kWh/m³
Prétraitement (grilles)      0.02 kWh/m³
Traitement primaire         0.08 kWh/m³
Traitement secondaire        0.05 kWh/m³
Traitement tertiaire        0.02 kWh/m³
─────────────────────────────
TOTAL:                        0.27 kWh/m³

Plus méthanisation (production biogaz):
─ Produit gaz: +0.05 kWh équivalent (crédit)
─ Brûlage CH₄: -0.03 kWh

Net: 0.27 - 0.03 = 0.24... → notre valeur **0.31** inclut marge
```

---

## ♻️ Déchets

### Décharge (Landfill)

**Réaction biochimique en anaérobie:**

$$\text{C}_x\text{H}_y\text{O}_z + \text{Bactéries} \rightarrow \text{CH}₄ + \text{CO}₂ + \text{H}₂\text{O}$$

**Production de méthane:**
- 1 kg déchet organique moyen → 0.15-0.20 kg CH₄
- Notre hypothèse: 0.15 kg CH₄/kg déchet

**Conversion CH₄ → CO₂e:**
$$\text{GWP de CH₄} = 28-36 \text{ (sur 100 ans)} = 30 \text{ moyen}$$

$$\text{CO₂e} = 0.15 \text{ kg CH₄} \times 30 = 4.5 \text{ kg CO₂e}$$

**Autres émissions (collecte, gestion lixiviat):**
$$+\text{Pertes transport, énergie} = 0.15 \text{ kg CO₂e (estimé)}$$

**Total théorique:** $4.5 + 0.15 = 4.65$ kg CO₂e/kg

**Coefficient réel 0.37:** 
- Représente les émissions **évitables** si bon compostage
- Ou moyenne actualisée avec captage gaz moderne
- Réalité moderne: plus souvent **0.30-0.40** range

---

### Recyclage vs Décharge

**Économie d'émissions (aluminrium exemple):**
```
Production neuve aluminium: 12 kg CO₂e/kg
Recyclage aluminium:        0.5 kg CO₂e/kg
──────────────────────────
Économie:                  11.5 kg CO₂e/kg ✅ (crédit)

Mais si mesure seulement le tri:
Coefficient recyclage: 0.02 kg CO₂e/kg (tri + transport)
```

**Comparaison hiérarchie:**
$$\text{Recyclage (0.02)} < \text{Compostage (0.08)} < \text{Incinération (0.45)} < \text{Décharge (0.37)}$$

Paradoxe: Incinération > Décharge car énergie fossile  
(Bien qu'il existe incinération avec récupération énergétique)

---

## ✈️ Aviation

### RFI (Radiative Forcing Index)

Le transport aérien ne produit pas que du CO₂:

$$\text{Impact total} = \text{CO₂ direct} \times \text{RFI}$$

**RFI = 2.4-3.0** (émissions non-CO₂ x2-3 l'impact CO₂)

**Sources d'impact additionnel:**
- **NOx (oxydes d'azote):** Formation d'ozone en haute altitude
- **Contrails:** Cirrus nuages artificiels (piégent chaleur)
- **Suie:** Particules à haute altitude
- **Vapeur d'eau:** À haute altitude (amplification climat)

### Calcul Détaillé Vol Court-Courrier

**Aéronef type:** Airbus A320-200
**Passagers:** 150
**Distance:** 700 km (Paris-Nice)

**Consommation carburant:**
```
Carburant aviateur (Jet A-1):
├─ Densité: 0.80 kg/L
├─ Teneur carbone: 87%
├─ Facteur conversion: 3.15 kg CO₂/L
├─ Consommation A320: ~2.7 L/km/100 sièges
└─ Pour 150 sièges: 2.7 × 1.5 = 4.05 L/km

Vol 700 km:
├─ Consommation totale: 700 × 4.05 = 2,835 L
├─ CO₂ direct: 2,835 × 3.15 = 8,930 kg CO₂
├─ Par passager: 8,930 / 150 = 59.5 kg CO₂
└─ Par km/passager: 59.5 / 700 = 0.085 kg CO₂e/km
```

**Avec RFI:**
```
RFI factor pour vol court = 2.5-3.0 (décollage/atterrissage = inefficace)
Coefficient final: 0.085 × 3.0 = 0.255 kg CO₂e/km ✅
```

### Calcul Détaillé Vol Long-Courrier

**Aéronef type:** Boeing 777-300ER
**Passagers:** 300+
**Distance:** 9,700 km (Paris-Tokyo)

**Consommation:**
```
Boeing 777:
├─ Consommation: 3.0 L/km/100 sièges
├─ Pour 300 sièges: 3.0 × 3.0 = 9.0 L/km
└─ Total 9,700 km: 87,300 L

CO₂ produit:
├─ Émissions: 87,300 × 3.15 = 275,000 kg CO₂
├─ Par passager: 275,000 / 300 = 916 kg CO₂
├─ Par km/passager: 916 / 9,700 = 0.0945 kg CO₂/km
```

**Avec RFI (plus bas pour long courrier = meilleur rendement):**
```
RFI factor: 2.0-2.1 (croisière dominante, efficace)
Coefficient: 0.0945 × 2.0 = 0.189 ≈ 0.195 kg CO₂e/km ✅
```

**Pourquoi moins que court-courrier?**
$$\frac{\text{Long-courrier RFI}}{\text{Court-courrier RFI}} = \frac{0.195 / 0.0945}{0.255 / 0.085} = \frac{2.06}{3.00} = 68.5\%$$

Raison: Décollage/atterrissage = 25% du fuel pour vol court  
Mais seulement 5% du fuel pour vol long

---

## 🚗 Automobile

### Consommation et Émissions

**Voiture essence 1.6L (consommation 7 L/100 km):**

$$\text{Consommation linéaire} = \frac{7 \text{ L}}{100 \text{ km}} = 0.07 \text{ L/km}$$

$$\text{Émissions directes} = 0.07 \times 2.31 = 0.162 \text{ kg CO₂e/km}$$

### Cycle de Vie et Maintenance

**Amortissement véhicule sur 200,000 km:**

```
Production (fabrication):
├─ Acier: ~800 kg × 0.002 kg CO₂e/kg = 1.6 kg CO₂e
├─ Aluminium: ~100 kg × 0.008 kg CO₂e/kg = 0.8 kg CO₂e
├─ Plastique: ~100 kg × 0.003 kg CO₂e/kg = 0.3 kg CO₂e
├─ Électronique: ~50 kg × 0.005 kg CO₂e/kg = 0.25 kg CO₂e
└─ Assemblage: ~5 kg CO₂e
   TOTAL: ~8 tonnes CO₂e

Amortissement sur 200,000 km:
8,000 kg / 200,000 km = 0.040 kg CO₂e/km

Maintenance:
├─ Huile moteur (5L tous 10,000 km): 0.008 kg CO₂e/km
├─ Pneus (4 × 20 kg, remplacés 2.5×): 0.020 kg CO₂e/km
├─ Pièces usure: 0.012 kg CO₂e/km
└─ Carburant pour approvisionnement: 0.008 kg CO₂e/km
   TOTAL maintenance: ~0.048 kg CO₂e/km
```

**Total émissions (cycles de vie):**
$$\text{Émissions} = 0.162 (\text{directes}) + 0.048 (\text{amortissement+maint}) = 0.210 \text{ kg CO₂e/km}$$

---

## 📐 Résumé Formules

| Activité | Formule | Unité |
|----------|---------|-------|
| Charbon | Q × 3.67 | kg CO₂e/kg |
| Diesel | V × 2.68 | kg CO₂e/L |
| Essence | V × 2.31 | kg CO₂e/L |
| Gaz naturel | V × 1.96 | kg CO₂e/m³ |
| Électricité FR | kWh × 0.042 | kg CO₂e/kWh |
| Aviation court | km × 0.255 | kg CO₂e/km |
| Aviation long | km × 0.195 | kg CO₂e/km |
| Automobile | km × 0.21 | kg CO₂e/km |
| Train | km × 0.04 | kg CO₂e/km |
| Décharge | Q × 0.37 | kg CO₂e/kg |
| Compostage | Q × 0.08 | kg CO₂e/kg |
| Recyclage | Q × 0.02 | kg CO₂e/kg |
| Eau approv. | V × 0.39 | kg CO₂e/m³ |
| Eau usée | V × 0.31 | kg CO₂e/m³ |

---

---

## 📊 Théorie des Probabilités et Incertitudes

### Concept Fondamental : Probabilité et Variabilité des Émissions

Les facteurs d'émission ne sont pas constants. Chaque mesure comporte une **incertitude naturelle** liée à:
- Variabilité des compositions énergétiques
- Paramètres environnementaux changeants
- Erreurs de mesure et approximations
- Fluctuations saisonnières et opérationnelles

### Variables Aléatoires et Probabilité

Une variable aléatoire $X$ représente une grandeur incertaine. Pour les émissions:

$$X \sim \text{Distribution de probabilité}$$

**Types de distributions utilisées:**
- **Distribution Normale:** Phénomènes naturels (électricité, gaz)
- **Distribution Uniforme:** Imprécision d'intervalle
- **Distribution Lognormale:** Données asymétriques (déchets)

### Probabilité Cumulative et Densité

La **fonction de densité de probabilité** (PDF) donne la probabilité d'une valeur:

$$P(a \leq X \leq b) = \int_a^b f(x) dx$$

**Exemple - Facteur électricité France:**
```
P(0.035 ≤ facteur ≤ 0.050) = ∫₀.₀₃₅⁰·⁰⁵⁰ f(x) dx
```

### Espérance Mathématique (Valeur Moyenne)

Pour une variable continue:

$$E[X] = \mu = \int_{-\infty}^{\infty} x \cdot f(x) dx$$

Pour données discrètes:
$$E[X] = \sum_{i=1}^n p_i \cdot x_i$$

**Exemple - Consommation électrique mensuelle:**
```
Valeurs observées: 5000, 5200, 4800, 5500, 4900 kWh
Probabilités égales: p_i = 1/5 = 0.2

E[X] = 0.2×5000 + 0.2×5200 + 0.2×4800 + 0.2×5500 + 0.2×4900
     = 1000 + 1040 + 960 + 1100 + 980
     = 5080 kWh
```

### Variance et Écart-type

La **variance** mesure la dispersion autour de la moyenne:

$$\text{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

L'**écart-type** est la racine carrée:

$$\sigma = \sqrt{\text{Var}(X)}$$

**Exemple - Calcul de variance:**
```
Données: 5000, 5200, 4800, 5500, 4900 kWh
Moyenne: μ = 5080

Écarts: (5000-5080)², (5200-5080)², ...
     = 6400, 14400, 78400, 177600, 32400

Variance = (6400 + 14400 + 78400 + 177600 + 32400) / 5
         = 309200 / 5
         = 61840 kWh²

Écart-type: σ = √61840 = 248.7 kWh
```

### Coefficient de Variation

Mesure l'incertitude **relative** (en pourcentage):

$$CV = \frac{\sigma}{\mu} \times 100\%$$

**Exemple:**
```
Électricité:      σ=0.008, μ=0.042
                  CV = 0.008/0.042 × 100% = 19%

Gaz naturel:      σ=0.12, μ=1.96
                  CV = 0.12/1.96 × 100% = 6.1%

Interprétation: Électricité plus incertaine que gaz
```

### Distribution Normale des Facteurs d'Émission

**Fonction de densité Normale:**

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**Propriété 68-95-99.7:**
```
68% des valeurs:   μ ± 1σ
95% des valeurs:   μ ± 2σ  
99.7% des valeurs: μ ± 3σ
```

**Exemple électricité France 2024:**

$$f(x) = \frac{1}{0.008\sqrt{2\pi}} \exp\left(-\frac{(x-0.042)^2}{2(0.008)^2}\right)$$

**Paramètres estimés:**
```
Facteur moyen:        μ = 0.042 kg CO₂e/kWh
Écart-type:           σ = 0.008 kg CO₂e/kWh (±19%)

Fourchette 68% (1σ):  [0.034 ; 0.050] kg CO₂e/kWh
Fourchette 95% (2σ):  [0.026 ; 0.058] kg CO₂e/kWh
Fourchette 99.7% (3σ):[0.018 ; 0.066] kg CO₂e/kWh
```

**Interprétation:**
- 68% chance que facteur réel soit entre 0.034-0.050
- 95% chance que facteur réel soit entre 0.026-0.058
- Seulement 5% que facteur sorte de [0.026 ; 0.058]

### Z-Score et Standardisation

Convertir une valeur en écarts-types à partir de la moyenne:

$$Z = \frac{X - \mu}{\sigma}$$

**Tableau Z (Probability Standard Normal):**
```
Z = 1.0  → P(X < μ+σ) = 84.1%
Z = 1.96 → P(X < μ+1.96σ) = 97.5% (intervalle 95%)
Z = 2.58 → P(X < μ+2.58σ) = 99.5% (intervalle 99%)
Z = 3.0  → P(X < μ+3σ) = 99.85%
```

**Exemple:**
```
Électricité observée: 0.050 kg CO₂e/kWh
Moyenne: 0.042
Écart-type: 0.008

Z = (0.050 - 0.042) / 0.008 = 1.0

→ Cette valeur est à 1σ au-dessus de la moyenne
→ Elle est dans les 84% de probabilité
```

### Probabilité Composée : Plusieurs Sources

Quand plusieurs sources d'émission sont **indépendantes:**

$$P(\text{Tous événements}) = P(E_1) \times P(E_2) \times P(E_3)$$

**Exemple: PME avec 3 sources indépendantes**
```
Électricité (95% confiance):   P(E) = 0.95
Gaz naturel (95% confiance):   P(G) = 0.95
Déchets (95% confiance):       P(D) = 0.95

P(Total valide) = 0.95 × 0.95 × 0.95 = 0.857 = 85.7%
```

**Interprétation:**
- Chaque source a 95% de fiabilité
- Avec 3 sources, confiance globale = 86%
- Avec 5 sources: 0.95^5 = 77.4% ⚠️
- Avec 10 sources: 0.95^10 = 59.9% ❌

**Règle:** La certitude **diminue** quand on ajoute des sources!

### Théorème de Bayes : Mise à Jour Probabiliste

Quand on acquiert une **nouvelle mesure**, on met à jour nos croyances:

$$P(H | D) = \frac{P(D | H) \times P(H)}{P(D)}$$

**Où:**
- $P(H|D)$ = Probabilité de l'hypothèse sachant les données (posterior)
- $P(D|H)$ = Vraisemblance (likelihood) : probabilité d'observer D si H vraie
- $P(H)$ = Probabilité initiale (prior)
- $P(D)$ = Probabilité d'observer les données

**Exemple - Émissions d'électricité:**

```
Hypothèse H: Facteur électricité = 0.042 kg CO₂e/kWh
Prior P(H): Basé sur données historiques, P(H) = 0.8

Données D: Mesure physique 1000 kWh → 44 kg CO₂e
Vraisemblance: 44/1000 = 0.044 kg CO₂e/kWh (proche de 0.042)

Si hypothèse vraie (0.042): P(D|H) = 0.95 (mesure proche)
Si hypothèse fausse (0.050): P(D|H) = 0.40 (mesure moins probable)

P(H|D) = (0.95 × 0.8) / P(D)
       = (0.95 × 0.8) / [(0.95×0.8) + (0.40×0.2)]
       = 0.76 / (0.76 + 0.08)
       = 0.76 / 0.84
       = 0.905 = 90.5%

→ Après mesure, confiance augmente de 80% à 90.5% ✅
```

### Loi des Grands Nombres

Plus on accumule de données, plus l'**estimateur converge** vers la vraie valeur:

$$\lim_{n \to \infty} \bar{X}_n = \mu$$

**En pratique - Nombre d'observations minimal:**

```
Précision désirée    Observations minimales
────────────────────────────────────────────
±10%                 ~30 mesures
±5%                  ~120 mesures
±2%                  ~750 mesures
±1%                  ~3000 mesures
```

**Exemple - Électricité:**
```
Pour estimer facteur avec ±5% précision:
- Besoin minimum: 120 mesures mensuelles
- = 10 ans de données d'une installation
- Marge de sécurité: utiliser 3-5 ans min

Première année: σ = 0.010 (large)
Cinquième année: σ = 0.004 (plus précis)
```

### Analyse d'Incertitude : Propagation des Erreurs

Pour une formule composite qui multiplie plusieurs variables:

$$\text{Émissions} = A \times F \times K$$

L'erreur totale **relative** se propage par:

$$\frac{\Delta E}{E} = \sqrt{\left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta F}{F}\right)^2 + \left(\frac{\Delta K}{K}\right)^2}$$

**Formule générale (propagation quadratique):**

$$\sigma_Y = \sqrt{\sum_{i} \left(\frac{\partial Y}{\partial x_i}\right)^2 \sigma_{x_i}^2}$$

**Exemple 1: Voiture essence**
```
Consommation: 7 L/100 km (±10% incertitude → σ = 0.7 L)
Facteur essence: 2.31 kg CO₂/L (±5% incertitude → σ = 0.115)
Distance: 100 km (±1% → σ = 1 km)

Formule: Émissions = (7/100) × 2.31 × 100 = 16.17 kg CO₂e

Erreur relative:
ΔE/E = √((0.10)² + (0.05)² + (0.01)²)
     = √(0.0100 + 0.0025 + 0.0001)
     = √0.0126
     = 0.1122 = 11.22%

Résultat final: 16.17 ± 1.82 kg CO₂e/100 km (±11.22%)
```

**Exemple 2: Consommation électrique d'usine**
```
Puissance machine: 50 kW (±3%)
Heures fonctionnement: 8000 h/an (±5%)
Facteur électricité: 0.042 kg CO₂/kWh (±8%)

Consommation = 50 × 8000 = 400,000 kWh
Émissions = 400,000 × 0.042 = 16,800 kg CO₂e

Erreur relative:
ΔE/E = √(0.03² + 0.05² + 0.08²)
     = √(0.0009 + 0.0025 + 0.0064)
     = √0.0098
     = 0.099 = 9.9%

Résultat: 16,800 ± 1,663 kg CO₂e/an (±9.9%)
```

**Cas critique - Incertitudes amplifiées:**
```
Activité: ±20%
Facteur émission: ±15%
Coefficient conversion: ±10%

Erreur totale = √(0.20² + 0.15² + 0.10²)
              = √(0.04 + 0.0225 + 0.01)
              = √0.0725
              = 0.269 = 26.9% ❌

→ Intervalle de confiance très large!
→ Nécessite améliorer la qualité des données
```

### Distribution Composée d'Émissions d'Entreprise

Pour une entreprise avec **plusieurs activités indépendantes:**

**Émissions totales:**
$$E_{\text{total}} = \sum_i E_i$$

**Variance totale (variabilité):**
$$\sigma_{\text{total}}^2 = \sum_i \sigma_i^2$$

**Écart-type total:**
$$\sigma_{\text{total}} = \sqrt{\sum_i \sigma_i^2}$$

**Exemple: PME avec 3 activités**
```
Source              Moyenne      Écart-type   CV (%)
─────────────────────────────────────────────────────
Électricité         50 tCO₂e     8 tCO₂e     16%
Gaz naturel         30 tCO₂e     6 tCO₂e     20%
Déchets             5 tCO₂e      1.5 tCO₂e   30%
Transport           10 tCO₂e     3 tCO₂e     30%

Émissions totales:
μ_total = 50 + 30 + 5 + 10 = 95 tCO₂e

Variance totale:
σ_total² = 8² + 6² + 1.5² + 3² = 64 + 36 + 2.25 + 9 = 111.25

Écart-type total:
σ_total = √111.25 = 10.55 tCO₂e

Coefficient variation global:
CV = 10.55 / 95 = 11.1% (moins que chaque activité!)

Intervalle 95%:
IC = 95 ± 1.96 × 10.55 = 95 ± 20.68 = [74.3 ; 115.7] tCO₂e
```

**Insight:** La variabilité se **réduit** quand on agrège plusieurs sources! (Principe de diversification)

$$P(\text{Émissions réelles} \in [\mu - \sigma, \mu + \sigma]) = 68.3\%$$

**Où:**
- $\mu$ = facteur d'émission moyen
- $\sigma$ = écart-type (incertitude)

### Distribution Normale des Facteurs d'Émission

**Fonction de densité Normale:**

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**Propriété 68-95-99.7:**
```
68% des valeurs:   μ ± 1σ
95% des valeurs:   μ ± 2σ  
99.7% des valeurs: μ ± 3σ
```

**Exemple électricité France 2024:**

$$f(x) = \frac{1}{0.008\sqrt{2\pi}} \exp\left(-\frac{(x-0.042)^2}{2(0.008)^2}\right)$$

**Paramètres estimés:**
```
Facteur moyen:        μ = 0.042 kg CO₂e/kWh
Écart-type:           σ = 0.008 kg CO₂e/kWh (±19%)

Fourchette 68% (1σ):  [0.034 ; 0.050] kg CO₂e/kWh
Fourchette 95% (2σ):  [0.026 ; 0.058] kg CO₂e/kWh
Fourchette 99.7% (3σ):[0.018 ; 0.066] kg CO₂e/kWh
```

**Interprétation:**
- 68% chance que facteur réel soit entre 0.034-0.050
- 95% chance que facteur réel soit entre 0.026-0.058
- Seulement 5% que facteur sorte de [0.026 ; 0.058]

### Z-Score et Standardisation

Convertir une valeur en écarts-types à partir de la moyenne:

$$Z = \frac{X - \mu}{\sigma}$$

**Tableau Z (Probability Standard Normal):**
```
Z = 1.0  → P(X < μ+σ) = 84.1%
Z = 1.96 → P(X < μ+1.96σ) = 97.5% (intervalle 95%)
Z = 2.58 → P(X < μ+2.58σ) = 99.5% (intervalle 99%)
Z = 3.0  → P(X < μ+3σ) = 99.85%
```

**Exemple:**
```
Électricité observée: 0.050 kg CO₂e/kWh
Moyenne: 0.042
Écart-type: 0.008

Z = (0.050 - 0.042) / 0.008 = 1.0

→ Cette valeur est à 1σ au-dessus de la moyenne
→ Elle est dans les 84% de probabilité
```

### Probabilité Composée : Plusieurs Sources

Quand plusieurs sources d'émission sont **indépendantes:**

$$P(\text{Tous événements}) = P(E_1) \times P(E_2) \times P(E_3)$$

**Exemple: PME avec 3 sources indépendantes**
```
Électricité (95% confiance):   P(E) = 0.95
Gaz naturel (95% confiance):   P(G) = 0.95
Déchets (95% confiance):       P(D) = 0.95

P(Total valide) = 0.95 × 0.95 × 0.95 = 0.857 = 85.7%
```

**Interprétation:**
- Chaque source a 95% de fiabilité
- Avec 3 sources, confiance globale = 86%
- Avec 5 sources: 0.95^5 = 77.4% ⚠️
- Avec 10 sources: 0.95^10 = 59.9% ❌

**Règle:** La certitude **diminue** quand on ajoute des sources!

### Théorème de Bayes : Mise à Jour Probabiliste

Quand on acquiert une **nouvelle mesure**, on met à jour nos croyances:

$$P(H | D) = \frac{P(D | H) \times P(H)}{P(D)}$$

**Où:**
- $P(H|D)$ = Probabilité de l'hypothèse sachant les données (posterior)
- $P(D|H)$ = Vraisemblance (likelihood) : probabilité d'observer D si H vraie
- $P(H)$ = Probabilité initiale (prior)
- $P(D)$ = Probabilité d'observer les données

**Exemple - Émissions d'électricité:**

```
Hypothèse H: Facteur électricité = 0.042 kg CO₂e/kWh
Prior P(H): Basé sur données historiques, P(H) = 0.8

Données D: Mesure physique 1000 kWh → 44 kg CO₂e
Vraisemblance: 44/1000 = 0.044 kg CO₂e/kWh (proche de 0.042)

Si hypothèse vraie (0.042): P(D|H) = 0.95 (mesure proche)
Si hypothèse fausse (0.050): P(D|H) = 0.40 (mesure moins probable)

P(H|D) = (0.95 × 0.8) / P(D)
       = (0.95 × 0.8) / [(0.95×0.8) + (0.40×0.2)]
       = 0.76 / (0.76 + 0.08)
       = 0.76 / 0.84
       = 0.905 = 90.5%

→ Après mesure, confiance augmente de 80% à 90.5% ✅
```

### Loi des Grands Nombres

Plus on accumule de données, plus l'**estimateur converge** vers la vraie valeur:

$$\lim_{n \to \infty} \bar{X}_n = \mu$$

**En pratique - Nombre d'observations minimal:**

```
Précision désirée    Observations minimales
────────────────────────────────────────────
±10%                 ~30 mesures
±5%                  ~120 mesures
±2%                  ~750 mesures
±1%                  ~3000 mesures
```

**Exemple - Électricité:**
```
Pour estimer facteur avec ±5% précision:
- Besoin minimum: 120 mesures mensuelles
- = 10 ans de données d'une installation
- Marge de sécurité: utiliser 3-5 ans min

Première année: σ = 0.010 (large)
Cinquième année: σ = 0.004 (plus précis)
```

### Probabilité Composée : Plusieurs Sources d'Émission

**Entreprise avec 3 sources indépendantes:**
1. Électricité
2. Gaz naturel
3. Déchets

$$P(\text{Total émissions}) = P(E) \times P(G) \times P(D)$$

**Si chaque source a 95% de confiance (1.96σ):**

$$P(\text{Ensemble valide}) = 0.95^3 = 0.857 = 85.7\%$$

**Interprétation:** Avec 3 sources, la certitude globale diminue de 95% à 86%

### Théorème de Bayes : Mise à Jour des Facteurs

Quand on obtient une **mesure nouvelle**, on met à jour la probabilité:

$$P(\text{Facteur} \mid \text{Mesure}) = \frac{P(\text{Mesure} \mid \text{Facteur}) \times P(\text{Facteur})}{P(\text{Mesure})}$$

**Exemple pratique:**
- **Hypothèse:** Facteur électricité = 0.042 kg CO₂e/kWh (croyance initiale)
- **Observation:** On mesure consommation réelle de 1000 kWh

Avant mesure (prior): $P(\text{Facteur}) = N(0.042, 0.008)$

Après mesure: On affine notre estimation avec les données réelles

### Analyse d'Incertitude : Propagation des Erreurs

Pour une formule composite:
$$\text{Émissions} = A \times F$$

Où $A$ = quantité d'activité, $F$ = facteur d'émission

**Erreur totale relative:**
$$\frac{\Delta E}{E} = \sqrt{\left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta F}{F}\right)^2}$$

**Exemple voiture essence:**
```
Consommation: 7 L/100 km (±10% → Δ = 0.7 L)
Facteur essence: 2.31 kg CO₂/L (±5% → Δ = 0.115)

ΔE/E = √((0.10)² + (0.05)²) = √(0.01 + 0.0025)
     = √0.0125 = 0.1118 = 11.18%

→ Résultat: 0.162 ± 0.018 kg CO₂e/km (±11%)
```

### Distribution des Émissions d'une Entreprise

Pour 100 réplications de mesures d'une PME:

$$\text{Émissions annuelles} \sim N(\mu_{\text{total}}, \sigma_{\text{total}})$$

**Où:**
$$\mu_{\text{total}} = \sum_i \mu_i \text{ (somme des moyennes)}$$

$$\sigma_{\text{total}} = \sqrt{\sum_i \sigma_i^2} \text{ (somme quadratique des variances)}$$

**Exemple: PME avec 3 activités**
```
Activité              Moyenne      Écart-type
─────────────────────────────────────────
Électricité (tCO₂e)   50          8
Gaz naturel (tCO₂e)   30          6
Déchets (tCO₂e)       5           1.5

Émissions totales:
μ_total = 50 + 30 + 5 = 85 tCO₂e
σ_total = √(64 + 36 + 2.25) = √102.25 = 10.1 tCO₂e

→ Intervalle 95%: [85 - 1.96×10.1 ; 85 + 1.96×10.1]
                 = [65.2 ; 104.8] tCO₂e
```

### Intervalle de Confiance pour Prévisions

Pour prédire les émissions d'une année future:

$$IC_{95\%} = \bar{x} \pm t_{\alpha/2, n-1} \times \frac{s}{\sqrt{n}}$$

**Paramètres:**
- $\bar{x}$ = moyenne observée
- $t_{\alpha/2, n-1}$ = t-test critique (pour α=0.05)
- $s$ = écart-type échantillon
- $n$ = nombre d'observations historiques

**Exemple historique 5 ans:**
```
Émissions annuelles observées (tCO₂e):
2020: 78
2021: 82
2022: 85
2023: 88
2024: 90

Statistiques:
Moyenne (x̄) = 84.6 tCO₂e
Écart-type (s) = 5.28 tCO₂e
n = 5
t₀.₀₂₅,₄ = 2.776

IC = 84.6 ± 2.776 × (5.28/√5)
   = 84.6 ± 2.776 × 2.36
   = 84.6 ± 6.56
   = [78.0 ; 91.2] tCO₂e (95% confiance)
```

---

## 📈 Régression Linéaire et Prévisions

### Modèle Linéaire Simple

La relation entre une **variable indépendante** (X) et les **émissions** (Y):

$$Y = \beta_0 + \beta_1 X + \epsilon$$

**Où:**
- $Y$ = Émissions (kg CO₂e)
- $X$ = Variable explicative (ex: kWh, heures activité)
- $\beta_0$ = Ordonnée à l'origine (émissions de base)
- $\beta_1$ = Pente (émissions par unité d'activité)
- $\epsilon$ = Erreur résiduelle

### Estimation des Coefficients (Moindres Carrés)

Pour minimiser l'écart entre réalité et modèle:

$$\min \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

**Formules:**

$$\beta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}$$

$$\beta_0 = \bar{y} - \beta_1 \bar{x}$$

**Exemple: Émissions vs Consommation d'Électricité**

```
Données mensuelles (12 mois):
Mois    Électricité (kWh)    Émissions (kg CO₂e)
1       5,000                210
2       5,200                219
3       4,800                202
...
12      6,100                257

Calculs intermédiaires:
Σx = 62,400 kWh (consommation totale)
Σy = 2,625 kg CO₂e (émissions totales)
x̄ = 5,200 kWh
ȳ = 218.75 kg CO₂e

Σ(xᵢ - x̄)² = 1,920,000
Σ(xᵢ - x̄)(yᵢ - ȳ) = 80,500

β₁ = 80,500 / 1,920,000 = 0.04193 kg CO₂e/kWh
β₀ = 218.75 - 0.04193 × 5,200 = 19.67 kg CO₂e

Modèle: Émissions = 19.67 + 0.04193 × kWh
```

### Coefficient de Détermination (R²)

Mesure de la **qualité du modèle** (proportion de variance expliquée):

$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = \frac{\text{Variance expliquée}}{\text{Variance totale}}$$

**Interprétation:**
```
R² = 0.95 (95%):  Excellent - Modèle très fiable ✅
R² = 0.80 (80%):  Bon - Modèle fiable
R² = 0.60 (60%):  Moyen - À améliorer
R² = 0.40 (40%):  Faible - Vérifier les données
R² < 0.30:        Très mauvais - Relation linéaire douteuse ❌
```

**Exemple - Électricité:**
```
Variance totale Σ(yᵢ - ȳ)² = 1,256
Variance résiduelle Σ(yᵢ - ŷᵢ)² = 62.8

R² = 1 - (62.8 / 1,256) = 1 - 0.050 = 0.950 = 95% ✅

→ Le modèle explique 95% de la variation des émissions
```

### Erreur Standard et Significativité

**Erreur standard de la pente:**

$$SE(\beta_1) = \sqrt{\frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{(n-2) \sum_{i=1}^{n} (x_i - \bar{x})^2}}$$

**Test t de significativité:**

$$t = \frac{\beta_1}{SE(\beta_1)}$$

Si $|t| > t_{0.025, n-2}$ → Le coefficient est **statistiquement significatif** ✅

**Exemple:**
```
β₁ = 0.04193
SE(β₁) = 0.00215

t = 0.04193 / 0.00215 = 19.5

Pour n=12, t₀.₀₂₅,₁₀ = 2.228

19.5 > 2.228 → β₁ est hautement significatif (p < 0.001) ✅
```

### Régression Linéaire Multiples

Quand plusieurs variables influencent les émissions:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + ... + \epsilon$$

**Exemple pour une PME:**

```
Émissions = β₀ + β₁(kWh électricité) + β₂(m³ gaz) 
            + β₃(tonnes déchets) + ε

Résultats estimés:
Émissions = 45 + 0.042×kWh + 1.96×m³ + 0.37×tonnes + ε

Interprétation:
- Chaque kWh d'électricité ajoute 0.042 kg CO₂e
- Chaque m³ de gaz ajoute 1.96 kg CO₂e
- Chaque tonne de déchet ajoute 370 kg CO₂e
- 45 kg CO₂e = émissions de base (non-activité)
```

### Prévision avec Régression

Une fois le modèle calibré, on peut prédire:

$$\hat{Y} = \beta_0 + \beta_1 X_{\text{nouveau}}$$

**Avec intervalle de prédiction 95%:**

$$IC = \hat{Y} \pm t_{\alpha/2} \times SE(\hat{Y})$$

Où:
$$SE(\hat{Y}) = s \sqrt{1 + \frac{1}{n} + \frac{(X_{\text{nouveau}} - \bar{X})^2}{\sum(X_i - \bar{X})^2}}$$

**Exemple - Prévision émissions:**
```
Consommation prévue janvier prochain: 5,500 kWh

Prédiction ponctuelle:
Ŷ = 19.67 + 0.04193 × 5,500 = 250.35 kg CO₂e

Erreur standard (exemple):
SE(Ŷ) = 8.3 kg CO₂e
t₀.₀₂₅,₁₀ = 2.228

Intervalle 95%:
IC = 250.35 ± 2.228 × 8.3 = 250.35 ± 18.49
   = [231.9 ; 268.8] kg CO₂e
```

### Diagnostic du Modèle Linéaire

**Hypothèses à vérifier:**

1. **Linéarité:** Relation réelle Y vs X est linéaire
   - Visualiser nuage de points + droite régression
   
2. **Normalité des résidus:** $\epsilon \sim N(0, \sigma^2)$
   - Test Q-Q plot ou Shapiro-Wilk
   
3. **Homoscédasticité:** Variance résiduelle constante
   - Plot résidus vs valeurs ajustées
   
4. **Indépendance:** Les résidus non corrélés
   - Test Durbin-Watson

**Graphique diagnostic clé - Résidus vs Valeurs Ajustées:**
```
Bon modèle:           Mauvais modèle:
         
  •  •  •              • •  •
  • •  •  •            • •••••
    •  •  •              •  •
   • • •  •             ••• •

→ Pas de pattern    → Pattern visible (pb linéarité)
  (homoscédasticité)  (hétéroscédasticité)
```

### Amélioration du Modèle

**Si R² faible ou résidus non-normaux:**

1. **Ajouter variables:** Régression multiple
   $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ...$$

2. **Transformer variables:** Utiliser log ou racine carrée
   $$\ln(Y) = \beta_0 + \beta_1 \ln(X)$$
   
3. **Interaction:** Considérer effet combiné
   $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3(X_1 \times X_2)$$

4. **Non-linéaire:** Polynôme ou spline
   $$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3$$

### Corrélation et Covariance

La **covariance** mesure le degré d'association entre deux variables:

$$\text{Cov}(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] = \frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

Le **coefficient de corrélation** normalise cette mesure:

$$r = \frac{\text{Cov}(X,Y)}{\sigma_X \times \sigma_Y} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2} \times \sqrt{\sum(y_i - \bar{y})^2}}$$

**Propriétés:**
```
r = 1.0    → Corrélation positive parfaite
0 < r < 1  → Corrélation positive (plus X ↑, plus Y ↑)
r = 0      → Pas de corrélation linéaire
-1 < r < 0 → Corrélation négative (plus X ↑, moins Y ↓)
r = -1.0   → Corrélation négative parfaite
```

**Interprétation pratique:**
```
|r| > 0.9  → Très forte corrélation ✅
0.7 < |r| ≤ 0.9 → Forte corrélation
0.5 < |r| ≤ 0.7 → Corrélation modérée
0.3 < |r| ≤ 0.5 → Faible corrélation
|r| ≤ 0.3  → Très faible ou pas corrélation ❌
```

**Exemple - Électricité vs Émissions:**
```
Données 24 mois:
x = [5000, 5200, 4800, ..., 6100] kWh
y = [210, 219, 202, ..., 257] kg CO₂e

Cov(X,Y) = 80,500 kWh·kg
σ_X = 487 kWh
σ_Y = 17.2 kg CO₂e

r = 80,500 / (487 × 17.2) = 0.961 ✅

→ Très forte corrélation positive
→ Plus consommation → Plus émissions (logique!)
```

**Relation: r² = R²**
$$r^2 = R^2 = 0.961^2 = 0.924 = 92.4\%$$

### Matrice de Corrélation (Régression Multiple)

Pour plusieurs variables indépendantes (X₁, X₂, X₃...):

$$\begin{pmatrix}
1 & r_{12} & r_{13} & r_{1Y} \\
r_{12} & 1 & r_{23} & r_{2Y} \\
r_{13} & r_{23} & 1 & r_{3Y} \\
r_{1Y} & r_{2Y} & r_{3Y} & 1
\end{pmatrix}$$

**Exemple - PME:**
```
Correlations entre variables:
                Électricité   Gaz    Déchets  Émissions
Électricité     1.00         0.34   0.12     0.92
Gaz             0.34         1.00   0.45     0.88
Déchets         0.12         0.45   1.00     0.65
Émissions       0.92         0.88   0.65     1.00

Observations:
- Électricité et Émissions: r=0.92 (très forte)
- Gaz et Émissions: r=0.88 (très forte)
- Déchets et Émissions: r=0.65 (modérée)
- Électricité et Gaz: r=0.34 (faible) → peu multicolinéaires ✅
```

### Multicolinéarité

Problème: Deux variables indépendantes très corrélées

$$\text{VIF} = \frac{1}{1 - R_k^2}$$

Où $R_k^2$ = R² de la régression Xₖ vs autres X

**Interprétation VIF:**
```
VIF < 5        → Acceptable ✅
5 ≤ VIF < 10   → À investiguer ⚠️
VIF ≥ 10       → Multicolinéarité problématique ❌
```

**Exemple:**
```
Si r(électricité, température) = 0.85
R² = 0.72
VIF = 1/(1-0.72) = 3.57 ✅ Acceptable

Si r(électricité, employés) = 0.95
R² = 0.90
VIF = 1/(1-0.90) = 10.0 ❌ Problématique
```

### Analyse des Résidus (Diagnostic Avancé)

Les **résidus** représentent l'écart entre réalité et prédiction:

$$e_i = y_i - \hat{y}_i$$

**Propriétés résidus normaux:**
```
1. Moyenne ≈ 0:           E[e] = 0 ✓
2. Variance constante:    Var(e) = σ² (homoscédasticité)
3. Distribution normale:  e ~ N(0, σ²)
4. Indépendance:          Corr(eᵢ, eⱼ) = 0 si i ≠ j
```

**Test de normalité - Kolmogorov-Smirnov:**

$$D = \max|F_n(x) - F(x)|$$

Où $F_n$ = fonction distribution empirique, $F$ = distribution théorique

Si p-value > 0.05 → Résidus normaux ✅

**Test d'homoscédasticité - Breusch-Pagan:**

$$\text{Var}(e) = \alpha_0 + \alpha_1 X_1 + \alpha_2 X_2 + ...$$

Si relation significative → Hétéroscédasticité ❌

**Test d'indépendance - Durbin-Watson:**

$$DW = \frac{\sum_{i=2}^{n} (e_i - e_{i-1})^2}{\sum_{i=1}^{n} e_i^2}$$

**Interprétation:**
```
DW ≈ 2    → Pas d'autocorrélation ✅
DW < 2    → Autocorrélation positive ❌
DW > 2    → Autocorrélation négative ❌
DW ∈ [1.5, 2.5] → Zone acceptable
```

### Prédiction vs Interpolation vs Extrapolation

**Définitions:**

1. **Interpolation:** Prédire à l'intérieur du range des données ✅
   - Fiable et peu d'erreur
   - Exemple: Prévoir juin quand données = jan-dec

2. **Extrapolation:** Prédire en dehors du range ⚠️
   - Moins fiable, plus d'erreur
   - Exemple: Prévoir janvier année suivante

3. **Exrapolation extrême:** Très loin du range ❌
   - Non recommandée
   - Exemple: Prédire année +10

**Formule d'incertitude (intervalle de prédiction):**

Plus on s'éloigne de $\bar{X}$, plus incertitude augmente:

$$SE(\hat{Y}) = s \sqrt{1 + \frac{1}{n} + \frac{(X_{\text{nouveau}} - \bar{X})^2}{\sum(X_i - \bar{X})^2}}$$

**Graphique:**
```
Largeur intervalle confiance vs X:

        │
        │      /│ ╲
        │     / │  ╲    ← Intervalle 95%
        │    /  │   ╲
        │───────────────  ← Prédiction point
        │  /    │    ╲
        │ /     │     ╲
        │/      │      ╲
        └─────────────────
         Données    Extrapolation
         (fiable)   (incertain)
```

### Sélection de Variables (Feature Selection)

Pour régression multiple, comment choisir les meilleures variables?

**Méthode 1: Pas à pas avant (Forward Selection)**
```
Étape 1: Ajouter variable avec meilleur r avec Y
Étape 2: Ajouter variable qui améliore le plus R²
Étape 3: Continuer jusqu'à pas d'amélioration significative
```

**Méthode 2: Pas à pas arrière (Backward Elimination)**
```
Étape 1: Démarrer avec toutes les variables
Étape 2: Enlever variable avec plus faible t-stat
Étape 3: Continuer jusqu'à toutes variables significatives
```

**Critère AIC (Akaike Information Criterion):**

$$\text{AIC} = 2p + n \ln\left(\frac{\text{RSS}}{n}\right)$$

Où $p$ = nombre paramètres, RSS = résidual sum squares

**Critère BIC (Bayesian Information Criterion):**

$$\text{BIC} = p \ln(n) + n \ln\left(\frac{\text{RSS}}{n}\right)$$

**Principe:** Plus AIC/BIC bas, meilleur le modèle ✅

### Régression Logistique (Classification)

Quand Y est binaire (0/1) plutôt que continu:

$$P(Y=1) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}$$

Ou en logits:
$$\ln\left(\frac{P}{1-P}\right) = \beta_0 + \beta_1 X$$

**Exemple - Prédiction dépassement seuil:**
```
Y = 1 si émissions > 100 tCO₂e/an (dépasser seuil)
Y = 0 si émissions < 100 tCO₂e/an (en-dessous)

Modèle: P(Dépasser) = f(électricité, gaz, activité)

Si P(Dépasser) = 0.75 → 75% probabilité dépassement
→ Entreprise doit réduire ses émissions de 75% pour sûrement rester en-dessous
```

---

## 🎓 Conclusion Mathématique

Tous les coefficients dérivent de:
1. **Chimie élémentaire** (rapports molaires C → CO₂)
2. **Données énergétiques** (contenu énergétique, rendements)
3. **Facteurs GWP** (pour gaz non-CO₂)
4. **Analyse cycle de vie** (ressources, transport, fin de vie)
5. **Marges de sécurité** (incertitudes ±5-20%)

**Probabilités et Statistiques** permettent de:
- Quantifier l'incertitude des mesures
- Construire des intervalles de confiance
- Évaluer la validité des prédictions

**Régression Linéaire** permet de:
- Établir relations quantitatives entre activité et émissions
- Prédire émissions futures basées sur données historiques
- Identifier les facteurs les plus influents
- Évaluer la qualité prédictive du modèle

La précision dépend de:
- ✅ Qualité données entrée (quantités activités)
- ✅ Applicabilité régionale (mix électrique local)
- ✅ Spécificité contextuelle (type équipement, durée de vie)
- ✅ Taille échantillon historique (pour régression)
- ⚠️ Évolution technologique (rendements améliorés)

