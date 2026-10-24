# Credit Card Fraud Detection

Det här är ett grupprojekt inom Data Science där vi undersöker hur maskininlärning kan användas för att upptäcka bedrägliga kreditkortstransaktioner.

Vi har testat flera olika modeller och jämfört resultaten för att se vilken modell som fungerar bäst på datasetet.

## Dataset

Vi använder datasetet **Credit Card Fraud Detection** från Kaggle.

Datasetet innehåller 284 807 kreditkortstransaktioner från europeiska kortinnehavare under två dagar i september 2013.

Av transaktionerna är:

- 284 315 normala transaktioner
- 492 bedrägerier

Det betyder att endast cirka 0,17 % av transaktionerna är bedrägerier. Datasetet är därför väldigt obalanserat.

Kolumnerna V1-V28 är anonymiserade och transformerade med PCA. Det finns även kolumnerna Time, Amount och Class.

Class används som målvariabel:

- 0 = normal transaktion
- 1 = bedrägeri

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

## Vad vi har gjort

Projektet har bland annat bestått av:

- EDA för att undersöka datasetet
- Logistic Regression som baseline
- Random Forest
- HistGradientBoosting
- tester med class weight
- SMOTE för att hantera klassobalansen
- jämförelse mellan modellerna
- felanalys av den valda modellen

Logistic Regression användes som en enkel baseline som de andra modellerna kunde jämföras med.

Eftersom datasetet innehåller väldigt få bedrägerier testade vi även SMOTE. SMOTE användes bara på träningsdatan för att inte påverka validation- eller testdatan.

## Train, validation och test

Datasetet delades upp i:

- 70 % träningsdata
- 15 % validation-data
- 15 % testdata

Vi använde stratifiering så att andelen bedrägerier blev ungefär lika i de olika delarna.

Träningsdatan användes för att träna modellerna.

Validation-datan användes för att jämföra modeller och välja threshold.

Testdatan hölls utanför modellvalet och användes sedan i slutet för att utvärdera den valda modellen.

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

Random Forest med SMOTE gav bäst resultat av de modeller vi testade när vi jämförde hur många bedrägerier modellerna kunde hitta samtidigt som antalet falska larm hölls nere.

Den valda modellen utvärderades sedan på testdatan.

På testdatan fick modellen:

- Precision: 0,913
- Recall: 0,851
- F1-score: 0,881
- PR-AUC: 0,833

Random Forest med SMOTE hittade 63 av 74 bedrägliga transaktioner i testdatan och missade 11.

Den gav samtidigt 6 false positives, alltså normala transaktioner som felaktigt klassificerades som bedrägerier.

Som jämförelse hittade Logistic Regression 49 av 74 bedrägerier och missade 25.

I vårt test gav Random Forest med SMOTE därför en bättre balans mellan att hitta bedrägerier och att hålla nere antalet falska larm.

## Projektstruktur

```text
CreditCardFraud-MMBHJ/
│
├── data/
│   └── creditcard.csv
│
├── models/
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
│   ├── io_utils.py
│   ├── schemas.py
│   ├── smote.py
│   ├── process.py
│   └── transform.py
│
├── pyproject.toml
└── README.md
```

## Köra projektet

Projektet använder Python 3.13 eller senare.

Klona först repositoryt och skapa en virtuell Python-miljö.

Datasetet `creditcard.csv` behöver sedan laddas ner från Kaggle och läggas i mappen `data`.

Analysen och modelleringen finns i notebookarna i mappen `notebooks`.

Python-paket som används i projektet är bland annat:

- pandas
- scikit-learn
- matplotlib
- joblib
- imbalanced-learn
- Jupyter

## Begränsningar

Datasetet innehåller endast transaktioner från två dagar under 2013. Resultaten kan därför inte automatiskt antas fungera lika bra på ny eller modern kreditkortsdata.

Testdatan innehåller också bara 74 bedrägliga transaktioner. Ett ganska litet antal observationer kan därför påverka resultaten mycket.

Vi använde en stratifierad slumpmässig uppdelning av datan. Ett annat alternativ hade varit att dela datan efter tid, vilket hade kunnat likna ett verkligt scenario bättre där modellen tränas på äldre transaktioner och sedan används på framtida transaktioner.

V1-V28 är anonymiserade vilket också gör det svårare att tolka exakt vad dessa variabler representerar.

## Slutsats

I vår jämförelse valdes Random Forest med SMOTE som slutmodell.

På testdatan hittade modellen fler bedrägerier än Logistic Regression samtidigt som den hade få falska larm.

Resultaten gäller däremot bara för det dataset och den uppdelning vi har använt. Mer testning på ny data skulle behövas innan en sådan modell skulle kunna användas i verkligheten.