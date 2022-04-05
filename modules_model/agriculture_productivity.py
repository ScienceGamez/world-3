"""
Module agriculture_productivity
Translated using PySD version 2.2.0
"""


def land_yield_multiplier_from_air_pollution():
    """
    Real Name: land yield multiplier from air pollution
    Original Eqn: land yield multipler from air pollution 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land yield multiplier from air pollution                 (LYMAP#105).
    """
    return land_yield_multipler_from_air_pollution_1()


def land_yield_multiplier_from_technology():
    """
    Real Name: land yield multiplier from technology
    Original Eqn: land yield factor 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land Yield factor (LYF#104)
    """
    return land_yield_factor_1()


def land_yield_technology_change_rate():
    """
    Real Name: land yield technology change rate
    Original Eqn: 0
    Units: 1/year
    Limits: (None, None)
    Type: constant
    Subs: None

    Land yield from technology change rate (LYTDR#--)
    """
    return 0


def desired_food_ratio():
    """
    Real Name: desired food ratio
    Original Eqn: 2
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    desired food ratio (DFR#--)
    """
    return 2


def ind_out_in_1970():
    """
    Real Name: IND OUT IN 1970
    Original Eqn: 7.9e+11
    Units: $/year
    Limits: (None, None)
    Type: constant
    Subs: None

    INDUSTRIAL OUTPUT IN 1970 (IO70#107.2)
    """
    return 7.9e11


def land_yield():
    """
    Real Name: land yield
    Original Eqn: land yield multiplier from technology * Land Fertility * land yield multiplier from capital * land yield multiplier from air pollution
    Units: Veg equiv kg/(year*hectare)
    Limits: (None, None)
    Type: component
    Subs: None

    LAND YIELD (LY#103)
    """
    return (
        land_yield_multiplier_from_technology()
        * land_fertility()
        * land_yield_multiplier_from_capital()
        * land_yield_multiplier_from_air_pollution()
    )


def land_yield_multiplier_from_capital():
    """
    Real Name: land yield multiplier from capital
    Original Eqn: land yield multiplier from capital table ( agricultural input per hectare/unit agricultural input )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LAND YIELD MULTIPLIER FROM CAPITAL (LYMC#102)
    """
    return land_yield_multiplier_from_capital_table(
        agricultural_input_per_hectare() / unit_agricultural_input()
    )


def land_yield_multiplier_from_capital_table(x):
    """
    Real Name: land yield multiplier from capital table
    Original Eqn: ( (0,1),(40,3),(80,4.5),(120,5),(160,5.3),(200,5.6),(240,5.9) ,(280,6.1),(320,6.35),(360,6.6),(400,6.9),(440,7.2),(480,7.4) ,(520,7.6),(560,7.8),(600,8),(640,8.2),(680,8.4),(720,8.6) ,(760,8.8),(800,9),(840,9.2),(880,9.4),(920,9.6),(960,9.8) ,(1000,10) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating agricultural inputs to land yeild                 (LYMCT#102.1).
    """
    return lookup(
        x,
        [
            0,
            40,
            80,
            120,
            160,
            200,
            240,
            280,
            320,
            360,
            400,
            440,
            480,
            520,
            560,
            600,
            640,
            680,
            720,
            760,
            800,
            840,
            880,
            920,
            960,
            1000,
        ],
        [
            1,
            3,
            4.5,
            5,
            5.3,
            5.6,
            5.9,
            6.1,
            6.35,
            6.6,
            6.9,
            7.2,
            7.4,
            7.6,
            7.8,
            8,
            8.2,
            8.4,
            8.6,
            8.8,
            9,
            9.2,
            9.4,
            9.6,
            9.8,
            10,
        ],
    )


def land_yield_factor_1():
    """
    Real Name: land yield factor 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Land yield factor before policy year (LYF1#104.1).
    """
    return 1


def land_yield_factor_2():
    """
    Real Name: land yield factor 2
    Original Eqn: SMOOTH3 ( Land Yield Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land yield factor after policy year (LYF1#104.2).
    """
    return _smooth_land_yield_factor_2()


def land_yield_multipler_from_air_pollution_1():
    """
    Real Name: land yield multipler from air pollution 1
    Original Eqn: land yield multipler from air pollution table 1 ( industrial output / IND OUT IN 1970 )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land yield multiplier from air pollution before air                 poll time (LYMAP1#106).
    """
    return land_yield_multipler_from_air_pollution_table_1(
        industrial_output() / ind_out_in_1970()
    )


def land_yield_multipler_from_air_pollution_table_1(x):
    """
    Real Name: land yield multipler from air pollution table 1
    Original Eqn: ( (0,1),(10,1),(20,0.7),(30,0.4) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating non-persistent pollution from                 industry to agricultural output (LYMAPT#106.1).
    """
    return lookup(x, [0, 10, 20, 30], [1, 1, 0.7, 0.4])


def land_yield_multiplier_from_air_pollution_2():
    """
    Real Name: land yield multiplier from air pollution 2
    Original Eqn: land yield multipler from air pollution table 2 ( industrial output / IND OUT IN 1970 )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land yield multiplier from air pollution after air                 poll time (LYMAP2#107).
    """
    return land_yield_multipler_from_air_pollution_table_2(
        industrial_output() / ind_out_in_1970()
    )


def land_yield_multipler_from_air_pollution_table_2(x):
    """
    Real Name: land yield multipler from air pollution table 2
    Original Eqn: ( (0,1),(10,1),(20,0.98),(30,0.95) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating non-persistent pollution from                 industry to agricultural output (LYMAPT#107.1).
    """
    return lookup(x, [0, 10, 20, 30], [1, 1, 0.98, 0.95])


def land_yield_technology_change_rate_multiplier():
    """
    Real Name: land yield technology change rate multiplier
    Original Eqn: land yield technology change rate multiplier table ( desired food ratio - food ratio )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    Land yield from technology change multiplier                 (LYCM#--)
    """
    return land_yield_technology_change_rate_multiplier_table(
        desired_food_ratio() - food_ratio()
    )


def land_yield_technology_change_rate_multiplier_table(x):
    """
    Real Name: land yield technology change rate multiplier table
    Original Eqn: ( (0,0),(1,0) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the food ratio gap to the change in                 agricultural technology (LYCMT#--).
    """
    return lookup(x, [0, 1], [0, 0])


def land_yield_technology():
    """
    Real Name: Land Yield Technology
    Original Eqn: INTEG ( land yield technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LAND YIELD TECHNOLOGY INITIATED (LYTD#--)
    """
    return _integ_land_yield_technology()


def land_life_multiplier_from_land_yield_1():
    """
    Real Name: land life multiplier from land yield 1
    Original Eqn: land life multiplier from land yield table 1 ( land yield / inherent land fertility )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land life multiplier from yield before switch time                 (LLMY1#114).
    """
    return land_life_multiplier_from_land_yield_table_1(
        land_yield() / inherent_land_fertility()
    )


def land_life_multiplier_from_land_yield_table_1(x):
    """
    Real Name: land life multiplier from land yield table 1
    Original Eqn: ( (0,1.2),(1,1),(2,0.63),(3,0.36),(4,0.16),(5,0.055),(6,0.04) ,(7,0.025),(8,0.015),(9,0.01) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating yield to the effect on land life                 (LLMY1T#114.1).
    """
    return lookup(
        x,
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1.2, 1, 0.63, 0.36, 0.16, 0.055, 0.04, 0.025, 0.015, 0.01],
    )


def land_life_multiplier_from_land_yield_2():
    """
    Real Name: land life multiplier from land yield 2
    Original Eqn: land life multiplier from land yield table 2 ( land yield / inherent land fertility )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land life multiplier from yield after switch time                 (LLMY2#115).
    """
    return land_life_multiplier_from_land_yield_table_2(
        land_yield() / inherent_land_fertility()
    )


def land_life_multiplier_from_land_yield_table_2(x):
    """
    Real Name: land life multiplier from land yield table 2
    Original Eqn: ( (0,1.2),(1,1),(2,0.63),(3,0.36),(4,0.29),(5,0.26),(6,0.24) ,(7,0.22),(8,0.21),(9,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating yield to the effect on land life                 (LLMY2T#115.1).
    """
    return lookup(
        x,
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1.2, 1, 0.63, 0.36, 0.29, 0.26, 0.24, 0.22, 0.21, 0.2],
    )


def marginal_land_yield_multiplier_from_capital():
    """
    Real Name: marginal land yield multiplier from capital
    Original Eqn: marginal land yield multiplier from capital table ( agricultural input per hectare/unit agricultural input )
    Units: hectare/$
    Limits: (None, None)
    Type: component
    Subs: None

    MARGINAL LAND YIELD MULTIPLIER FROM CAPITAL                 (MLYMC#111).
    """
    return marginal_land_yield_multiplier_from_capital_table(
        agricultural_input_per_hectare() / unit_agricultural_input()
    )


def marginal_land_yield_multiplier_from_capital_table(x):
    """
    Real Name: marginal land yield multiplier from capital table
    Original Eqn: ( (0,0.075),(40,0.03),(80,0.015),(120,0.011),(160,0.009),(200,0.008) ,(240,0.007),(280,0.006),(320,0.005),(360,0.005),(400,0.005) ,(440,0.005),(480,0.005),(520,0.005),(560,0.005),(600,0.005) )
    Units: hectare/$
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating agricultural inputs to marginal land                 yield (MLYMCT#111.1).
    """
    return lookup(
        x,
        [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600],
        [
            0.075,
            0.03,
            0.015,
            0.011,
            0.009,
            0.008,
            0.007,
            0.006,
            0.005,
            0.005,
            0.005,
            0.005,
            0.005,
            0.005,
            0.005,
            0.005,
        ],
    )


def marginal_productivity_of_agricultural_inputs():
    """
    Real Name: marginal productivity of agricultural inputs
    Original Eqn: average life agricultural inputs * land yield * marginal land yield multiplier from capital / land yield multiplier from capital
    Units: Veg equiv kg/$
    Limits: (None, None)
    Type: component
    Subs: None

    MARGINAL PRODUCTIVITY OF AGRICULTURAL INPUTS                 (MPAI#110).
    """
    return (
        average_life_agricultural_inputs()
        * land_yield()
        * marginal_land_yield_multiplier_from_capital()
        / land_yield_multiplier_from_capital()
    )


def industrial_capital_output_ratio_multiplier_from_land_yield_technology():
    """
    Real Name: industrial capital output ratio multiplier from land yield technology
    Original Eqn: industrial capital output ratio multiplier table ( land yield multiplier from technology)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    CAPITAL OUTPUT YIELD MULTIPLIER (COYM#--)
    """
    return industrial_capital_output_ratio_multiplier_table(
        land_yield_multiplier_from_technology()
    )


def industrial_capital_output_ratio_multiplier_table(x):
    """
        Real Name: industrial capital output ratio multiplier table
        Original Eqn: ( [(1,0.8)-(2,2)],(1,1),(1.2,1.05),(1.4,1.12),(1.6,1.25),(1.8,1.35),(2,1.5))
        Units: Dmnl
        Limits: (None, None)
        Type: lookup
        Subs: None

        Table relating the yield of technology to the effect                 on the capital output ratio (COYMT#--)
    !
    !
    """
    return lookup(x, [1, 1.2, 1.4, 1.6, 1.8, 2], [1, 1.05, 1.12, 1.25, 1.35, 1.5])


def technology_development_delay():
    """
    Real Name: technology development delay
    Original Eqn:
      2
      0
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The technology development delay (TDD#--)
    """
    return 20


_smooth_land_yield_factor_2 = Smooth(
    lambda: land_yield_technology(),
    lambda: technology_development_delay(),
    lambda: land_yield_technology(),
    lambda: 3,
    "_smooth_land_yield_factor_2",
)


_integ_land_yield_technology = Integ(
    lambda: land_yield_technology_change_rate(),
    lambda: 1,
    "_integ_land_yield_technology",
)
