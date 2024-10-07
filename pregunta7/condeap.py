import random
from deap import base, creator, tools, algorithms

# Definir la función objetivo
def eval_func(individual):
    x = int("".join(map(str, individual)), 2)
    return x**2 * x - 1,

# Configuración de DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Algoritmo Genético
def main():
    random.seed(64)
    pop = toolbox.population(n=10)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", lambda x: sum(v[0] for v in x) / len(x))
    stats.register("min", lambda x: min(v[0] for v in x))
    stats.register("max", lambda x: max(v[0] for v in x))

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=3, stats=stats, halloffame=hof, verbose=True)

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, hof = main()
    print("Mejor individuo:", hof[0])
