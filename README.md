# Taumutu #
#### Author: Mitchell Anderson ####

 ### Risk Assessment for the Taumutu community


This repository contains 3 scripts and the elevation profile data used to create the figure at Urutau.co.nz/Taumutu.html

## Scripts
  1. src/slr_model.py
    - This creates a rate of sea level rise based on IPCC predictions for 2090.
  2. src/plot_profiles.py
    - This takes input values for sea level rise and tides to give a scenario graph
  3. src/slr_gif.py
    - Takes the SLR model and creates a dynamic image (gif) for the rising sea level relative to the current ground profile
    
## Data
  1. data/bank_profile.csv
    - CSV file of elevations for approx 1km of coastline (Can be used to assess potential entry points for inundation)
  2. data/church_profile.csv
    - CSV file of elevation from the church to the coast
  2. data/marae_profile.csv
    - CSV file of elevation from the marae to the coast
