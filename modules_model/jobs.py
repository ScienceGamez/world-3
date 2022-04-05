"""
Module jobs
Translated using PySD version 2.2.0
"""


def delayed_labor_utilization_fraction():
    """
    Real Name: Delayed Labor Utilization Fraction
    Original Eqn: SMOOTHI (labor utilization fraction, labor utilization fraction delay time ,1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    LABOR UTILIZATION FRACTION DELAYED (LUFD#82)
    """
    return _smooth_delayed_labor_utilization_fraction()


def capacity_utilization_fraction():
    """
    Real Name: capacity utilization fraction
    Original Eqn: ACTIVE INITIAL( capacity utilization fraction table ( Delayed Labor Utilization Fraction) , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    CAPITAL UTILIZATION FRACTION (CUF#83)
    """
    return active_initial(
        __data["time"],
        lambda: capacity_utilization_fraction_table(
            delayed_labor_utilization_fraction()
        ),
        1,
    )


def capacity_utilization_fraction_table(x):
    """
    Real Name: capacity utilization fraction table
    Original Eqn: ( (1,1),(3,0.9),(5,0.7),(7,0.3),(9,0.1),(11,0.1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating labor utilization to capacity                 utilization (CUFT#83.2).
    """
    return lookup(x, [1, 3, 5, 7, 9, 11], [1, 0.9, 0.7, 0.3, 0.1, 0.1])


def jobs():
    """
    Real Name: jobs
    Original Eqn: potential jobs industrial sector + potential jobs agricultural sector + potential jobs service sector
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    JOBS (J#73).
    """
    return (
        potential_jobs_industrial_sector()
        + potential_jobs_agricultural_sector()
        + potential_jobs_service_sector()
    )


def jobs_per_hectare():
    """
    Real Name: jobs per hectare
    Original Eqn: jobs per hectare table ( agricultural input per hectare/unit agricultural input )
    Units: Person/hectare
    Limits: (None, None)
    Type: component
    Subs: None

    Jobs per hectare in agriculture (JPH#79).
    """
    return jobs_per_hectare_table(
        agricultural_input_per_hectare() / unit_agricultural_input()
    )


def jobs_per_hectare_table(x):
    """
    Real Name: jobs per hectare table
    Original Eqn: ( (2,2),(6,0.5),(10,0.4),(14,0.3),(18,0.27),(22,0.24),(26,0.2) ,(30,0.2) )
    Units: Person/hectare
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating agricultural input intensity to the                number of jobs per hectare in agriculture                 (JPHT#79.1).
    """
    return lookup(
        x, [2, 6, 10, 14, 18, 22, 26, 30], [2, 0.5, 0.4, 0.3, 0.27, 0.24, 0.2, 0.2]
    )


def jobs_per_industrial_capital_unit():
    """
    Real Name: jobs per industrial capital unit
    Original Eqn: ( jobs per industrial capital unit table ( industrial output per capita/GDP pc unit ) ) * 0.001
    Units: Person/$
    Limits: (None, None)
    Type: component
    Subs: None

    Jobs per industrial capital units (JPICU#75).
    """
    return (
        jobs_per_industrial_capital_unit_table(
            industrial_output_per_capita() / gdp_pc_unit()
        )
    ) * 0.001


def jobs_per_industrial_capital_unit_table(x):
    """
    Real Name: jobs per industrial capital unit table
    Original Eqn: ( (50,0.37),(200,0.18),(350,0.12),(500,0.09),(650,0.07),(800,0.06) )
    Units: Person/$
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output per capita to job                 per industrial capital unit (JPICUT#75.1).
    """
    return lookup(
        x, [50, 200, 350, 500, 650, 800], [0.37, 0.18, 0.12, 0.09, 0.07, 0.06]
    )


def jobs_per_service_capital_unit():
    """
    Real Name: jobs per service capital unit
    Original Eqn: ( jobs per service capital unit table ( service output per capita/GDP pc unit ) ) * 0.001
    Units: Person/$
    Limits: (None, None)
    Type: component
    Subs: None

    Jobs per service capital unit (JPSCU#77).
    """
    return (
        jobs_per_service_capital_unit_table(service_output_per_capita() / gdp_pc_unit())
    ) * 0.001


def jobs_per_service_capital_unit_table(x):
    """
    Real Name: jobs per service capital unit table
    Original Eqn: ( (50,1.1),(200,0.6),(350,0.35),(500,0.2),(650,0.15),(800,0.15) )
    Units: Person/$
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating service output per capita to job per                 service capital unit (JPICUT#77.1).
    """
    return lookup(x, [50, 200, 350, 500, 650, 800], [1.1, 0.6, 0.35, 0.2, 0.15, 0.15])


def labor_utilization_fraction():
    """
    Real Name: labor utilization fraction
    Original Eqn: jobs / labor force
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Labor utilization fraction (LUF#81).
    """
    return jobs() / labor_force()


def labor_utilization_fraction_delay_time():
    """
    Real Name: labor utilization fraction delay time
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Labor utilization fraction delay time (LUFDT#82.1)
    """
    return 2


def potential_jobs_agricultural_sector():
    """
    Real Name: potential jobs agricultural sector
    Original Eqn: ( ( jobs per hectare ) ) * ( Arable Land )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    Potential jobs in the agricultural sector (PJAS#78).
    """
    return ((jobs_per_hectare())) * (arable_land())


def potential_jobs_industrial_sector():
    """
    Real Name: potential jobs industrial sector
    Original Eqn: Industrial Capital * jobs per industrial capital unit
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    POTENTIAL JOBS IN INDUSTRIAL SECTOR (PKIS#74).
    """
    return industrial_capital() * jobs_per_industrial_capital_unit()


def potential_jobs_service_sector():
    """
    Real Name: potential jobs service sector
    Original Eqn: ( ( Service Capital ) ) * ( jobs per service capital unit )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    Potential jobs in the service sector (PJSS#76).
    """
    return ((service_capital())) * (jobs_per_service_capital_unit())


_smooth_delayed_labor_utilization_fraction = Smooth(
    lambda: labor_utilization_fraction(),
    lambda: labor_utilization_fraction_delay_time(),
    lambda: 1,
    lambda: 1,
    "_smooth_delayed_labor_utilization_fraction",
)
