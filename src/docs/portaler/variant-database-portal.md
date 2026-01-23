---
title: NGP Variant Database Portal
---

# :cyclone: NGP Variant Database Portal
## Introduktion & Syfte
Målet med NGP Variant Database Portal är att bygga upp en databas med tolkade och otolkade varianter, samt kunna göra sökningar bland dessa. De tolkade varianterna laddas upp via portalen i form av Excel-filer. Dessa filer valideras baserad på en standardiserad mall i samband med uppladdningen. 

Mallen innefattar fält som till exempel `CHR`,`POS`, `REF`, `ALT`, `Submitter`, `Submitter org`, `Classification` och `Classification score`. `Classification` och `Classification score` syftar på klassifiering från American College of Medical Genetics (ACMG).

Innan uppladdningen jämförs varianterna i Excel-filen mot varianterna i databasen. Om användaren försöker ladda upp variant-klassifiering som inte matchar med klassifieringen som finns i databasen, så kommer den att avvisas. Till exempel, om den existerande klassifieringen av en variant är `PATOGENIC` och en användare försöker ladda upp ett resultat med samma variant fast med klassifieringen `LIKELY_BENIGN`, så kommer portalen att avvisa resultet.

Portalen avvisar en klassifering baserat på tre så kallade klassifikationsgrupper:

$$
P = \{\text{"PATHOGENIC"}, \text{"LIKELY_PATHOGENIC"}\},
$$

$$
B = \{\text{"BENIGN"}, \text{"LIKELY_BENIGN"}\},
$$

$$
U = \{\text{"UNCERTAIN"}\}
$$

Portalen avvisar en inkommande klassifiering, $k_i$, om den och existerande klassifiering $k_e$ inte ingår i samma klassifierningsgrupp. Dvs:

$$
\neg (k_i \in A \land k_e \in A) \forall A, A = \{P, B, U\}
$$
