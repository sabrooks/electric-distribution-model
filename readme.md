# Distribution Model

Distribution Model is a library to build an electric utility distribution model (Digital Twin) from an ESRI database.  Elements are connected based on element type and location. This library supports engineering analysis of a distribution utility. 

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


## Postgres SQL Data Loading

Elements are loaded from the PostGIS database.  The SQL query is stored in the element file.

## Analysis Supported
1. Transformer Loading
2. Conductor peak load 
3. Phase balancing

## Future Development
Migrate to ESRI Utility Newtork has two main benefits:
1. Standardizes data model between utilties.
2. Provides more robust / stable connection logic than element type and location.