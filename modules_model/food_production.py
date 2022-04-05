"""
Module food_production
Translated using PySD version 2.2.0
"""


def fraction_of_industrial_output_allocated_to_agriculture():
    """
    Real Name: fraction of industrial output allocated to agriculture
    Original Eqn: fraction of industrial output allocated to agriculture 1
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO                 AGRICULTURE (FIOAA#93).
    """
    return fraction_of_industrial_output_allocated_to_agriculture_1()


def indicated_food_per_capita():
    """
    Real Name: indicated food per capita
    Original Eqn: indicated food per capita 1
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated food per capita (IFPC#89).
    """
    return indicated_food_per_capita_1()


def food():
    """
    Real Name: food
    Original Eqn: land yield * Arable Land * land fraction harvested * ( 1 - processing loss )
    Units: Veg equiv kg/year
    Limits: (None, None)
    Type: component
    Subs: None

    The total amount of usable food (F#87).
    """
    return (
        land_yield()
        * arable_land()
        * land_fraction_harvested()
        * (1 - processing_loss())
    )


def food_per_capita():
    """
    Real Name: food per capita
    Original Eqn: food / population
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Food per capita (FPC#88)
    """
    return food() / population()


def land_fraction_harvested():
    """
    Real Name: land fraction harvested
    Original Eqn: 0.7
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    Land fraction harvested (LFH#87.1).
    """
    return 0.7


def fraction_of_industrial_output_allocated_to_agriculture_1():
    """
    Real Name: fraction of industrial output allocated to agriculture 1
    Original Eqn: fraction industrial output allocated to agriculture table 1 ( food per capita/ indicated food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of industrial output allocated to                 agriculture before policy time (FIOAA1#94).
    """
    return fraction_industrial_output_allocated_to_agriculture_table_1(
        food_per_capita() / indicated_food_per_capita()
    )


def fraction_industrial_output_allocated_to_agriculture_table_1(x):
    """
    Real Name: fraction industrial output allocated to agriculture table 1
    Original Eqn: ( (0,0.4),(0.5,0.2),(1,0.1),(1.5,0.025),(2,0),(2.5,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating food per capita to the fraction of                industrial output allocated to agriculture                 (FIOAA1T#94.1).
    """
    return lookup(x, [0, 0.5, 1, 1.5, 2, 2.5], [0.4, 0.2, 0.1, 0.025, 0, 0])


def fraction_of_industrial_output_allocated_to_agriculture_2():
    """
    Real Name: fraction of industrial output allocated to agriculture 2
    Original Eqn: fraction industrial output allocated to agriculture table 2 ( food per capita/ indicated food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of industrial output allocated to                 agriculture after policy time (FIOAA2#95).
    """
    return fraction_industrial_output_allocated_to_agriculture_table_2(
        food_per_capita() / indicated_food_per_capita()
    )


def fraction_industrial_output_allocated_to_agriculture_table_2(x):
    """
    Real Name: fraction industrial output allocated to agriculture table 2
    Original Eqn: ( (0,0.4),(0.5,0.2),(1,0.1),(1.5,0.025),(2,0),(2.5,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating food per capita to the fraction of                industrial output allocated to agriculture                 (FIOAA2T#95.1).
    """
    return lookup(x, [0, 0.5, 1, 1.5, 2, 2.5], [0.4, 0.2, 0.1, 0.025, 0, 0])


def indicated_food_per_capita_1():
    """
    Real Name: indicated food per capita 1
    Original Eqn: indicated food per capita table 1 ( industrial output per capita/GDP pc unit )
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated foord per capita befor policy time                 (IFPC1#90).
    """
    return indicated_food_per_capita_table_1(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def indicated_food_per_capita_table_1(x):
    """
    Real Name: indicated food per capita table 1
    Original Eqn: ( (0,230),(200,480),(400,690),(600,850),(800,970),(1000,1070) ,(1200,1150),(1400,1210),(1600,1250) )
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output to indicated food                 requirements 1 (IFPC1T#90.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [230, 480, 690, 850, 970, 1070, 1150, 1210, 1250],
    )


def indicated_food_per_capita_2():
    """
    Real Name: indicated food per capita 2
    Original Eqn: indicated food per capita table 2 ( industrial output per capita/GDP pc unit )
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Indicated foord per capita after policy time                 (IFPC1#90).
    """
    return indicated_food_per_capita_table_2(
        industrial_output_per_capita() / gdp_pc_unit()
    )


def indicated_food_per_capita_table_2(x):
    """
    Real Name: indicated food per capita table 2
    Original Eqn: ( (0,230),(200,480),(400,690),(600,850),(800,970),(1000,1070) ,(1200,1150),(1400,1210),(1600,1250) )
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating industrial output to indicated food                 requirements 2 (IFPC1T#90.1).
    """
    return lookup(
        x,
        [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
        [230, 480, 690, 850, 970, 1070, 1150, 1210, 1250],
    )


def processing_loss():
    """
    Real Name: processing loss
    Original Eqn: 0.1
    Units: Dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    PROCESSING LOSS (PL#87.2)
    """
    return 0.1


def total_agricultural_investment():
    """
    Real Name: total agricultural investment
    Original Eqn: industrial output * fraction of industrial output allocated to agriculture
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    TOTAL AGRICULTURAL INVESTMENT (TAI#92)
    """
    return (
        industrial_output() * fraction_of_industrial_output_allocated_to_agriculture()
    )


def average_life_agricultural_inputs():
    """
    Real Name: average life agricultural inputs
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    AVERAGE LIFETIME OF AGRICULTURAL INPUTS (ALAI#100)
    """
    return 2


def agricultural_inputs():
    """
    Real Name: Agricultural Inputs
    Original Eqn: SMOOTH (current agricultural inputs, average life agricultural inputs )
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    AGRICULTURAL INPUTS (AI#99)
    """
    return _smooth_agricultural_inputs()


def agricultural_input_per_hectare():
    """
    Real Name: agricultural input per hectare
    Original Eqn: Agricultural Inputs * ( 1 - fraction of agricultural inputs for land maintenance ) / Arable Land
    Units: $/(year*hectare)
    Limits: (None, None)
    Type: component
    Subs: None

    AGRICULTURAL INPUTS PER HECTARE (AIPH#101)
    """
    return (
        agricultural_inputs()
        * (1 - fraction_of_agricultural_inputs_for_land_maintenance())
        / arable_land()
    )


def current_agricultural_inputs():
    """
    Real Name: current agricultural inputs
    Original Eqn: ACTIVE INITIAL( total agricultural investment * ( 1 - fraction of agricultural inputs allocated to land development) , 5e+09)
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    CURRENT AGRICULTURAL INPUTS (CAI#98).
    """
    return active_initial(
        __data["time"],
        lambda: total_agricultural_investment()
        * (1 - fraction_of_agricultural_inputs_allocated_to_land_development()),
        5e09,
    )


def perceived_food_ratio():
    """
    Real Name: Perceived Food Ratio
    Original Eqn: SMOOTH (food ratio, food shortage perception delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    PERCEIVED FOOD RATIO (PFR#128).
    """
    return _smooth_perceived_food_ratio()


def food_ratio():
    """
    Real Name: food ratio
    Original Eqn: ACTIVE INITIAL( food per capita / subsistence food per capita , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FOOD RATIO (FR#127)
    """
    return active_initial(
        __data["time"], lambda: food_per_capita() / subsistence_food_per_capita(), 1
    )


def food_shortage_perception_delay():
    """
    Real Name: food shortage perception delay
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    FOOD SHORTAGE PERCEPTION DELAY (FSPD#128.2)
    """
    return 2


def fraction_of_agricultural_inputs_for_land_maintenance():
    """
    Real Name: fraction of agricultural inputs for land maintenance
    Original Eqn: fraction of agricultural inputs for land maintenance table ( Perceived Food Ratio)
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF INPUTS ALLOCATED TO LAND MAINTENANCE                 (FALM#126).
    """
    return fraction_of_agricultural_inputs_for_land_maintenance_table(
        perceived_food_ratio()
    )


def fraction_of_agricultural_inputs_for_land_maintenance_table(x):
    """
    Real Name: fraction of agricultural inputs for land maintenance table
    Original Eqn: ( (0,0),(1,0.04),(2,0.07),(3,0.09),(4,0.1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    Table relating the perceived food ratio to the                fraction of input used for land maintenance                 (FALMT#126.1).
    """
    return lookup(x, [0, 1, 2, 3, 4], [0, 0.04, 0.07, 0.09, 0.1])


def subsistence_food_per_capita():
    """
    Real Name: subsistence food per capita
    Original Eqn: 230
    Units: Veg equiv kg/(Person*year)
    Limits: (None, None)
    Type: constant
    Subs: None

    Subsistence food per capita (SFPC#127.1).
    """
    return 230


_smooth_agricultural_inputs = Smooth(
    lambda: current_agricultural_inputs(),
    lambda: average_life_agricultural_inputs(),
    lambda: current_agricultural_inputs(),
    lambda: 1,
    "_smooth_agricultural_inputs",
)


_smooth_perceived_food_ratio = Smooth(
    lambda: food_ratio(),
    lambda: food_shortage_perception_delay(),
    lambda: food_ratio(),
    lambda: 1,
    "_smooth_perceived_food_ratio",
)
