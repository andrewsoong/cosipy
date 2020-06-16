"""
    Declaration of constants
    Do not modify unless you are absolutely sure what you are doing.
"""

' GENERAL INFORMATION ' 
dt = 3600                                       # Time step in the input files [s]
max_layers = 500                                # Max. number of layers, just for the restart file
z = 2.0                                         # Measurement height [m]

' PARAMETERIZATIONS '
stability_correction = 'Ri'                     # possibilities: 'Ri','MO'
albedo_method = 'Oerlemans98'                   # possibilities: 'Oerlemans98'
densification_method = 'Boone'                  # possibilities: 'Boone','Vionnet','empirical','constant'
penetrating_method = 'Bintanja95'               # possibilities: 'Bintanja95'
roughness_method = 'Moelg12'                    # possibilities: 'Moelg12'
saturation_water_vapour_method = 'Sonntag90'    # possibilities: 'Sonntag90'


' INITIAL CONDITIONS '
initial_snowheight_constant = 1.0               # Initial snowheight
initial_snow_layer_heights = 0.10               # Initial thickness of snow layers
initial_glacier_height = 10.0                   # Initial glacier height without snowlayers
initial_glacier_layer_heights = 0.5             # Initial thickness of glacier ice layers

initial_top_density_snowpack_constant = 300.    # Top density for initial snowpack
initial_bottom_density_snowpack_constant = 600. # Bottom density for initial snowpack

temperature_top_constant = 273.0                # Upper boundary condition for initial temperature profile (K)
temperature_bottom = 272.16                     # Lower boundary condition for initial temperature profile (K)
const_init_temp = 0.1                           # constant for init temperature profile used in exponential function (exponential decay)


' MODEL CONSTANTS '
center_snow_transfer_function = 2.5             # center (50/50) when total precipitation is transferred to snow and rain
spread_snow_transfer_function = 1               # 1: +-2.5
mult_factor_RRR = 1.0                           # multiplication factor for RRR

minimum_snow_to_reset_albedo = 0.01             # minimum snowfall to reset hours since last snowfall! Default was 0.005
minimum_snow_layer_height = 0.001               # minimum layer height


' REMESHING OPTIONS'
remesh_method = 'log_profile'                   # Remeshing (log_profile or adaptive_profile)
first_layer_height = 0.01                       # The first layer will always have the defined height (m)
layer_stretching = 1.20                         # Stretching factor used by the log_profile method (e.g. 1.1 mean the subsequent layer is 10% greater than the previous

merge_max = 1                                   # How many mergings are allowed per time step
density_threshold_merging = 5                   # If merging is true threshold for layer densities difference two layer try: 5-10 (kg m^-3)
temperature_threshold_merging = 0.01            # If mering is true threshold for layer temperatures to merge  try: 0.05-0.1 (K)


' PHYSICAL CONSTANTS '
constant_density = 300.                        # constant density of freshly fallen snow [kg m-3], if densification_method is set to 'constant'

albedo_fresh_snow = 0.9                         # albedo of fresh snow [-] (Moelg et al. 2012, TC)
albedo_firn = 0.6                               # albedo of firn [-] (Moelg et al. 2012, TC)
albedo_ice = 0.3                                # albedo of ice [-] (Moelg et al. 2012, TC)
albedo_mod_snow_aging = 20.0                    # effect of ageing on snow albedo [days] (Moelg et al. 2012, TC)
albedo_mod_snow_depth = 1.0                     # effect of snow depth on albedo [cm] (Moelg et al. 2012, TC)

roughness_fresh_snow = 0.24                     # surface roughness length for fresh snow [mm] (Moelg et al. 2012, TC)
roughness_ice = 1.7                             # surface roughness length for ice [mm] (Moelg et al. 2012, TC)
roughness_firn = 4.0                            # surface roughness length for aged snow [mm] (Moelg et al. 2012, TC)
aging_factor_roughness = 0.0026                 # effect of ageing on roughness lenght (hours) 60 days from 0.24 to 4.0 => 0.0026

snow_ice_threshold = 900.0                      # pore close of density [kg m^(-3)]
snow_firn_threshold = 555.0                     #

lat_heat_melting = 3.34e5                       # latent heat for melting [J kg-1]
lat_heat_vaporize = 2.5e6                       # latent heat for vaporization [J kg-1]
lat_heat_sublimation = 2.834e6                  # latent heat for sublimation [J kg-1]

spec_heat_air = 1004.67                         # specific heat of air [J kg-1 K-1]
spec_heat_ice = 2050.00                         # specific heat of ice [J Kg-1 K-1]
spec_heat_water = 4217.00                       # specific heat of water [J Kg-1 K-1]

#k_i = 2.25                                      # thermal conductivity ice [W m^-1 K^-1]
#k_w = 0.6089                                    # thermal conductivity water [W m^-1 K^-1]
#k_a = 0.026                                     # thermal conductivity air [W m^-1 K^-1]
k_i = 2.22                                      # thermal conductivity ice [W m^-1 K^-1]
k_w = 0.55                                    # thermal conductivity water [W m^-1 K^-1]
k_a = 0.024                                     # thermal conductivity air [W m^-1 K^-1]

water_density = 1000.0                          # density of water [kg m^(-3)]
ice_density = 917.                              # density of ice [kg m^(-3)]
air_density = 1.1                               # density of air [kg m^(-3)]

sigma = 5.67e-8                                 # Stefan-Bolzmann constant [W m-2 K-4]
zero_temperature = 273.16                       # Melting temperature [K]
surface_emission_coeff = 0.99                   # surface emission coefficient [-]
