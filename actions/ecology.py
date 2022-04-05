from pysimgame.actions import Policy, change_constant, change_method


def tech_reduced_pollution(model):
    return model.persistent_pollution_generation_factor_2()


def ecological_technology_research(model):
    return (
        model.persistent_pollution_technology()
        * model.persistent_pollution_technology_change_multiplier()
    )


def ecological_ressource_extraction(model):
    return (
        model.resource_conservation_technology()
        * model.resource_technology_change_rate_multiplier()
    )


def ecological_ressource_use(model):
    return model.resource_use_fact_2()


def lower_food_need(model):
    return model.indicated_food_per_capita_2()


def ecological_indus_output_for_agr(model):
    return model.fraction_of_industrial_output_allocated_to_agriculture_2()


def land_preservation_technology(model):
    return (
        model.land_yield_technology()
        * model.land_yield_technology_change_rate_multiplier()
    )


def land_yield_from_tech(model):
    return model.land_yield_factor_2()


def reduced_air_pollution(model):
    return model.land_yield_multiplier_from_air_pollution_2()


# Global variable
_land_life_policy_implementation_time = None


def protected_land_life(model):
    global _land_life_policy_implementation_time
    if _land_life_policy_implementation_time is None:
        # First step that this is activated
        _land_life_policy_implementation_time = model.time()

    years_since_accepted = (
        0.95 ** (model.time() - _land_life_policy_implementation_time)
        / model.one_year()
    )

    return (
        years_since_accepted * model.land_life_multiplier_from_land_yield_1()
        + (
            1
            - years_since_accepted
            * model.land_life_multiplier_from_land_yield_2()
        )
    )


def industrial_equilibrium(model):
    return (
        model.fraction_of_industrial_output_allocated_to_consumption_variable()
    )

Policy(
    name="Birth Control",
    modifiers=[
        change_constant(
            "fertility_control_effectiveness",
            1.0,
        ),
        change_constant(  # Controlled family size
            "desired_completed_family_size",
            2.0,
        ),
        change_method(  # Controlled births
            "births",
            lambda model: model.deaths(),
        ),
    ]
)

Policy(
    name="Reduce Goods Consumption",
    # No idea if I am doing things right there
    modifiers=[
        change_method(
            "fraction_of_industrial_capital_allocated_to_obtaining_resources",
            lambda model: model.fraction_of_capital_allocated_to_obtaining_resources_2(),
        ),
        change_method(
            "resource_use_factor",
            ecological_ressource_use,
        ),
        change_method(
            "fraction_of_industrial_output_allocated_to_consumption",
            industrial_equilibrium,
        ),
    ]
)


Policy(
    name="Ecological world (ALL POLICIES)",
    modifiers=[
        change_constant(
            "fertility_control_effectiveness",
            1.0,
        ),
        change_constant(  # Controlled family size
            "desired_completed_family_size",
            2.0,
        ),
        change_method(  # Controlled births
            "births",
            lambda model: model.deaths(),
        ),
        change_method(
            "persistent_pollution_generation_factor",
            tech_reduced_pollution,
        ),
        change_method(
            "persistent_pollution_technology_change_rate",
            ecological_technology_research,
        ),
        change_method(
            "resource_technology_change_rate",
            ecological_ressource_extraction,
        ),
        change_method(
            "fraction_of_industrial_capital_allocated_to_obtaining_resources",
            lambda model: model.fraction_of_capital_allocated_to_obtaining_resources_2(),
        ),
        change_method(
            "resource_use_factor",
            ecological_ressource_use,
        ),
        change_method(
            "indicated_food_per_capita",
            lower_food_need,
        ),
        change_method(
            "fraction_of_industrial_output_allocated_to_agriculture",
            ecological_indus_output_for_agr,
        ),
        change_constant(
            "average_life_agricultural_inputs",
            2.0,
        ),
        change_method(
            "land_yield_technology_change_rate",
            land_preservation_technology,
        ),
        change_method(
            "land_yield_multiplier_from_technology", land_yield_from_tech
        ),
        change_method(
            "land_yield_multiplier_from_air_pollution", reduced_air_pollution
        ),
        change_method(
            "land_life_multiplier_from_land_yield", protected_land_life
        ),
        change_constant(  # lower_consumming_goods_usage
            "fraction_of_industrial_output_allocated_to_consumption", 0.43
        ),
        change_constant(  # recycling induustrial stuff
            "average_life_of_industrial_capital", 14
        ),
        change_constant("average_life_of_service_capital", 20),
        change_method(
            "industrial_capital_output_ratio",
            lambda model: model.industrial_capital_output_ratio_2(),
        ),
        change_method(
            "indicated_services_output_per_capita",
            lambda model: model.indicated_services_output_per_capita_2(),
        ),
        change_method(
            "fraction_of_industrial_output_allocated_to_services",
            lambda model: model.fraction_of_industrial_output_allocated_to_services_2(),
        ),
        change_method(
            "fraction_of_industrial_output_allocated_to_consumption",
            industrial_equilibrium,
        ),
        change_constant("service_capital_output_ratio", 1.0),
    ],
)
