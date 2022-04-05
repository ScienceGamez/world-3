"""
Module industrial_output
Translated using PySD version 2.2.0
"""


def fraction_of_industrial_output_allocated_to_consumption():
    """
    Real Name: fraction of industrial output allocated to consumption
    Original Eqn: 0.43
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Fraction of industrial output allocated to                 consumption (FIAOC#58)
    """
    return 0.43


def industrial_capital_output_ratio():
    """
    Real Name: industrial capital output ratio
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    INDUSTRIAL CAPITAL-OUTPUT RATIO (ICOR#51)
    """
    return 3


def average_life_of_industrial_capital():
    """
    Real Name: average life of industrial capital
    Original Eqn: 14
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    AVERAGE LIFETIME OF INDUSTRIAL CAPITAL (ALIC#54).
    """
    return 14


def fraction_of_industrial_output_allocated_to_investment():
    """
    Real Name: fraction of industrial output allocated to investment
    Original Eqn: ( 1 - fraction of industrial output allocated to agriculture - fraction of industrial output allocated to services - fraction of industrial output allocated to consumption )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of industrial output allocated to industry                 (FIAOI#56).
    """
    return (
        1
        - fraction_of_industrial_output_allocated_to_agriculture()
        - fraction_of_industrial_output_allocated_to_services()
        - fraction_of_industrial_output_allocated_to_consumption()
    )


def industrial_capital_depreciation():
    """
    Real Name: industrial capital depreciation
    Original Eqn: Industrial Capital / average life of industrial capital
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    Industrial capital depreciation rate (ICDR#53).
    """
    return industrial_capital() / average_life_of_industrial_capital()


def industrial_capital_investment():
    """
    Real Name: industrial capital investment
    Original Eqn: ( ( industrial output ) ) * ( fraction of industrial output allocated to investment )
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    Industrial capital investment rate (ICIR#55).
    """
    return ((industrial_output())) * (
        fraction_of_industrial_output_allocated_to_investment()
    )


def industrial_output_per_capita():
    """
    Real Name: industrial output per capita
    Original Eqn: industrial output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    INDUSTRIAL OUTPUT PER CAPITA (IOPC#49)
    """
    return industrial_output() / population()


def industrial_output_per_capita_desired():
    """
    Real Name: industrial output per capita desired
    Original Eqn: 400
    Units: $/(Person*year)
    Limits: (None, None)
    Type: constant
    Subs: None

    Industrial output per capita desired (IOPCD#59.2).
    """
    return 400


def industrial_capital():
    """
    Real Name: Industrial Capital
    Original Eqn: INTEG( ( industrial capital investment - industrial capital depreciation ) , initial industrial capital )
    Units: $
    Limits: (None, None)
    Type: component
    Subs: None

    INDUSTRIAL CAPITAL (IC#52).
    """
    return _integ_industrial_capital()


def initial_industrial_capital():
    """
    Real Name: initial industrial capital
    Original Eqn: 2.1e+11
    Units: $
    Limits: (None, None)
    Type: constant
    Subs: None

    INDUSTRIAL CAPITAL INITIAL (ICI#52.1).
    """
    return 2.1e11


def industrial_output():
    """
    Real Name: industrial output
    Original Eqn: ( ( ( Industrial Capital ) ) * ( 1 - fraction of industrial capital allocated to obtaining resources )) * ( capacity utilization fraction ) / industrial capital output ratio
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    Industrial output (IO#50)
    """
    return (
        (
            ((industrial_capital()))
            * (1 - fraction_of_industrial_capital_allocated_to_obtaining_resources())
        )
        * (capacity_utilization_fraction())
        / industrial_capital_output_ratio()
    )


def fraction_of_industrial_output_allocated_to_consumption_variable():
    """
    Real Name: fraction of industrial output allocated to consumption variable
    Original Eqn: fraction of industrial output allocated to consumption variable table ( industrial output per capita / industrial output per capita desired )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction industrial output allocated to consumption                 variable (FIAOCV#59)
    """
    return fraction_of_industrial_output_allocated_to_consumption_variable_table(
        industrial_output_per_capita() / industrial_output_per_capita_desired()
    )


def fraction_of_industrial_output_allocated_to_consumption_variable_table(x):
    """
    Real Name: fraction of industrial output allocated to consumption variable table
    Original Eqn: ( (0,0.3),(0.2,0.32),(0.4,0.34),(0.6,0.36),(0.8,0.38),(1,0.43) ,(1.2,0.73),(1.4,0.77),(1.6,0.81),(1.8,0.82),(2,0.83) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Fraction of industrial output allocated to                 consumption variable TABLE (FIAOCVT#59.1)
    """
    return lookup(
        x,
        [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2],
        [0.3, 0.32, 0.34, 0.36, 0.38, 0.43, 0.73, 0.77, 0.81, 0.82, 0.83],
    )


def industrial_capital_output_ratio_2():
    """
    Real Name: industrial capital output ratio 2
    Original Eqn: industrial capital output ratio multiplier from resource conservation technology* industrial capital output ratio multiplier from land yield technology * industrial capital output ratio multiplier from pollution technology
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    Industrial capital output ratio after the policy                 year (ICOR2#51.2)
    """
    return (
        industrial_capital_output_ratio_multiplier_from_resource_conservation_technology()
        * industrial_capital_output_ratio_multiplier_from_land_yield_technology()
        * industrial_capital_output_ratio_multiplier_from_pollution_technology()
    )


_integ_industrial_capital = Integ(
    lambda: (industrial_capital_investment() - industrial_capital_depreciation()),
    lambda: initial_industrial_capital(),
    "_integ_industrial_capital",
)
