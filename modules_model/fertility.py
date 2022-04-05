"""
Module fertility
Translated using PySD version 2.2.0
"""


def fertility_control_effectiveness():
    """
    Real Name: fertility control effectiveness
    Original Eqn: fertility control effectiveness table ( fertility control facilities per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fertility control effectiveness (FCE#45).
    """
    return fertility_control_effectiveness_table(
        fertility_control_facilities_per_capita() / gdp_pc_unit()
    )


def desired_completed_family_size():
    """
    Real Name: desired completed family size
    Original Eqn: desired completed family size normal * family response to social norm * social family size normal
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Desired completed family size (DCFS#38)
    """
    return (
        desired_completed_family_size_normal()
        * family_response_to_social_norm()
        * social_family_size_normal()
    )


def average_industrial_output_per_capita():
    """
    Real Name: average industrial output per capita
    Original Eqn: SMOOTH ( industrial output per capita , income expectation averaging time )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Average industrial output per capita (AIOPC#43).
    """
    return _smooth_average_industrial_output_per_capita()


def completed_multiplier_from_perceived_lifetime():
    """
    Real Name: completed multiplier from perceived lifetime
    Original Eqn: completed multiplier from perceived lifetime table ( perceived life expectancy/one year)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    COMPENSATORY MULTIPLIER FROM PERCEIVED LIFE                 EXPECTANCY (CMPLE#36).
    """
    return completed_multiplier_from_perceived_lifetime_table(
        perceived_life_expectancy() / one_year()
    )


def completed_multiplier_from_perceived_lifetime_table(x):
    """
    Real Name: completed multiplier from perceived lifetime table
    Original Eqn: ( (0,3),(10,2.1),(20,1.6),(30,1.4),(40,1.3),(50,1.2),(60,1.1) ,(70,1.05),(80,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating perceived life expectancy to birth                 rate compensation (CMPLET#36.1).
    """
    return lookup(
        x,
        [0, 10, 20, 30, 40, 50, 60, 70, 80],
        [3, 2.1, 1.6, 1.4, 1.3, 1.2, 1.1, 1.05, 1],
    )


def delayed_industrial_output_per_capita():
    """
    Real Name: delayed industrial output per capita
    Original Eqn: SMOOTH3 ( industrial output per capita , social adjustment delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Delayed industrial output per capita (DIOPC#40).
    """
    return _smooth_delayed_industrial_output_per_capita()


def desired_completed_family_size_normal():
    """
    Real Name: desired completed family size normal
    Original Eqn: 3.8
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    DESIRED COMPLETED FAMILY SIZE NORMAL (DCFSN#38.2).
    """
    return 3.8


def desired_total_fertility():
    """
    Real Name: desired total fertility
    Original Eqn: desired completed family size * completed multiplier from perceived lifetime
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    DESIRED TOTAL FERTILITY (DTF#35).
    """
    return (
        desired_completed_family_size() * completed_multiplier_from_perceived_lifetime()
    )


def family_income_expectation():
    """
    Real Name: family income expectation
    Original Eqn: ( industrial output per capita - average industrial output per capita ) / average industrial output per capita
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Family income expectations (FIE#42).
    """
    return (
        industrial_output_per_capita() - average_industrial_output_per_capita()
    ) / average_industrial_output_per_capita()


def family_response_to_social_norm():
    """
    Real Name: family response to social norm
    Original Eqn: family response to social norm table ( family income expectation )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FAMILY RESPONSE TO SOCIAL NORM (FRSN#41).
    """
    return family_response_to_social_norm_table(family_income_expectation())


def family_response_to_social_norm_table(x):
    """
    Real Name: family response to social norm table
    Original Eqn: ( (-0.2,0.5),(-0.1,0.6),(0,0.7),(0.1,0.85),(0.2,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating income expectations to family                 size (FRSNT#41.1).
    """
    return lookup(x, [-0.2, -0.1, 0, 0.1, 0.2], [0.5, 0.6, 0.7, 0.85, 1])


def fecundity_multiplier():
    """
    Real Name: fecundity multiplier
    Original Eqn: fecundity multiplier table ( life expectancy/one year )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FECUNDITY MULTIPLIER (FM#34).
    """
    return fecundity_multiplier_table(life_expectancy() / one_year())


def fecundity_multiplier_table(x):
    """
    Real Name: fecundity multiplier table
    Original Eqn: ( (0,0),(10,0.2),(20,0.4),(30,0.6),(40,0.7),(50,0.75),(60,0.79) ,(70,0.84),(80,0.87) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating life expectancy to fecundity                 (FMT#34.1).
    """
    return lookup(
        x,
        [0, 10, 20, 30, 40, 50, 60, 70, 80],
        [0, 0.2, 0.4, 0.6, 0.7, 0.75, 0.79, 0.84, 0.87],
    )


def fertility_control_allocation_per_capita():
    """
    Real Name: fertility control allocation per capita
    Original Eqn: fraction services allocated to fertility control * service output per capita
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    FERTILITY CONTROL ALLOCATIONS PER CAPITA (FCAPC#47).
    """
    return (
        fraction_services_allocated_to_fertility_control() * service_output_per_capita()
    )


def fertility_control_effectiveness_table(x):
    """
    Real Name: fertility control effectiveness table
    Original Eqn: ( (0,0.75),(0.5,0.85),(1,0.9),(1.5,0.95),(2,0.98),(2.5,0.99) ,(3,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Fertility control effectiveness table (FCET#45.2).
    """
    return lookup(
        x, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0.75, 0.85, 0.9, 0.95, 0.98, 0.99, 1]
    )


def fertility_control_facilities_per_capita():
    """
    Real Name: fertility control facilities per capita
    Original Eqn: SMOOTH3 ( fertility control allocation per capita , health services impact delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    FERTILITY CONTROL FACILITIES PER CAPITA (FCFPC#46).
    """
    return _smooth_fertility_control_facilities_per_capita()


def fraction_services_allocated_to_fertility_control():
    """
    Real Name: fraction services allocated to fertility control
    Original Eqn: fraction services allocated to fertility control table ( need for fertility control)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF SERVICES ALLOCATED TO FERTILITY CONTROL                 (FSAFC#48).
    """
    return fraction_services_allocated_to_fertility_control_table(
        need_for_fertility_control()
    )


def fraction_services_allocated_to_fertility_control_table(x):
    """
    Real Name: fraction services allocated to fertility control table
    Original Eqn: ( (0,0),(2,0.005),(4,0.015),(6,0.025),(8,0.03),(10,0.035) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the need for fertility control to                 services allocated. (FSAFCT#48.1).
    """
    return lookup(x, [0, 2, 4, 6, 8, 10], [0, 0.005, 0.015, 0.025, 0.03, 0.035])


def income_expectation_averaging_time():
    """
    Real Name: income expectation averaging time
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Income expectation averaging time (IEAT#43.1)
    """
    return 3


def lifetime_perception_delay():
    """
    Real Name: lifetime perception delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    Lifetime perception delay (LPD#37.1)
    """
    return 20


def maximum_total_fertility():
    """
    Real Name: maximum total fertility
    Original Eqn: maximum total fertility normal * fecundity multiplier
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    MAXIMUM TOTAL FERTILITY (MTF#33).
    """
    return maximum_total_fertility_normal() * fecundity_multiplier()


def maximum_total_fertility_normal():
    """
    Real Name: maximum total fertility normal
    Original Eqn: 12
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    The normal maximum fertility that would be realized                if people had sufficient food and perfect health.                 (MTFN#33)
    """
    return 12


def need_for_fertility_control():
    """
    Real Name: need for fertility control
    Original Eqn: ( maximum total fertility / desired total fertility ) - 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    NEED FOR FERTILITY CONTROL (NFC#44).
    """
    return (maximum_total_fertility() / desired_total_fertility()) - 1


def perceived_life_expectancy():
    """
    Real Name: perceived life expectancy
    Original Eqn: SMOOTH3 ( life expectancy , lifetime perception delay )
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    Perceived life expectancy (PLE#37)
    """
    return _smooth_perceived_life_expectancy()


def social_family_size_normal():
    """
    Real Name: social family size normal
    Original Eqn: social family size normal table ( delayed industrial output per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    SOCIAL FAMILY SIZE NORM (SFN#39).
    """
    return social_family_size_normal_table(
        delayed_industrial_output_per_capita() / gdp_pc_unit()
    )


def social_family_size_normal_table(x):
    """
    Real Name: social family size normal table
    Original Eqn: ( (0,1.25),(200,0.94),(400,0.715),(600,0.59),(800,0.5))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating material well being to family size                 (SFNT#39.1)
    """
    return lookup(x, [0, 200, 400, 600, 800], [1.25, 0.94, 0.715, 0.59, 0.5])


def social_adjustment_delay():
    """
    Real Name: social adjustment delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    SOCIAL ADJUSTMENT DELAY (SAD#40.1).
    """
    return 20


def total_fertility():
    """
    Real Name: total fertility
    Original Eqn: MIN ( maximum total fertility , ( maximum total fertility * ( 1 - fertility control effectiveness ) + desired total fertility * fertility control effectiveness ) )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    TOTAL FERTILITY (TF#32).
    """
    return np.minimum(
        maximum_total_fertility(),
        (
            maximum_total_fertility() * (1 - fertility_control_effectiveness())
            + desired_total_fertility() * fertility_control_effectiveness()
        ),
    )


_smooth_average_industrial_output_per_capita = Smooth(
    lambda: industrial_output_per_capita(),
    lambda: income_expectation_averaging_time(),
    lambda: industrial_output_per_capita(),
    lambda: 1,
    "_smooth_average_industrial_output_per_capita",
)


_smooth_delayed_industrial_output_per_capita = Smooth(
    lambda: industrial_output_per_capita(),
    lambda: social_adjustment_delay(),
    lambda: industrial_output_per_capita(),
    lambda: 3,
    "_smooth_delayed_industrial_output_per_capita",
)


_smooth_fertility_control_facilities_per_capita = Smooth(
    lambda: fertility_control_allocation_per_capita(),
    lambda: health_services_impact_delay(),
    lambda: fertility_control_allocation_per_capita(),
    lambda: 3,
    "_smooth_fertility_control_facilities_per_capita",
)


_smooth_perceived_life_expectancy = Smooth(
    lambda: life_expectancy(),
    lambda: lifetime_perception_delay(),
    lambda: life_expectancy(),
    lambda: 3,
    "_smooth_perceived_life_expectancy",
)
