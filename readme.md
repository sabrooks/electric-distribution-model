# Distribution Model

Distribution Model is a library to build a distribution model.  Elements are connected based on element type and location.  

## Elements

1. Generic Elements
    1. Point
        1. Transformers
        2. Protection (Circuit Switchers, Reclosers, Swithces, Bkrs)
        3. Fuses
        3. Services
            1. Light

    2. Line Elements
        1. Primary
            1. Busbar
        2. Secondary


## Postgres SQL Load

Elements are loaded from the PostGIS database.  The SQL query is stored in the element file.

## Uses
1. Transformer Loading
2. Conductor peak load 
3. Phase balancing
