"""
Module output_graphs
Translated using PySD version 2.2.0
"""


def land_yield_technology_change_rate_multiplier_table(x):
    """
    Real Name: land yield technology change rate multiplier table
    Original Eqn:
      (
        .
        .
        .
      )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the food ratio gap to the change in                 agricultural technology (LYCMT#--).
    """
    return lookup(x, [0, 1], [0, 0])


def persistent_pollution_technology_change_mult_table(x):
    """
    Real Name: persistent pollution technology change mult table
    Original Eqn:
      (
        .
        .
        .
      )
    Units: 1/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating persisten pollution to changes due to                 technology (POLGFMT#--).
    """
    return lookup(x, [-1, 0], [0, 0])


def resource_technology_change_mult_table(x):
    """
    Real Name: resource technology change mult table
    Original Eqn:
      (
        .
        .
        .
      )
    Units: Dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating resource use to technological change.                 (NRCMT#--)
    """
    return lookup(x, [-1, 0], [0, 0])
