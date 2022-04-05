"""
Module welfare__footprint
Translated using PySD version 2.2.0
"""


def absorption_land_gha():
    """
    Real Name: "Absorption Land (GHA)"
    Original Eqn: persistent pollution generation rate*ha per unit of pollution/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        persistent_pollution_generation_rate()
        * ha_per_unit_of_pollution()
        / ha_per_gha()
    )


def arable_land_in_gigahectares_gha():
    """
    Real Name: "Arable Land in Gigahectares (GHA)"
    Original Eqn: Arable Land/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return arable_land() / ha_per_gha()


def education_index():
    """
    Real Name: Education Index
    Original Eqn: Education Index LOOKUP(GDP per capita/GDP pc unit)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return education_index_lookup(gdp_per_capita() / gdp_pc_unit())


def education_index_lookup(x):
    """
    Real Name: Education Index LOOKUP
    Original Eqn: ((0,0),(1000,0.81),(2000,0.88),(3000,0.92),(4000,0.95),(5000,0.98),(6000,0.99),(7000,1))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return lookup(
        x,
        [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
        [0, 0.81, 0.88, 0.92, 0.95, 0.98, 0.99, 1],
    )


def gdp_index():
    """
    Real Name: GDP Index
    Original Eqn: LOG(GDP per capita/Ref Lo GDP,10)/LOG(Ref Hi GDP/Ref Lo GDP,10)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return log(gdp_per_capita() / ref_lo_gdp(), 10) / log(
        ref_hi_gdp() / ref_lo_gdp(), 10
    )


def gdp_per_capita():
    """
    Real Name: GDP per capita
    Original Eqn: GDP per capita LOOKUP(industrial output per capita/GDP pc unit)
    Units: $/(year*Person)
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return gdp_per_capita_lookup(industrial_output_per_capita() / gdp_pc_unit())


def gdp_per_capita_lookup(x):
    """
    Real Name: GDP per capita LOOKUP
    Original Eqn: ((0,120),(200,600),(400,1200),(600,1800),(800,2500),(1000,3200))
    Units: $/(year*Person)
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return lookup(x, [0, 200, 400, 600, 800, 1000], [120, 600, 1200, 1800, 2500, 3200])


def ha_per_gha():
    """
    Real Name: ha per Gha
    Original Eqn: 1e+09
    Units: hectare/Ghectare
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1e09


def ha_per_unit_of_pollution():
    """
    Real Name: ha per unit of pollution
    Original Eqn: 4
    Units: hectares/(Pollution units/year)
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 4


def human_ecological_footprint():
    """
    Real Name: Human Ecological Footprint
    Original Eqn: ("Arable Land in Gigahectares (GHA)"+"Urban Land (GHA)"+"Absorption Land (GHA)" )/Total Land
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    See Appendix 2 of Limits to Growth - the 30-Year Update for discussion of
        this index
    """
    return (
        arable_land_in_gigahectares_gha() + urban_land_gha() + absorption_land_gha()
    ) / total_land()


def human_welfare_index():
    """
    Real Name: Human Welfare Index
    Original Eqn: (Life Expectancy Index+Education Index+GDP Index)/3
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    See Appendix 2 of Limits to Growth - the 30-Year Update for discussion of
        this index
    """
    return (life_expectancy_index() + education_index() + gdp_index()) / 3


def life_expectancy_index():
    """
    Real Name: Life Expectancy Index
    Original Eqn: Life Expectancy Index LOOKUP(life expectancy/one year)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return life_expectancy_index_lookup(life_expectancy() / one_year())


def life_expectancy_index_lookup(x):
    """
    Real Name: Life Expectancy Index LOOKUP
    Original Eqn: ((25,0),(35,0.16),(45,0.33),(55,0.5),(65,0.67),(75,0.84),(85,1))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return lookup(x, [25, 35, 45, 55, 65, 75, 85], [0, 0.16, 0.33, 0.5, 0.67, 0.84, 1])


def ref_hi_gdp():
    """
    Real Name: Ref Hi GDP
    Original Eqn: 9508
    Units: $/(year*Person)
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 9508


def ref_lo_gdp():
    """
    Real Name: Ref Lo GDP
    Original Eqn: 24
    Units: $/(year*Person)
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 24


def total_land():
    """
    Real Name: Total Land
    Original Eqn: 1.91
    Units: Ghectares
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1.91


def urban_land_gha():
    """
    Real Name: "Urban Land (GHA)"
    Original Eqn: Urban and Industrial Land/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return urban_and_industrial_land() / ha_per_gha()
