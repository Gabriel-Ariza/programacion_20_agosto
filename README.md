# programacion_20_agosto

```mermaid
graph TD
    A[Inicio] --> B["Llamar función calcular IMC"]

    B --> C["Solicitar peso y altura"]
    C --> D["Calcular IMC"]
    D --> E{"Si IMC < 18.5?"}
    E -- Sí --> F["Mostrar bajo peso"]
    E -- No --> G{"Si IMC >= 18.5 y < 25?"}
    G -- Sí --> H["Mostrar peso normal"]
    G -- No --> I{"Si IMC >= 25 y < 30?"}
    I -- Sí --> J["Mostrar sobrepeso"]
    I -- No --> K["Mostrar obeso"]

    F --> L
    H --> L
    J --> L
    K --> L["Mostrar IMC y preguntar: "]

    L --> M["Desea hacer otra consulta"]
    M -- "1. Sí" --> B
    M -- "2. No" --> N["Mostrar Gracias y terminar"]
```


```mermaid
graph TD
    A[Inicio] --> B(Ingresar total_compra y valor_pagado);
    B --> C{Calcular cambio};
    C --> D{Es el cambio >= 0 y múltiplo de 500?};
    D -- Sí --> E[Calcular cantidad de billetes y monedas];
    E --> F[Mostrar desglose del cambio];
    F --> G[Mostrar total de la devuelta];
    D -- No --> H[Mostrar mensaje de error];
    G --> I[Fin];
    H --> I;
