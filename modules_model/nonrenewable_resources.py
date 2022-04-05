"""
Module nonrenewable_resources
Translated using PySD version 2.2.0
"""


def industrial_capital_output_ratio_multiplier_from_resource_conservation_technology():
    """
    Real Name: industrial capital output ratio multiplier from resource conservation technology
    Original Eqn: industrial capital output ratio multiplier from resource table ( resource use factor )
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    Technology driven industrial capital output ratio                 (ICOR2T#--)
    """
    return industrial_capital_output_ratio_multiplier_from_resource_table(
        resource_use_factor()
    )


def industrial_capital_output_ratio_multiplier_from_resource_table(x):
    """
    Real Name: industrial capital output ratio multiplier from resource table
    Original Eqn: ( (0,3.75),(0.1,3.6),(0.2,3.47),(0.3,3.36),(0.4,3.25),(0.5,3.16) ,(0.6,3.1),(0.7,3.06),(0.8,3.02),(0.9,3.01),(1,3) )
    Units: year
    Limits: (None, None)
    Type: lookup
    Subs: None

    CAPITAL OUTPUT FROM RESOURCES technology multiplier                 TABLE (ICOR2TT#--)
    """
    return lookup(
        x,
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [3.75, 3.6, 3.47, 3.36, 3.25, 3.16, 3.1, 3.06, 3.02, 3.01, 3],
    )


def resource_technology_change_rate():
    """
    Real Name: resource technology change rate
    Original Eqn: 0
    Units: 1/year
    Limits: (None, None)
    Type: constant
    Subs: None

    RESOURCE TECHNOLOGY IMPROVEMENT RATE (NRATE-##).
    """
    return 0


def fraction_of_industrial_capital_allocated_to_obtaining_resources():
    """
    Real Name: fraction of industrial capital allocated to obtaining resources
    Original Eqn: fraction of capital allocated to obtaining resources 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF CAPITAL ALLOCATED TO OBTAINING RESOURCES                 (FCAOR#134).
    """
    return fraction_of_capital_allocated_to_obtaining_resources_1()


def resource_use_factor():
    """
    Real Name: resource use factor
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    NONRENEWABLE RESOURCE USAGE FACTOR (NRUF#131).
    """
    return 1


def desired_resource_use_rate():
    """
    Real Name: desired resource use rate
    Original Eqn: 4.8e+09
    Units: Resource units/year
    Limits: (None, None)
    Type: constant
    Subs: None

    Desired non-renewable resource usage rate (DNRUR#--)
    """
    return 4.8e09


def fraction_of_resources_remaining():
    """
    Real Name: fraction of resources remaining
    Original Eqn: Nonrenewable Resources / initial nonrenewable resources
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Non-renewable resource fraction remaining                 (NRFR#133).
    """
    return nonrenewable_resources() / initial_nonrenewable_resources()


def resource_usage_rate():
    """
    Real Name: resource usage rate
    Original Eqn: ( ( ( population ) ) * ( per capita resource use multiplier ) ) * ( resource use factor )
    Units: Resource units/year
    Limits: (None, None)
    Type: component
    Subs: None

    Non-renewable resource use rate (NRUR#130).
    """
    return (((population())) * (per_capita_resource_use_multiplier())) * (
        resource_use_factor()
    )


def initial_nonrenewable_resources():
    """
    Real Name: initial nonrenewable resources
    Original Eqn: 1e+12
    Units: Resource units
    Limits: (None, None)
    Type: constant
    Subs: None

    NONRENEWABLE RESOURCE INITIAL (NR#129.2).
    """
    return 1e12


def nonrenewable_resources():
    """
    Real Name: Nonrenewable Resources
    Original Eqn: INTEG( ( - resource usage rate ) , initial nonrenewable resources )
    Units: Resource units
    Limits: (None, None)
    Type: component
    Subs: None

    Non-renewable resource (NR#129)
    """
    return _integ_nonrenewable_resources()


def fraction_of_capital_allocated_to_obtaining_resources_1():
    """
    Real Name: fraction of capital allocated to obtaining resources 1
    Original Eqn: fraction of capital allocated to obtaining resources 1 table ( fraction of resources remaining )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of capital allocated to obtaining resources                 before switch time (FCAOR1#135).
    """
    return fraction_of_capital_allocated_to_obtaining_resources_1_table(
        fraction_of_resources_remaining()
    )


def fraction_of_capital_allocated_to_obtaining_resources_1_table(x):
    """
    Real Name: fraction of capital allocated to obtaining resources 1 table
    Original Eqn: ( (0,1),(0.1,0.9),(0.2,0.7),(0.3,0.5),(0.4,0.2),(0.5,0.1),(0.6,0.05) ,(0.7,0.05),(0.8,0.05),(0.9,0.05),(1,0.05) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the fraction of resources remaining                to capital allocated to resource extraction                 (FCAOR1T#135.1).
    """
    return lookup(
        x,
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [1, 0.9, 0.7, 0.5, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05],
    )


def fraction_of_capital_allocated_to_obtaining_resources_2():
    """
    Real Name: fraction of capital allocated to obtaining resources 2
    Original Eqn: fraction of capital allocated to obtaining resources 2 table ( fraction of resources remaining )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of capital allocated to obtaining resources                 after switch time (FCAOR2#136).
    """
    return fraction_of_capital_allocated_to_obtaining_resources_2_table(
        fraction_of_resources_remaining()
    )


def fraction_of_capital_allocated_to_obtaining_resources_2_table(x):
    """
    Real Name: fraction of capital allocated to obtaining resources 2 table
    Original Eqn: ( (0,1),(0.1,0.2),(0.2,0.1),(0.3,0.05),(0.4,0.05),(0.5,0.05) ,(0.6,0.05),(0.7,0.05),(0.8,0.05),(0.9,0.05),(1,0.05) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the fraction of resources remaining                to capital allocated to resource extraction                 (FCAOR2T#136.1).
    """
    return lookup(
        x,
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [1, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    )


def resource_use_fact_2():
    """
    Real Name: resource use fact 2
    Original Eqn: SMOOTH3 ( Resource Conservation Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    The nonrenewable resource usage factor after the                 policy year (NRUF2#131.2).
    """
    return _smooth_resource_use_fact_2()


def resource_technology_change_rate_multiplier():
    """
    Real Name: resource technology change rate multiplier
    Original Eqn: resource technology change mult table ( 1 - resource usage rate / desired resource use rate )
    Units: Dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None

    Resource technology change multiplier (NRCM#--)
    """
    return resource_technology_change_mult_table(
        1 - resource_usage_rate() / desired_resource_use_rate()
    )


def resource_technology_change_mult_table(x):
    """
    Real Name: resource technology change mult table
    Original Eqn: ( (-1,0),(0,0) )
    Units: Dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating resource use to technological change.                 (NRCMT#--)
    """
    return lookup(x, [-1, 0], [0, 0])


def per_capita_resource_use_multiplier():
    """
    Real Name: per capita resource use multiplier
    Original Eqn: per capita resource use mult table ( industrial output per capita/GDP pc unit )
    Units: Resource unit/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Per capita resource usage multiplier (PCRUM#132).
    """
    return per_capita_resource_use_mult_table(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def per_capita_resource_use_mult_table(x):
    """
    Real Name: per capita resource use mult table
    Original Eqn: ( (0,0),(200,0.85),(400,2.6),(600,3.4),(800,3.8),(1000,4.1), (1200,4.4),(1400,4.7),(1600,5) )
    Units: Resource units/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output to resource usage                 per capita (PCRUMT#132.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [0, 0.85, 2.6, 3.4, 3.8, 4.1, 4.4, 4.7, 5],
    )


def resource_conservation_technology():
    """
    Real Name: Resource Conservation Technology
    Original Eqn: INTEG ( resource technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Non-renewable resource technology (NRTD#--)
    """
    return _integ_resource_conservation_technology()


_integ_nonrenewable_resources = Integ(
    lambda: (-resource_usage_rate()),
    lambda: initial_nonrenewable_resources(),
    "_integ_nonrenewable_resources",
)


_smooth_resource_use_fact_2 = Smooth(
    lambda: resource_conservation_technology(),
    lambda: technology_development_delay(),
    lambda: resource_conservation_technology(),
    lambda: 3,
    "_smooth_resource_use_fact_2",
)


_integ_resource_conservation_technology = Integ(
    lambda: resource_technology_change_rate(),
    lambda: 1,
    "_integ_resource_conservation_technology",
)
