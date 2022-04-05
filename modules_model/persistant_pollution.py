"""
Module persistant_pollution
Translated using PySD version 2.2.0
"""


def industrial_capital_output_ratio_multiplier_from_pollution_technology():
    """
    Real Name: industrial capital output ratio multiplier from pollution technology
    Original Eqn: industrial capital output ratio multiplier from pollution table ( persistent pollution generation factor )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Pollution control technology multiplier for capital                 output ratio (COPM#--).
    """
    return industrial_capital_output_ratio_multiplier_from_pollution_table(
        persistent_pollution_generation_factor()
    )


def industrial_capital_output_ratio_multiplier_from_pollution_table(x):
    """
    Real Name: industrial capital output ratio multiplier from pollution table
    Original Eqn: ( (0,1.25),(0.1,1.2),(0.2,1.15),(0.3,1.11),(0.4,1.08),(0.5,1.05) ,(0.6,1.03),(0.7,1.02),(0.8,1.01),(0.9,1),(1,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating pollution correction technology to                 the capital output ratio (COPMT#--)
    """
    return lookup(
        x,
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [1.25, 1.2, 1.15, 1.11, 1.08, 1.05, 1.03, 1.02, 1.01, 1, 1],
    )


def persistent_pollution_technology_change_rate():
    """
    Real Name: persistent pollution technology change rate
    Original Eqn: 0
    Units: 1/year
    Limits: (None, None)
    Type: constant
    Subs: None

    pollution control technology change rate (PTDR#--)
    """
    return 0


def persistent_pollution_generation_factor():
    """
    Real Name: persistent pollution generation factor
    Original Eqn: persistent pollution generation factor 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    PERSISTENT POLLUTION GENERATED FACTOR (PPGF#138).
    """
    return persistent_pollution_generation_factor_1()


def agricultural_material_toxicity_index():
    """
    Real Name: agricultural material toxicity index
    Original Eqn: 1
    Units: Pollution units/$
    Limits: (None, None)
    Type: constant
    Subs: None

    Agricultural material toxicity index (AMTI#140.2).
    """
    return 1


def assimilation_half_life():
    """
    Real Name: assimilation half life
    Original Eqn: assimilation half life in 1970 * assimilation half life multiplier
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    ASSIMILATION HALF-LIFE (AHL#146).
    """
    return assimilation_half_life_in_1970() * assimilation_half_life_multiplier()


def assimilation_half_life_in_1970():
    """
    Real Name: assimilation half life in 1970
    Original Eqn: 1.5
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Assimilation half life of persistent pollution int                 1970 (AHL70#146.1).
    """
    return 1.5


def assimilation_half_life_multiplier():
    """
    Real Name: assimilation half life multiplier
    Original Eqn: assimilation half life mult table ( persistent pollution index )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Assimilation half life of multiplier of persistent                 pollution (AHLM#145)
    """
    return assimilation_half_life_mult_table(persistent_pollution_index())


def assimilation_half_life_mult_table(x):
    """
    Real Name: assimilation half life mult table
    Original Eqn: ( (1,1),(251,11),(501,21),(751,31),(1001,41) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the level of persisten pollution to                 its assimilation rate (AHLMT#145.1).
    """
    return lookup(x, [1, 251, 501, 751, 1001], [1, 11, 21, 31, 41])


def desired_persistent_pollution_index():
    """
    Real Name: desired persistent pollution index
    Original Eqn: 1.2
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Desires persistent pollution index (DPOLX#--).
    """
    return 1.2


def fraction_of_agricultural_inputs_from_persistent_materials():
    """
    Real Name: fraction of agricultural inputs from persistent materials
    Original Eqn: 0.001
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Fraction of inputs as persistent materials                 (FIPM#140.1).
    """
    return 0.001


def fraction_of_resources_from_persistent_materials():
    """
    Real Name: fraction of resources from persistent materials
    Original Eqn: 0.02
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Fraction of resources as persistent materials                 (FRPM#139.1)
    """
    return 0.02


def industrial_material_toxicity_index():
    """
    Real Name: industrial material toxicity index
    Original Eqn: 10
    Units: Pollution units/Resource unit
    Limits: (None, None)
    Type: constant
    Subs: None

    Industrial materials toxicity index (IMTI#139.3)
    """
    return 10


def industrial_material_emissions_factor():
    """
    Real Name: industrial material emissions factor
    Original Eqn: 0.1
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Industrial materials emission factor (IMEF#139.2).
    """
    return 0.1


def persistent_pollution_generation_factor_1():
    """
    Real Name: persistent pollution generation factor 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Persistent pollution generation factor before policy                 time (PPGF1#138.1).
    """
    return 1


def persistent_pollution_generation_factor_2():
    """
    Real Name: persistent pollution generation factor 2
    Original Eqn: SMOOTH3 ( Persistent Pollution Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution generation factor after policy                 time (PPGF1#138.2).
    """
    return _smooth_persistent_pollution_generation_factor_2()


def persistent_pollution_technology_change_multiplier():
    """
    Real Name: persistent pollution technology change multiplier
    Original Eqn: persistent pollution technology change mult table ( 1 - persistent pollution index / desired persistent pollution index )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    POLLUTION CONTROL TECHNOLOGY CHANGE MULTIPLIER                 (POLGFM#--).
    """
    return persistent_pollution_technology_change_mult_table(
        1 - persistent_pollution_index() / desired_persistent_pollution_index()
    )


def persistent_pollution_technology_change_mult_table(x):
    """
    Real Name: persistent pollution technology change mult table
    Original Eqn: ( (-1,0),(0,0) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating persisten pollution to changes due to                 technology (POLGFMT#--).
    """
    return lookup(x, [-1, 0], [0, 0])


def persistent_pollution():
    """
    Real Name: Persistent Pollution
    Original Eqn: INTEG( ( persistent pollution appearance rate - persistent pollution assimilation rate ) , initial persistent pollution )
    Units: Pollution units
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution (PPOL#142).
    """
    return _integ_persistent_pollution()


def initial_persistent_pollution():
    """
    Real Name: initial persistent pollution
    Original Eqn: 2.5e+07
    Units: Pollution units
    Limits: (None, None)
    Type: constant
    Subs: None

    persistent pollution initial (PPOLI#142.2
    """
    return 2.5e07


def persistent_pollution_generation_industry():
    """
    Real Name: persistent pollution generation industry
    Original Eqn: per capita resource use multiplier * population * fraction of resources from persistent materials * industrial material emissions factor * industrial material toxicity index
    Units: Pollution units/year
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution generated by industrial output.                 (PPGIO#139)
    """
    return (
        per_capita_resource_use_multiplier()
        * population()
        * fraction_of_resources_from_persistent_materials()
        * industrial_material_emissions_factor()
        * industrial_material_toxicity_index()
    )


def persistent_pollution_generation_agriculture():
    """
    Real Name: persistent pollution generation agriculture
    Original Eqn: agricultural input per hectare * Arable Land * fraction of agricultural inputs from persistent materials * agricultural material toxicity index
    Units: Pollution units/year
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution generated by agriculture                 (PPGAO#140)
    """
    return (
        agricultural_input_per_hectare()
        * arable_land()
        * fraction_of_agricultural_inputs_from_persistent_materials()
        * agricultural_material_toxicity_index()
    )


def persistent_pollution_generation_rate():
    """
    Real Name: persistent pollution generation rate
    Original Eqn: ( persistent pollution generation industry + persistent pollution generation agriculture ) * ( persistent pollution generation factor )
    Units: Pollution units/year
    Limits: (None, None)
    Type: component
    Subs: None

    PERSISTENT POLLUTION GENERATION RATE (PPGR#137).
    """
    return (
        persistent_pollution_generation_industry()
        + persistent_pollution_generation_agriculture()
    ) * (persistent_pollution_generation_factor())


def persistent_pollution_appearance_rate():
    """
    Real Name: persistent pollution appearance rate
    Original Eqn: DELAY3 ( persistent pollution generation rate , persistent pollution transmission delay )
    Units: Pollution units/year
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution appearance rate (PPAPR#141)
    """
    return _delay_persistent_pollution_appearance_rate()


def persistent_pollution_assimilation_rate():
    """
    Real Name: persistent pollution assimilation rate
    Original Eqn: Persistent Pollution / ( assimilation half life * 1.4)
    Units: Pollution units/year
    Limits: (None, None)
    Type: component
    Subs: None

    PERSISTENT POLLUTION ASSIMILATION RATE (PPASR#144).
    """
    return persistent_pollution() / (assimilation_half_life() * 1.4)


def persistent_pollution_in_1970():
    """
    Real Name: persistent pollution in 1970
    Original Eqn: 1.36e+08
    Units: Pollution units
    Limits: (None, None)
    Type: constant
    Subs: None

    PERSISTENT POLLUTION IN 1970 (PPOL70#143.1).
    """
    return 1.36e08


def persistent_pollution_index():
    """
    Real Name: persistent pollution index
    Original Eqn: Persistent Pollution / persistent pollution in 1970
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Persistent pollution index relative to 1970                 (PPOLX#143).
    """
    return persistent_pollution() / persistent_pollution_in_1970()


def persistent_pollution_technology():
    """
    Real Name: Persistent Pollution Technology
    Original Eqn: INTEG( persistent pollution technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Pollution control technology initiated (PTD#--)
    """
    return _integ_persistent_pollution_technology()


def persistent_pollution_transmission_delay():
    """
    Real Name: persistent pollution transmission delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Persistent pollution transmission delay                 (PPTD#141.1).
    """
    return 20


def technology_development_delay():
    """
    Real Name: technology development delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The technology development delay (TDD#--)
    """
    return 20


def persistent_pollution_intensity_industry():
    """
    Real Name: persistent pollution intensity industry
    Original Eqn: persistent pollution generation industry * persistent pollution generation factor / industrial output
    Units: Pollution units/$
    Limits: (None, None)
    Type: component
    Subs: None

    pollution intensity indicator (PLINID#--).
    """
    return (
        persistent_pollution_generation_industry()
        * persistent_pollution_generation_factor()
        / industrial_output()
    )


_smooth_persistent_pollution_generation_factor_2 = Smooth(
    lambda: persistent_pollution_technology(),
    lambda: technology_development_delay(),
    lambda: persistent_pollution_technology(),
    lambda: 3,
    "_smooth_persistent_pollution_generation_factor_2",
)


_integ_persistent_pollution = Integ(
    lambda: (
        persistent_pollution_appearance_rate()
        - persistent_pollution_assimilation_rate()
    ),
    lambda: initial_persistent_pollution(),
    "_integ_persistent_pollution",
)


_delay_persistent_pollution_appearance_rate = Delay(
    lambda: persistent_pollution_generation_rate(),
    lambda: persistent_pollution_transmission_delay(),
    lambda: persistent_pollution_generation_rate(),
    lambda: 3,
    time_step,
    "_delay_persistent_pollution_appearance_rate",
)


_integ_persistent_pollution_technology = Integ(
    lambda: persistent_pollution_technology_change_rate(),
    lambda: 1,
    "_integ_persistent_pollution_technology",
)
