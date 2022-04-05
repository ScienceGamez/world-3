"""
Module land_development_loss_fertility
Translated using PySD version 2.2.0
"""


def arable_land():
    """
    Real Name: Arable Land
    Original Eqn: INTEG( land development rate - land erosion rate - land removal for urban and industrial use , initial arable land )
    Units: hectare
    Limits: (None, None)
    Type: component
    Subs: None

    Arable land (AL#85).
    """
    return _integ_arable_land()


def initial_arable_land():
    """
    Real Name: initial arable land
    Original Eqn: 9e+08
    Units: hectare
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial amount of land that is arable.                 (ALI#85.2).
    """
    return 9e08


def development_cost_per_hectare():
    """
    Real Name: development cost per hectare
    Original Eqn: development cost per hectare table ( Potentially Arable Land / potentially arable land total )
    Units: $/hectare
    Limits: (None, None)
    Type: component
    Subs: None

    Development cost per hectare (DCPH#97).
    """
    return development_cost_per_hectare_table(
        potentially_arable_land() / potentially_arable_land_total()
    )


def development_cost_per_hectare_table(x):
    """
    Real Name: development cost per hectare table
    Original Eqn: ( (0,100000),(0.1,7400),(0.2,5200),(0.3,3500),(0.4,2400),(0.5,1500) ,(0.6,750),(0.7,300),(0.8,150),(0.9,75),(1,50) )
    Units: $/hectare
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating undeveloped land to the cost of land                 development (DCPHT#97.1).
    """
    return lookup(
        x,
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [100000, 7400, 5200, 3500, 2400, 1500, 750, 300, 150, 75, 50],
    )


def land_development_rate():
    """
    Real Name: land development rate
    Original Eqn: total agricultural investment * fraction of agricultural inputs allocated to land development / development cost per hectare
    Units: hectare/year
    Limits: (None, None)
    Type: component
    Subs: None

    The land developmen rate (LDR#96).
    """
    return (
        total_agricultural_investment()
        * fraction_of_agricultural_inputs_allocated_to_land_development()
        / development_cost_per_hectare()
    )


def potentially_arable_land():
    """
    Real Name: Potentially Arable Land
    Original Eqn: INTEG( ( - land development rate ) , initial potentially arable land )
    Units: hectare
    Limits: (None, None)
    Type: component
    Subs: None

    POTENTIALLY ARABLE LAND (PAL#86).
    """
    return _integ_potentially_arable_land()


def initial_potentially_arable_land():
    """
    Real Name: initial potentially arable land
    Original Eqn: 2.3e+09
    Units: hectare
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial amount of potentially arable land                 (PALI#86.2).
    """
    return 2.3e09


def potentially_arable_land_total():
    """
    Real Name: potentially arable land total
    Original Eqn: 3.2e+09
    Units: hectare
    Limits: (None, None)
    Type: constant
    Subs: None

    POTENTIALLY ARABLE LAND TOTAL (PALT#84.1).
    """
    return 3.2e09


def land_life_multiplier_from_land_yield():
    """
    Real Name: land life multiplier from land yield
    Original Eqn: land life multiplier from land yield 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LAND LIFE MULTIPLIER FROM YIELD (LLMY#113).
    """
    return land_life_multiplier_from_land_yield_1()


def average_life_of_land():
    """
    Real Name: average life of land
    Original Eqn: average life of land normal * land life multiplier from land yield
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    Average life of land (ALL#112).
    """
    return average_life_of_land_normal() * land_life_multiplier_from_land_yield()


def average_life_of_land_normal():
    """
    Real Name: average life of land normal
    Original Eqn: 1000
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    AVERAGE LIFE OF LAND NORMAL (ALLN#112.1).
    """
    return 1000


def land_erosion_rate():
    """
    Real Name: land erosion rate
    Original Eqn: Arable Land / average life of land
    Units: hectare/year
    Limits: (None, None)
    Type: component
    Subs: None

    Land erosion rate (LER#
    """
    return arable_land() / average_life_of_land()


def land_removal_for_urban_and_industrial_use():
    """
    Real Name: land removal for urban and industrial use
    Original Eqn: MAX(0, urban and industrial land required - Urban and Industrial Land ) / urban and industrial land development time
    Units: hectare/year
    Limits: (None, None)
    Type: component
    Subs: None

    LAND REMOVAL FOR URBAN-INDUSTRIAL USE (LRUI#119).
    """
    return (
        np.maximum(
            0, urban_and_industrial_land_required() - urban_and_industrial_land()
        )
        / urban_and_industrial_land_development_time()
    )


def urban_and_industrial_land_development_time():
    """
    Real Name: urban and industrial land development time
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Urban industrial land development time                 (UILDT#119.1).
    """
    return 10


def urban_and_industrial_land_required_per_capita():
    """
    Real Name: urban and industrial land required per capita
    Original Eqn: urban and industrial land required per capita table ( industrial output per capita/GDP pc unit )
    Units: hectare/Person
    Limits: (None, None)
    Type: component
    Subs: None

    Urban industrial land per capita (UILPC#117).
    """
    return urban_and_industrial_land_required_per_capita_table(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def urban_and_industrial_land_required_per_capita_table(x):
    """
    Real Name: urban and industrial land required per capita table
    Original Eqn: ( (0,0.005),(200,0.008),(400,0.015),(600,0.025),(800,0.04),(1000,0.055) ,(1200,0.07),(1400,0.08),(1600,0.09) )
    Units: hectare/Person
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output to urban industrial                 land (UILPCT#117.1)
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [0.005, 0.008, 0.015, 0.025, 0.04, 0.055, 0.07, 0.08, 0.09],
    )


def urban_and_industrial_land_required():
    """
    Real Name: urban and industrial land required
    Original Eqn: urban and industrial land required per capita * population
    Units: hectare
    Limits: (None, None)
    Type: component
    Subs: None

    Urban industrial land required (UILR#118).
    """
    return urban_and_industrial_land_required_per_capita() * population()


def urban_and_industrial_land():
    """
    Real Name: Urban and Industrial Land
    Original Eqn: INTEG( ( land removal for urban and industrial use ) , initial urban and industrial land )
    Units: hectare
    Limits: (None, None)
    Type: component
    Subs: None

    URBAN-INDUSTRIAL LAND (UIL#120).
    """
    return _integ_urban_and_industrial_land()


def initial_urban_and_industrial_land():
    """
    Real Name: initial urban and industrial land
    Original Eqn: 8.2e+06
    Units: hectare
    Limits: (None, None)
    Type: constant
    Subs: None

    URBAN-INDUSTRIAL LAND INITIAL (UILI#120.1).
    """
    return 8.2e06


def land_fertility_degredation():
    """
    Real Name: land fertility degredation
    Original Eqn: Land Fertility * land fertility degredation rate
    Units: Veg equiv kg/(year*year*hectare)
    Limits: (None, None)
    Type: component
    Subs: None

    LAND FERTILITY DEGRADATION (LFD#123).
    """
    return land_fertility() * land_fertility_degredation_rate()


def land_fertility_degredation_rate():
    """
    Real Name: land fertility degredation rate
    Original Eqn: land fertility degredation rate table ( persistent pollution index )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    Land fertility degradation rate (LFDR#122).
    """
    return land_fertility_degredation_rate_table(persistent_pollution_index())


def land_fertility_degredation_rate_table(x):
    """
    Real Name: land fertility degredation rate table
    Original Eqn: ( (0,0),(10,0.1),(20,0.3),(30,0.5) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating persistent pollution to land                 fertility degradation (LFDRT#122.1).
    """
    return lookup(x, [0, 10, 20, 30], [0, 0.1, 0.3, 0.5])


def land_fertility():
    """
    Real Name: Land Fertility
    Original Eqn: INTEG( ( land fertility regeneration - land fertility degredation ) , initial land fertility )
    Units: Veg equiv kg/(year*hectare)
    Limits: (None, None)
    Type: component
    Subs: None

    Land fertility (LFERT#121).
    """
    return _integ_land_fertility()


def initial_land_fertility():
    """
    Real Name: initial land fertility
    Original Eqn: 600
    Units: Veg equiv kg/(year*hectare)
    Limits: (None, None)
    Type: constant
    Subs: None

    LAND FERTILITY INITIAL (LFERTI#121.2)
    """
    return 600


def inherent_land_fertility():
    """
    Real Name: inherent land fertility
    Original Eqn: 600
    Units: Veg equiv kg/(year*hectare)
    Limits: (None, None)
    Type: constant
    Subs: None

    INHERENT LAND FERTILITY (ILF#124.1).
    """
    return 600


def land_fertility_regeneration():
    """
    Real Name: land fertility regeneration
    Original Eqn: ( inherent land fertility - Land Fertility ) / land fertility regeneration time
    Units: Veg equiv kg/(year*year*hectare)
    Limits: (None, None)
    Type: component
    Subs: None

    Land fertility regeneration (LFR#124).
    """
    return (
        inherent_land_fertility() - land_fertility()
    ) / land_fertility_regeneration_time()


def land_fertility_regeneration_time():
    """
    Real Name: land fertility regeneration time
    Original Eqn: land fertility regeneration time table ( fraction of agricultural inputs for land maintenance )
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    LAND FERTILITY REGENERATION TIME (LFRT#125)
    """
    return land_fertility_regeneration_time_table(
        fraction_of_agricultural_inputs_for_land_maintenance()
    )


def land_fertility_regeneration_time_table(x):
    """
    Real Name: land fertility regeneration time table
    Original Eqn: ( (0,20),(0.02,13),(0.04,8),(0.06,4),(0.08,2),(0.1,2) )
    Units: year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating inputs to land maintenance to land                 fertility regeneration (LFRTT#125.1).
    """
    return lookup(x, [0, 0.02, 0.04, 0.06, 0.08, 0.1], [20, 13, 8, 4, 2, 2])


def fraction_of_agricultural_inputs_allocated_to_land_development():
    """
    Real Name: fraction of agricultural inputs allocated to land development
    Original Eqn: fraction of agricultural inputs allocated to land development table ( ( marginal productivity of land development / marginal productivity of agricultural inputs ) )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of inputs allocated to land devlelopment                 (FIALD#108).
    """
    return fraction_of_agricultural_inputs_allocated_to_land_development_table(
        (
            marginal_productivity_of_land_development()
            / marginal_productivity_of_agricultural_inputs()
        )
    )


def fraction_of_agricultural_inputs_allocated_to_land_development_table(x):
    """
    Real Name: fraction of agricultural inputs allocated to land development table
    Original Eqn: ( (0,0),(0.25,0.05),(0.5,0.15),(0.75,0.3),(1,0.5),(1.25,0.7) ,(1.5,0.85),(1.75,0.95),(2,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the marginal productivity of land to                the fraction of inputs allocated to new land                 development (FIALDT#108.1).
    """
    return lookup(
        x,
        [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2],
        [0, 0.05, 0.15, 0.3, 0.5, 0.7, 0.85, 0.95, 1],
    )


def marginal_productivity_of_land_development():
    """
    Real Name: marginal productivity of land development
    Original Eqn: land yield / ( development cost per hectare * social discount )
    Units: Veg equiv kg/$
    Limits: (None, None)
    Type: component
    Subs: None

    The marginal productivity of land development                 (MPLD#109)
    """
    return land_yield() / (development_cost_per_hectare() * social_discount())


def social_discount():
    """
    Real Name: social discount
    Original Eqn: 0.07
    Units: 1/year
    Limits: (None, None)
    Type: constant
    Subs: None

    SOCIAL DISCOUNT (SD#109.1)
    """
    return 0.07


_integ_arable_land = Integ(
    lambda: land_development_rate()
    - land_erosion_rate()
    - land_removal_for_urban_and_industrial_use(),
    lambda: initial_arable_land(),
    "_integ_arable_land",
)


_integ_potentially_arable_land = Integ(
    lambda: (-land_development_rate()),
    lambda: initial_potentially_arable_land(),
    "_integ_potentially_arable_land",
)


_integ_urban_and_industrial_land = Integ(
    lambda: (land_removal_for_urban_and_industrial_use()),
    lambda: initial_urban_and_industrial_land(),
    "_integ_urban_and_industrial_land",
)


_integ_land_fertility = Integ(
    lambda: (land_fertility_regeneration() - land_fertility_degredation()),
    lambda: initial_land_fertility(),
    "_integ_land_fertility",
)
