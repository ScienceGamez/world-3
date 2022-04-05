"""
Python model 'model.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.functions import if_then_else, lookup, log, active_initial
from pysd.py_backend.statefuls import Delay, Integ, Smooth
from pysd.py_backend.utils import load_modules, load_model_data

__pysd_version__ = "2.2.0"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_namespace, _subscript_dict, _dependencies, _modules = load_model_data(_root, "model")

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 1900,
    "final_time": lambda: 2100,
    "time_step": lambda: 0.5,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2100
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The time at which simulation stops.
    """
    return __data["time"].final_time()


def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 1900
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The time at which the simulation begins.
    """
    return __data["time"].initial_time()


def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None

    The frequency with which results are saved.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.5
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None

    The time step for computing the model
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################

# load modules from modules_model directory
exec(load_modules("modules_model", _modules, _root, []))


def gdp_pc_unit():
    """
    Real Name: GDP pc unit
    Original Eqn: 1
    Units: $/Person/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def unit_agricultural_input():
    """
    Real Name: unit agricultural input
    Original Eqn: 1
    Units: $/hectare/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def unit_population():
    """
    Real Name: unit population
    Original Eqn: 1
    Units: Person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def one_year():
    """
    Real Name: one year
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def land_fr_cult():
    """
    Real Name: land fr cult
    Original Eqn: Arable Land / potentially arable land total
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Land fraction under cultivarion (LFC#84).
    """
    return arable_land() / potentially_arable_land_total()


def birth_rate():
    """
    Real Name: birth rate
    Original Eqn: THOUSAND * births / population
    Units: C/year
    Limits: (None, None)
    Type: component
    Subs: None

    The crude birth rate measured in people per thousand                 people per year (CBR#31).
    """
    return thousand() * births() / population()


def thousand():
    """
    Real Name: THOUSAND
    Original Eqn: 1000
    Units: C
    Limits: (None, None)
    Type: constant
    Subs: None

    Units converted for /1000 rates (--).
    """
    return 1000


def death_rate():
    """
    Real Name: death rate
    Original Eqn: THOUSAND * deaths / population
    Units: C/year
    Limits: (None, None)
    Type: component
    Subs: None

    CRUDE DEATH RATE (CDR#18)
    """
    return thousand() * deaths() / population()


def consumed_industrial_output():
    """
    Real Name: consumed industrial output
    Original Eqn: industrial output * fraction of industrial output allocated to consumption
    Units: $/year
    Limits: (None, None)
    Type: component
    Subs: None

    Consumed industrial output (CIO#--).
    """
    return (
        industrial_output() * fraction_of_industrial_output_allocated_to_consumption()
    )


def consumed_industrial_output_per_capita():
    """
    Real Name: consumed industrial output per capita
    Original Eqn: consumed industrial output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component
    Subs: None

    Consumption Industrial Output per Capita (CIOPC#--)
    """
    return consumed_industrial_output() / population()


def fraction_of_output_in_agriculture():
    """
    Real Name: fraction of output in agriculture
    Original Eqn: ( PRICE OF FOOD * food ) / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF OUTPUT IN AGRICULTURE (FAO#147)
    """
    return (price_of_food() * food()) / (
        price_of_food() * food() + service_output() + industrial_output()
    )


def fraction_of_output_in_industry():
    """
    Real Name: fraction of output in industry
    Original Eqn: industrial output / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Fraction of output that is industrial output                 (FOI#148).
    """
    return industrial_output() / (
        price_of_food() * food() + service_output() + industrial_output()
    )


def fraction_of_output_in_services():
    """
    Real Name: fraction of output in services
    Original Eqn: service output / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    FRACTION OF OUTPUT IN SERVICES (FOS#149).
    """
    return service_output() / (
        price_of_food() * food() + service_output() + industrial_output()
    )


def price_of_food():
    """
    Real Name: PRICE OF FOOD
    Original Eqn: 0.22
    Units: $/Veg equiv kg
    Limits: (None, None)
    Type: constant
    Subs: None

    The price of food used as a basis for comparing                 agricultural and industrial output. (--).
    """
    return 0.22


def resource_use_intensity():
    """
    Real Name: resource use intensity
    Original Eqn: resource usage rate / industrial output
    Units: Resource units/$
    Limits: (None, None)
    Type: component
    Subs: None

    ADAPTIVE TECHNOLOGICAL CONTROL CARDS nonrenewable                 resource usage intensity (RESINT#--)
    """
    return resource_usage_rate() / industrial_output()
