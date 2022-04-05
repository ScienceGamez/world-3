"""
Module demographics
Translated using PySD version 2.2.0
"""


def labor_force():
    """
    Real Name: labor force
    Original Eqn: ( Population 15 To 44 + Population 45 To 64 ) * labor force participation fraction
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    LABOR FORCE (LF#80).
    """
    return (
        population_15_to_44() + population_45_to_64()
    ) * labor_force_participation_fraction()


def labor_force_participation_fraction():
    """
    Real Name: labor force participation fraction
    Original Eqn: 0.75
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    LABOR FORCE PARTICIPATION FRACTION (LFPF#80.1)
    """
    return 0.75


def deaths_0_to_14():
    """
    Real Name: deaths 0 to 14
    Original Eqn: Population 0 To 14 * mortality 0 to 14
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The number of deaths per year among people 0 to 14                 years of age (D1#3).
    """
    return population_0_to_14() * mortality_0_to_14()


def deaths_15_to_44():
    """
    Real Name: deaths 15 to 44
    Original Eqn: Population 15 To 44 * mortality 15 to 44
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The number of deaths per year among people 15 to 44                 years of age (D2#7).
    """
    return population_15_to_44() * mortality_15_to_44()


def deaths_45_to_64():
    """
    Real Name: deaths 45 to 64
    Original Eqn: Population 45 To 64 * mortality 45 to 64
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The number of deaths per year among people 55 to 64                 years of age (D3#11).
    """
    return population_45_to_64() * mortality_45_to_64()


def deaths_65_plus():
    """
    Real Name: deaths 65 plus
    Original Eqn: Population 65 Plus * mortality 65 plus
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The number of deaths per year among people 65 and                 older (D4#15).
    """
    return population_65_plus() * mortality_65_plus()


def maturation_14_to_15():
    """
    Real Name: maturation 14 to 15
    Original Eqn: ( ( Population 0 To 14 ) ) * ( 1 - mortality 0 to 14 ) / 15
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional rate at which people aged 0-14 mature                 into the next age cohort (MAT1#5).
    """
    return ((population_0_to_14())) * (1 - mortality_0_to_14()) / 15


def maturation_44_to_45():
    """
    Real Name: maturation 44 to 45
    Original Eqn: ( ( Population 15 To 44 ) ) * ( 1 - mortality 15 to 44 ) / 30
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional rate at which people aged 15-44                 mature into the next age cohort (MAT2#9).
    """
    return ((population_15_to_44())) * (1 - mortality_15_to_44()) / 30


def maturation_64_to_65():
    """
    Real Name: maturation 64 to 65
    Original Eqn: ( ( Population 45 To 64 ) ) * ( 1 - mortality 45 to 64 ) / 20
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional rate at which people aged 45-64                 mature into the next age cohort (MAT3#13).
    """
    return ((population_45_to_64())) * (1 - mortality_45_to_64()) / 20


def mortality_45_to_64():
    """
    Real Name: mortality 45 to 64
    Original Eqn: mortality 45 to 64 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional mortality rate for people aged 45-64                 (M3#12).
    """
    return mortality_45_to_64_table(life_expectancy() / one_year())


def mortality_45_to_64_table(x):
    """
    Real Name: mortality 45 to 64 table
    Original Eqn: ( (20,0.0562),(30,0.0373),(40,0.0252),(50,0.0171),(60,0.0118) ,(70,0.0083),(80,0.006) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating average life to mortality in the                 45 to 64 age group (M2T#12.1).
    """
    return lookup(
        x,
        [20, 30, 40, 50, 60, 70, 80],
        [0.0562, 0.0373, 0.0252, 0.0171, 0.0118, 0.0083, 0.006],
    )


def mortality_65_plus():
    """
    Real Name: mortality 65 plus
    Original Eqn: mortality 65 plus table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional mortality rate for people over 65                 (M4#16).
    """
    return mortality_65_plus_table(life_expectancy() / one_year())


def mortality_65_plus_table(x):
    """
    Real Name: mortality 65 plus table
    Original Eqn: ( (20,0.13),(30,0.11),(40,0.09),(50,0.07),(60,0.06),(70,0.05) ,(80,0.04) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating average life expectancy to                 mortality among people over 65 (M4T#16.1)
    """
    return lookup(
        x, [20, 30, 40, 50, 60, 70, 80], [0.13, 0.11, 0.09, 0.07, 0.06, 0.05, 0.04]
    )


def mortality_0_to_14():
    """
    Real Name: mortality 0 to 14
    Original Eqn: mortality 0 to 14 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional mortality rate for people aged 0-14                 (M1#4).
    """
    return mortality_0_to_14_table(life_expectancy() / one_year())


def mortality_0_to_14_table(x):
    """
    Real Name: mortality 0 to 14 table
    Original Eqn: ( (20,0.0567),(30,0.0366),(40,0.0243),(50,0.0155),(60,0.0082) ,(70,0.0023),(80,0.001) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating average life to mortality in the                 0 to 14 age group (M1T#4.1).
    """
    return lookup(
        x,
        [20, 30, 40, 50, 60, 70, 80],
        [0.0567, 0.0366, 0.0243, 0.0155, 0.0082, 0.0023, 0.001],
    )


def mortality_15_to_44():
    """
    Real Name: mortality 15 to 44
    Original Eqn: mortality 15 to 44 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component
    Subs: None

    The fractional mortality rate for people aged 15-44                 (M2#8).
    """
    return mortality_15_to_44_table(life_expectancy() / one_year())


def mortality_15_to_44_table(x):
    """
    Real Name: mortality 15 to 44 table
    Original Eqn: ( (20,0.0266),(30,0.0171),(40,0.011),(50,0.0065),(60,0.004), (70,0.0016),(80,0.0008) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    The table relating average life to mortality in the                 15 to 44 age group (M2T#8.1).
    """
    return lookup(
        x,
        [20, 30, 40, 50, 60, 70, 80],
        [0.0266, 0.0171, 0.011, 0.0065, 0.004, 0.0016, 0.0008],
    )


def population_0_to_14():
    """
    Real Name: Population 0 To 14
    Original Eqn: INTEG( ( births - deaths 0 to 14 - maturation 14 to 15 ) , initial population 0 to 14 )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    World population, AGES 0-14 (P1#2)
    """
    return _integ_population_0_to_14()


def initial_population_0_to_14():
    """
    Real Name: initial population 0 to 14
    Original Eqn: 6.5e+08
    Units: Person
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial number of people aged 0 to 14 (P1I#2.2).
    """
    return 6.5e08


def population_15_to_44():
    """
    Real Name: Population 15 To 44
    Original Eqn: INTEG( ( maturation 14 to 15 - deaths 15 to 44 - maturation 44 to 45 ) , initial population 15 to 44 )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    World population, AGES 15-44 (P2#6)
    """
    return _integ_population_15_to_44()


def initial_population_15_to_44():
    """
    Real Name: initial population 15 to 44
    Original Eqn: 7e+08
    Units: Person
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial number of people aged 15 to 44                 (P2I#6.2).
    """
    return 7e08


def population_45_to_64():
    """
    Real Name: Population 45 To 64
    Original Eqn: INTEG( ( maturation 44 to 45 - deaths 45 to 64 - maturation 64 to 65 ) , initial population 54 to 64 )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    The world population aged 0 to 14 (P3#10).
    """
    return _integ_population_45_to_64()


def initial_population_54_to_64():
    """
    Real Name: initial population 54 to 64
    Original Eqn: 1.9e+08
    Units: Person
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial number of people aged 45 to 64                 (P3I#10.2).
    """
    return 1.9e08


def population_65_plus():
    """
    Real Name: Population 65 Plus
    Original Eqn: INTEG( ( maturation 64 to 65 - deaths 65 plus ) , initial population 65 plus )
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    The world population aged 65 and over (P4#14).
    """
    return _integ_population_65_plus()


def initial_population_65_plus():
    """
    Real Name: initial population 65 plus
    Original Eqn: 6e+07
    Units: Person
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial number of people aged 65 and over                 (P4I#14.2)
    """
    return 6e07


def population():
    """
    Real Name: population
    Original Eqn: Population 0 To 14 + Population 15 To 44 + Population 45 To 64 + Population 65 Plus
    Units: Person
    Limits: (None, None)
    Type: component
    Subs: None

    Total world population in all age groups (POP#1).
    """
    return (
        population_0_to_14()
        + population_15_to_44()
        + population_45_to_64()
        + population_65_plus()
    )


def births():
    """
    Real Name: births
    Original Eqn: total fertility * Population 15 To 44 * 0.5 / reproductive lifetime
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The total number of births in the world (B#30).
    """
    return total_fertility() * population_15_to_44() * 0.5 / reproductive_lifetime()


def reproductive_lifetime():
    """
    Real Name: reproductive lifetime
    Original Eqn: 30
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The number of years people can reproduce (RLT#30.1)
    """
    return 30


def deaths():
    """
    Real Name: deaths
    Original Eqn: deaths 0 to 14 + deaths 15 to 44 + deaths 45 to 64 + deaths 65 plus
    Units: Person/year
    Limits: (None, None)
    Type: component
    Subs: None

    The total number of deaths per year for all age                 groups (D#17).
    """
    return deaths_0_to_14() + deaths_15_to_44() + deaths_45_to_64() + deaths_65_plus()


_integ_population_0_to_14 = Integ(
    lambda: (births() - deaths_0_to_14() - maturation_14_to_15()),
    lambda: initial_population_0_to_14(),
    "_integ_population_0_to_14",
)


_integ_population_15_to_44 = Integ(
    lambda: (maturation_14_to_15() - deaths_15_to_44() - maturation_44_to_45()),
    lambda: initial_population_15_to_44(),
    "_integ_population_15_to_44",
)


_integ_population_45_to_64 = Integ(
    lambda: (maturation_44_to_45() - deaths_45_to_64() - maturation_64_to_65()),
    lambda: initial_population_54_to_64(),
    "_integ_population_45_to_64",
)


_integ_population_65_plus = Integ(
    lambda: (maturation_64_to_65() - deaths_65_plus()),
    lambda: initial_population_65_plus(),
    "_integ_population_65_plus",
)
