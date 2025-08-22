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
flowchart TD
    A[Inicio] --> B[/Paso 1: Ingresa el total de la compra/];
    B --> C[/Paso 2: Ingresa el valor que te pagaron/];
    C --> D[Paso 3: Calcula el cambio: lo que te pagaron - la compra];
    D --> E{Paso 4: El cambio es <br>suficiente y válido?};
    E -- Sí --> F[Paso 5: Calcula cuántos billetes de 50.000 das<br>y guarda lo que queda del cambio];
    F --> G[Paso 6: Con lo que queda, calcula cuántos billetes de 20.000 das<br>y guarda lo que queda del cambio];
    G --> H[Paso 7: Con lo que queda, calcula cuántos billetes de 10.000 das<br>y guarda lo que queda del cambio];
    H --> I[Paso 8: Con lo que queda, calcula cuántos billetes de 5.000 das<br>y guarda lo que queda del cambio];
    I --> J[Paso 9: Con lo que queda, calcula cuántos billetes de 2.000 das<br>y guarda lo que queda del cambio];
    J --> K[Paso 10: Con lo que queda, calcula cuántos billetes de 1.000 das<br>y guarda lo que queda del cambio];
    K --> L[Paso 11: Con lo que queda, calcula cuántas monedas de 500 das<br>y guarda lo que queda del cambio];
    L --> M[/Paso 12: Muestra la cantidad de cada billete y moneda/];
    M --> N[/Paso 13: Muestra el total del cambio entregado/];
    N --> O[Fin];
    E -- No --> P[/Paso 14: Muestra el mensaje de error/];
    P --> O;
```
