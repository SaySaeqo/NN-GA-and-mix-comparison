from singleton.singleton import Singleton

MIN = 0
MAX = 1
PROBE_NUMBER = 100

DELTA_MUTATION = 0.01
ALGORITHMS_NUMBER = 4

MODIFY_WEIGHT = 0
MODIFY_BIAS = 1
CALC_NEURON = 2

INPUT = 0
OUTPUT = 1
MAX_GENERATIONS = MAX_ITERATIONS = 200  # ?? nie używam już


@Singleton
class NConst:
    MAX_GENERATIONS = 10
    POPULATION_SIZE = 8
    MUTATION_CHANCE = 0.9
    MUTATION_RATE = 0.2
    BATCH_SIZE = 10


@Singleton
class GConst:
    MAX_ITERATIONS = 200
    BATCH_SIZE = 10
