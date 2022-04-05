"""
Module life_expectancy
Translated using PySD version 2.2.0
"""


def crowding_multiplier_from_industry():
    """
    Real Name: crowding multiplier from industry
    Original Eqn: crowding multiplier from industry table ( industrial output per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    CROWDING MULTIPLIER FROM INDUSTRIALIZATION (CMI#27).
    """
    return crowding_multiplier_from_industry_table(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def crowding_multiplier_from_industry_table(x):
    """
    Real Name: crowding multiplier from industry table
    Original Eqn: ( (0,0.5),(200,0.05),(400,-0.1),(600,-0.08),(800,-0.02),(1000,0.05) ,(1200,0.1),(1400,0.15),(1600,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output to crowding                 (CMIT#27.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [0.5, 0.05, -0.1, -0.08, -0.02, 0.05, 0.1, 0.15, 0.2],
    )


def effective_health_services_per_capita():
    """
    Real Name: effective health services per capita
    Original Eqn: SMOOTH ( health services per capita , health services impact delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Effective health services per capita - delayed from                 allocation (EHSPC#22)
    """
    return _smooth_effective_health_services_per_capita()


def fraction_of_population_urban():
    """
    Real Name: fraction of population urban
    Original Eqn: fraction of population urban table ( population/unit population )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF POPULATION URBAN (FPU#26).
    """
    return fraction_of_population_urban_table(population() / unit_population())


def fraction_of_population_urban_table(x):
    """
    Real Name: fraction of population urban table
    Original Eqn: ( (0,0),(2e+09,0.2),(4e+09,0.4),(6e+09,0.5),(8e+09,0.58) ,(1e+10,0.65),(1.2e+10,0.72),(1.4e+10,0.78),(1.6e+10,0.8) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating population to the fraction of                 population that is urban (FPUT#26.1).
    """
    return lookup(
        x,
        [0, 2e09, 4e09, 6e09, 8e09, 1e10, 1.2e10, 1.4e10, 1.6e10],
        [0, 0.2, 0.4, 0.5, 0.58, 0.65, 0.72, 0.78, 0.8],
    )


def health_services_per_capita():
    """
    Real Name: health services per capita
    Original Eqn: health services per capita table ( service output per capita/GDP pc unit )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Health services allocation per capita (HSAPC#21).
    """
    return health_services_per_capita_table(service_output_per_capita() / gdp_pc_unit())


def health_services_per_capita_table(x):
    """
    Real Name: health services per capita table
    Original Eqn: ( (0,0),(250,20),(500,50),(750,95),(1000,140),(1250,175),(1500,200) ,(1750,220),(2000,230) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating service output to health services                 (HSAPCT#21.1).
    """
    return lookup(
        x,
        [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000],
        [0, 20, 50, 95, 140, 175, 200, 220, 230],
    )


def health_services_impact_delay():
    """
    Real Name: health services impact delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The delay between allocating health services, and                 realizing the benefit (HSID#22.1).
    """
    return 20


def life_expectancy_normal():
    """
    Real Name: life expectancy normal
    Original Eqn: 28
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The normal life expectancy with subsistance food, no                 medical care and no industrialization (LEN#19.1)
    """
    return 28


def life_expectancy():
    """
    Real Name: life expectancy
    Original Eqn: life expectancy normal * lifetime multiplier from food * lifetime multiplier from health services * lifetime multiplier from persistent pollution * lifetime multiplier from crowding
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    The average life expectancy (LE#19).
    """
    return (
        life_expectancy_normal()
        * lifetime_multiplier_from_food()
        * lifetime_multiplier_from_health_services()
        * lifetime_multiplier_from_persistent_pollution()
        * lifetime_multiplier_from_crowding()
    )


def lifetime_multiplier_from_crowding():
    """
    Real Name: lifetime multiplier from crowding
    Original Eqn: 1 - ( crowding multiplier from industry * fraction of population urban )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LIFETIME MULTIPLIER FROM CROWDING (LMC#28)
    """
    return 1 - (crowding_multiplier_from_industry() * fraction_of_population_urban())


def lifetime_multiplier_from_food():
    """
    Real Name: lifetime multiplier from food
    Original Eqn: lifetime multiplier from food table ( food per capita / subsistence food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    The life expectancy multiplier from food (LMF#20)
    """
    return lifetime_multiplier_from_food_table(
        food_per_capita() / subsistence_food_per_capita()
    )


def lifetime_multiplier_from_food_table(x):
    """
    Real Name: lifetime multiplier from food table
    Original Eqn: ( (0,0),(1,1),(2,1.43),(3,1.5),(4,1.5),(5,1.5) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table ralating relative food to the life                 expectancy multiplier for food (LMFT#20.1)
    """
    return lookup(x, [0, 1, 2, 3, 4, 5], [0, 1, 1.43, 1.5, 1.5, 1.5])


def lifetime_multiplier_from_health_services():
    """
    Real Name: lifetime multiplier from health services
    Original Eqn: IF THEN ELSE ( Time > 1940, lifetime multiplier from health services 2 , lifetime multiplier from health services 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    The life expectancy multiplier from health services                 (LMHS#23).
    """
    return if_then_else(
        time() > 1940,
        lambda: lifetime_multiplier_from_health_services_2(),
        lambda: lifetime_multiplier_from_health_services_1(),
    )


def lifetime_multiplier_from_health_services_1():
    """
    Real Name: lifetime multiplier from health services 1
    Original Eqn: lifetime multiplier from health services 1 table ( effective health services per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    The life expectancy multiplier from health services                 before 1940 (LMHS1#24).
    """
    return lifetime_multiplier_from_health_services_1_table(
        effective_health_services_per_capita() / gdp_pc_unit()
    )


def lifetime_multiplier_from_health_services_1_table(x):
    """
    Real Name: lifetime multiplier from health services 1 table
    Original Eqn: ( (0,1),(20,1.1),(40,1.4),(60,1.6),(80,1.7),(100,1.8) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating effective health care to life                 expectancy (LMHS1T#24.1).
    """
    return lookup(x, [0, 20, 40, 60, 80, 100], [1, 1.1, 1.4, 1.6, 1.7, 1.8])


def lifetime_multiplier_from_health_services_2():
    """
    Real Name: lifetime multiplier from health services 2
    Original Eqn: lifetime multiplier from health services 2 table ( effective health services per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    The life expectancy multipier from health services                 value after 1940 (LMHS2#25).
    """
    return lifetime_multiplier_from_health_services_2_table(
        effective_health_services_per_capita() / gdp_pc_unit()
    )


def lifetime_multiplier_from_health_services_2_table(x):
    """
    Real Name: lifetime multiplier from health services 2 table
    Original Eqn: ( (0,1),(20,1.5),(40,1.9),(60,2),(80,2),(100,2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating effective health care to life                 expectancy (LMHS2T#25.1)
    """
    return lookup(x, [0, 20, 40, 60, 80, 100], [1, 1.5, 1.9, 2, 2, 2])


def lifetime_multiplier_from_persistent_pollution():
    """
    Real Name: lifetime multiplier from persistent pollution
    Original Eqn: lifetime multiplier from persistent pollution table ( persistent pollution index)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LIFETIME MULTIPLIER FROM PERSISTENT POLLUTION                 (LMP#29)
    """
    return lifetime_multiplier_from_persistent_pollution_table(
        persistent_pollution_index()
    )


def lifetime_multiplier_from_persistent_pollution_table(x):
    """
    Real Name: lifetime multiplier from persistent pollution table
    Original Eqn: ( (0,1),(10,0.99),(20,0.97),(30,0.95),(40,0.9),(50,0.85),(60,0.75) ,(70,0.65),(80,0.55),(90,0.4),(100,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating persistent pollution to life                 expectancy (LMPT#29.1)
    """
    return lookup(
        x,
        [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        [1, 0.99, 0.97, 0.95, 0.9, 0.85, 0.75, 0.65, 0.55, 0.4, 0.2],
    )


_smooth_effective_health_services_per_capita = Smooth(
    lambda: health_services_per_capita(),
    lambda: health_services_impact_delay(),
    lambda: health_services_per_capita(),
    lambda: 1,
    "_smooth_effective_health_services_per_capita",
)
