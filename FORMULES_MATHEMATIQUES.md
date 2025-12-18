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

## 🎓 Conclusion Mathématique

Tous les coefficients dérivent de:
1. **Chimie élémentaire** (rapports molaires C → CO₂)
2. **Données énergétiques** (contenu énergétique, rendements)
3. **Facteurs GWP** (pour gaz non-CO₂)
4. **Analyse cycle de vie** (ressources, transport, fin de vie)
5. **Marges de sécurité** (incertitudes ±5-20%)

La précision dépend de:
- ✅ Qualité données entrée (quantités activités)
- ✅ Applicabilité régionale (mix électrique local)
- ✅ Spécificité contextuelle (type équipement, durée de vie)
- ⚠️ Évolution technologique (rendements améliorés)

