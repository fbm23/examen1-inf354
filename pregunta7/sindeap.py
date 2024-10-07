import random

# Definir la función objetivo
def eval_func(x):
    return x**2 * x - 1

# Crear la población inicial
def create_population(size, chrom_length):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 1) for _ in range(chrom_length)]
        population.append(individual)
    return population

# Convertir binario a decimal
def bin_to_dec(binary):
    return int("".join(map(str, binary)), 2)

# Selección
def select(population, fitnesses):
    selected = random.choices(population, weights=fitnesses, k=len(population))
    return selected

# Cruce
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutación
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

# Algoritmo Genético
def genetic_algorithm(pop_size, chrom_length, generations, mutation_rate):
    population = create_population(pop_size, chrom_length)
    for gen in range(generations):
        fitnesses = [eval_func(bin_to_dec(ind)) for ind in population]
        population = select(population, fitnesses)
        next_population = []
        for i in range(0, len(population), 2):
            parent1, parent2 = population[i], population[i+1]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_population.extend([child1, child2])
        population = next_population
        best_individual = max(population, key=lambda ind: eval_func(bin_to_dec(ind)))
        print(f"Generación {gen+1}: Mejor individuo = {best_individual}, Valor = {eval_func(bin_to_dec(best_individual))}")

# Parámetros
pop_size = 10
chrom_length = 5
generations = 3
mutation_rate = 0.1

genetic_algorithm(pop_size, chrom_length, generations, mutation_rate)
