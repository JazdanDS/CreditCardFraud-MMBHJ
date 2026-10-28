# Credit Card Fraud Detection

Det här är ett grupprojekt inom Data Science där vi har undersökt hur maskininlärning kan användas för att upptäcka bedrägliga kreditkortstransaktioner.

Målet med projektet var att jämföra flera modeller och undersöka vilken metod som fungerade bäst på vårt dataset, med fokus på att hitta så många bedrägerier som möjligt utan att samtidigt skapa för många falska larm.

Projektet är avgränsat till analys och modellutvärdering på ett historiskt dataset och är inte ett färdigt system för produktion.

## Gruppmedlemmar och målgrupp

**Grupp MMBHJ:** Marcus Bäckström, Martin Westberg, Ben Rinius, Henrik Andersson och Jazdan Tabrizi.

Projektets tänkta målgrupp är utredare inom banker och kreditinstitut. Modellen skulle kunna användas som beslutsstöd för att identifiera transaktioner som bör granskas vidare.

## Arbetssätt och projektplanering

Gruppen använde Microsoft Teams som gemensamt verktyg för kommunikation, planering och löpande avstämningar. Där fördelades arbetsuppgifter, beslut diskuterades och projektets nästa steg följdes upp.

Kodarbete genomfördes i separata Git-branches och ändringar granskades och fördes in i huvudversionen genom pull requests på GitHub.

## Dataset

Vi använde datasetet **Credit Card Fraud Detection** från Kaggle.

Datasetet innehåller 284 807 kreditkortstransaktioner från europeiska kortinnehavare under två dagar i september 2013.

Av transaktionerna är:

- 284 315 normala transaktioner
- 492 bedrägerier

Det betyder att endast cirka 0,17 % av transaktionerna är bedrägerier. Datasetet är därför väldigt obalanserat.

Kolumnerna V1–V28 är anonymiserade och transformerade med PCA. Det finns även kolumnerna `Time`, `Amount` och `Class`.

`Class` används som målvariabel:

- 0 = normal transaktion
- 1 = bedrägeri

Datasetet har samlats in och analyserats inom ett forskningssamarbete mellan Worldline och Machine Learning Group vid Université Libre de Bruxelles (ULB).

Datasetet hämtades från Kaggle under projektperioden hösten 2026.

Datasetet finns inte med i GitHub-repot utan behöver laddas ner separat från Kaggle och läggas i:

`data/creditcard.csv`

Dataset:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Licens

Kaggle anger licensen som:

- Database: Open Database
- Contents: Database Contents

Databasen omfattas av Open Database License (ODbL) och innehållet av Database Contents License (DbCL).

Mer information:  
https://opendatacommons.org/licenses/dbcl/1-0/

## Modeller och metoder

Projektet har bland annat bestått av:

- EDA för att undersöka datasetet
- Logistic Regression som baseline
- Random Forest
- HistGradientBoosting
- tester med class weight
- SMOTE för att hantera klassobalansen
- jämförelse mellan modellerna
- threshold-optimering
- felanalys av modellerna

Logistic Regression användes som en enkel baseline som de andra modellerna kunde jämföras med.

Eftersom datasetet innehåller väldigt få bedrägerier testade vi även SMOTE. SMOTE användes endast på träningsdatan för att inte påverka validation- eller testdatan.

## Train, validation och test

Datasetet delades upp i:

- 70 % träningsdata
- 15 % validation-data
- 15 % testdata

Vi använde stratifiering så att andelen bedrägerier blev ungefär lika i de olika delarna.

Träningsdatan användes för att träna modellerna.

Validation-datan användes för att jämföra modeller och välja threshold.

Testdatan hölls utanför modellvalet och användes först i slutet för att utvärdera den valda modellen.

## Utvärdering

Eftersom nästan alla transaktioner i datasetet är normala är accuracy inte det viktigaste måttet i det här projektet.

Vi har istället tittat på:

- Precision
- Recall
- F1-score
- PR-AUC
- Confusion matrix

Precision visar hur ofta modellen har rätt när den säger att en transaktion är ett bedrägeri.

Recall visar hur stor del av alla verkliga bedrägerier som modellen lyckas hitta.

Vi jämförde också modellerna vid ungefär samma antal false positives för att få en mer rättvis jämförelse.

## Resultat

Utifrån vår jämförelse på validation-datan valdes **Random Forest med SMOTE** som slutmodell.

Den slutliga konfigurationen använde SMOTE med `sampling_strategy=0.02`, `k_neighbors=1` och `threshold=0.40`. Random Forest-modellen använde 100 träd och `random_state=42`.

Random Forest med SMOTE gav bäst resultat av de modeller vi testade när vi jämförde hur många bedrägerier modellerna kunde hitta samtidigt som antalet falska larm hölls nere.

Den valda modellen utvärderades sedan på den tidigare orörda testdatan.

På testdatan fick modellen:

- Precision: 0,913
- Recall: 0,851
- F1-score: 0,881
- PR-AUC: 0,833

Random Forest med SMOTE hittade 63 av 74 bedrägliga transaktioner i testdatan och missade 11.

Den gav samtidigt 6 false positives, alltså normala transaktioner som felaktigt klassificerades som bedrägerier.

Som jämförelse hittade Logistic Regression 49 av 74 bedrägerier, missade 25 och gav 8 false positives.

I vårt test gav Random Forest med SMOTE därför en bättre balans mellan att hitta bedrägerier och att hålla nere antalet falska larm.

## Projektstruktur

```text
CreditCardFraud-MMBHJ/
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── baseline_model.joblib
│   └── baseline_scaler.joblib
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── baseline_logistic_regression.ipynb
│   ├── flermodeller.ipynb
│   ├── marcus_smote.ipynb
│   ├── ben_smote.ipynb
│   └── results.ipynb
│
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── io_utils.py
│   ├── schemas.py
│   └── smote.py
│
├── .gitignore
├── pyproject.toml
└── README.md
```

## Installation

Projektet använder Python 3.13 eller senare.

Klona först repositoryt:

```bash
git clone https://github.com/JazdanDS/CreditCardFraud-MMBHJ.git
cd CreditCardFraud-MMBHJ
```

Skapa sedan en virtuell Python-miljö:

```bash
python -m venv .venv
```

Aktivera miljön i Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

På macOS eller Linux:

```bash
source .venv/bin/activate
```

Installera sedan projektets beroenden:

```bash
python -m pip install --upgrade pip
pip install -e .
```

Beroenden finns definierade i `pyproject.toml` och omfattar bland annat:

- pandas
- numpy
- scikit-learn
- matplotlib
- joblib
- imbalanced-learn
- Jupyter

## Hämta data

Datasetet `creditcard.csv` behöver laddas ner från Kaggle:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Skapa vid behov mappen `data` i projektets rot och lägg filen där:

```text
data/creditcard.csv
```

CSV-filen versionshanteras inte i GitHub-repot.

## Köra projektet

Starta Jupyter från projektets rotmapp:

```bash
jupyter notebook
```

Analysen och modelleringen finns i mappen `notebooks`.

Notebookarna innehåller olika delar av projektet:

1. `EDA.ipynb` – undersökning av datasetet
2. `baseline_logistic_regression.ipynb` – Logistic Regression-baseline
3. `flermodeller.ipynb` – jämförelse av flera modeller
4. `marcus_smote.ipynb` och `ben_smote.ipynb` – experiment med SMOTE och modellinställningar
5. `results.ipynb` – slutlig modell och utvärdering på testdatan

För att återskapa den slutliga utvärderingen öppnar du `notebooks/results.ipynb` och kör cellerna uppifrån och ned.

## Begränsningar

Datasetet innehåller endast transaktioner från två dagar under 2013. Resultaten kan därför inte automatiskt antas fungera lika bra på ny eller modern kreditkortsdata.

Testdatan innehåller endast 74 bedrägliga transaktioner. Ett ganska litet antal observationer kan därför påverka resultaten mycket.

Vi använde en stratifierad slumpmässig uppdelning av datan. Ett annat alternativ hade varit att dela datan efter tid, vilket bättre hade kunnat efterlikna ett verkligt scenario där modellen tränas på äldre transaktioner och sedan används på framtida transaktioner.

V1–V28 är anonymiserade och PCA-transformerade, vilket gör det svårt att tolka exakt vad dessa variabler representerar i verkligheten.

Den threshold och det antal false positives som användes i jämförelsen är anpassade till vårt experiment och är inte baserade på en verklig banks kostnader eller utredningskapacitet.

Modellen bör därför inte användas direkt i en verklig verksamhet utan ytterligare validering på nyare och mer representativ data.

## Slutsats

I vår jämförelse valdes Random Forest med SMOTE som slutmodell.

På testdatan hittade modellen fler bedrägerier än Logistic Regression samtidigt som den gav färre falska larm.

Resultaten gäller däremot endast för det dataset och den uppdelning vi har använt. Mer testning på ny data skulle behövas innan en sådan modell skulle kunna användas i verkligheten.

## Användning av generativ AI

I enlighet med kursens anvisningar har Claude, ChatGPT, Copilot och Gemini använts som stöd för att utmana egna resonemang, förstå felmeddelanden, diskutera idéer och granska struktur och resultat, bland annat kring SMOTE.

Generativ AI har använts som stöd och inte för att ersätta gruppens eget arbete. All kod och alla resultat som använts i projektet har testats, kontrollerats och förståtts av gruppen.