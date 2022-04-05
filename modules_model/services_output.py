"""
Module services_output
Translated using PySD version 2.2.0
"""


def indicated_services_output_per_capita():
    """
    Real Name: indicated services output per capita
    Original Eqn: indicated services output per capita 1
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated service output per capita (ISOPC#60).
    """
    return indicated_services_output_per_capita_1()


def fraction_of_industrial_output_allocated_to_services():
    """
    Real Name: fraction of industrial output allocated to services
    Original Eqn: fraction of industrial output allocated to services 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 (FIOAS#63).
    """
    return fraction_of_industrial_output_allocated_to_services_1()


def average_life_of_service_capital():
    """
    Real Name: average life of service capital
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    AVERAGE LIFETIME OF SERVICE CAPITAL (ALSC#69)
    """
    return 20


def service_capital_output_ratio():
    """
    Real Name: service capital output ratio
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Service capital output ratio (SCOR#72).
    """
    return 1


def fraction_of_industrial_output_allocated_to_services_1():
    """
    Real Name: fraction of industrial output allocated to services 1
    Original Eqn: fraction of industrial output allocated to services table 1 ( service output per capita/ indicated services output per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 before policy year (FIOAS1#64).
    """
    return fraction_of_industrial_output_allocated_to_services_table_1(
        service_output_per_capita() / indicated_services_output_per_capita()
    )


def fraction_of_industrial_output_allocated_to_services_table_1(x):
    """
    Real Name: fraction of industrial output allocated to services table 1
    Original Eqn: ( (0,0.3),(0.5,0.2),(1,0.1),(1.5,0.05),(2,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating service output to the fraction of                industrial output allocated to service                 (FIOAS1T#64.1).
    """
    return lookup(x, [0, 0.5, 1, 1.5, 2], [0.3, 0.2, 0.1, 0.05, 0])


def fraction_of_industrial_output_allocated_to_services_2():
    """
    Real Name: fraction of industrial output allocated to services 2
    Original Eqn: fraction of industrial output allocated to services table 2 ( service output per capita/ indicated services output per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 after policy year (FIOAS2#65).
    """
    return fraction_of_industrial_output_allocated_to_services_table_2(
        service_output_per_capita() / indicated_services_output_per_capita()
    )


def fraction_of_industrial_output_allocated_to_services_table_2(x):
    """
    Real Name: fraction of industrial output allocated to services table 2
    Original Eqn: ( (0,0.3),(0.5,0.2),(1,0.1),(1.5,0.05),(2,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating service output to the fraction of                industrial output allocated to service                 (FIOAS2T#65.1).
    """
    return lookup(x, [0, 0.5, 1, 1.5, 2], [0.3, 0.2, 0.1, 0.05, 0])


def indicated_services_output_per_capita_1():
    """
    Real Name: indicated services output per capita 1
    Original Eqn: indicated services output per capita table 1 ( industrial output per capita/GDP pc unit)
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated service output per capita before policy                 year (ISOPC1#61).
    """
    return indicated_services_output_per_capita_table_1(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def indicated_services_output_per_capita_table_1(x):
    """
    Real Name: indicated services output per capita table 1
    Original Eqn: ( (0,40),(200,300),(400,640),(600,1000),(800,1220),(1000,1450) ,(1200,1650),(1400,1800),(1600,2000) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output per capita to the                indicated service output per capita before policy                 year (ISOPC1T#61.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [40, 300, 640, 1000, 1220, 1450, 1650, 1800, 2000],
    )


def indicated_services_output_per_capita_2():
    """
    Real Name: indicated services output per capita 2
    Original Eqn: indicated services output per capita table 2 ( industrial output per capita/GDP pc unit)
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated service output per capita after policy                 year (ISOPC2#621).
    """
    return indicated_services_output_per_capita_table_2(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def indicated_services_output_per_capita_table_2(x):
    """
    Real Name: indicated services output per capita table 2
    Original Eqn: ( (0,40),(200,300),(400,640),(600,1000),(800,1220),(1000,1450) ,(1200,1650),(1400,1800),(1600,2000) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output per capita to the                indicated service output per capita afte policy                 year (ISOPC1T#62.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [40, 300, 640, 1000, 1220, 1450, 1650, 1800, 2000],
    )


def service_capital_depreciation():
    """
    Real Name: service capital depreciation
    Original Eqn: Service Capital / average life of service capital
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    SERVICE CAPITAL DEPRECIATION RATE (SCDR#68).
    """
    return service_capital() / average_life_of_service_capital()


def service_capital_investment():
    """
    Real Name: service capital investment
    Original Eqn: ( ( industrial output ) ) * ( fraction of industrial output allocated to services )
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    SERVICE CAPITAL INVESTMENT RATE (SCIR#66).
    """
    return ((industrial_output())) * (
        fraction_of_industrial_output_allocated_to_services()
    )


def service_output_per_capita():
    """
    Real Name: service output per capita
    Original Eqn: service output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    SERVICE OUTPUT PER CAPITA (SOPC#71).
    """
    return service_output() / population()


def service_capital():
    """
    Real Name: Service Capital
    Original Eqn: INTEG( ( service capital investment - service capital depreciation ) , initial service capital )
    Units: $
    Limits: (None, None)
    Type: component
    Subs: None

    Service capital (SC#67).
    """
    return _integ_service_capital()


def initial_service_capital():
    """
    Real Name: initial service capital
    Original Eqn: 1.44e+11
    Units: $
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial level of service capital (SCI#67.2)
    """
    return 1.44e11


def service_output():
    """
    Real Name: service output
    Original Eqn: ( ( Service Capital ) ) * ( capacity utilization fraction ) / service capital output ratio
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    Service output (SO#70).
    """
    return (
        ((service_capital()))
        * (capacity_utilization_fraction())
        / service_capital_output_ratio()
    )


_integ_service_capital = Integ(
    lambda: (service_capital_investment() - service_capital_depreciation()),
    lambda: initial_service_capital(),
    "_integ_service_capital",
)
