import random

# Genetic Algorithm Configuration
POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwcyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Pratik Sahare"
TARGET_LEN = len(TARGET)
MUTATION_RATE = 0.1

# Function to create a random chromosome (gnome)
def create_gnome():
    return [random.choice(GENES) for _ in range(TARGET_LEN)]

# Function to calculate the fitness score of a chromosome
# Fitness score is the number of characters different from the target string
def calculate_fitness(chromosome):
    fitness = 0
    for c, t in zip(chromosome, TARGET):
        if c != t:
            fitness += 1
    return fitness

# Function to mate (crossover) two parents and produce an offspring
def mate(parent1, parent2):
    child_chromosome = []
    for gp1, gp2 in zip(parent1, parent2):
        prob = random.random()
        
        # With a probability, choose genes from parents or mutate
        if prob < 0.45:
            child_chromosome.append(gp1)
        elif prob < 0.90:
            child_chromosome.append(gp2)
        else:
            child_chromosome.append(random.choice(GENES))  # Mutate gene
            
    return child_chromosome

# Function to perform mutation on a chromosome with a set mutation rate
def mutate(chromosome):
    for i in range(TARGET_LEN):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.choice(GENES)
    return chromosome

# Main genetic algorithm execution
def genetic_algorithm():
    # Initial population (random chromosomes)
    population = [create_gnome() for _ in range(POPULATION_SIZE)]
    generation = 1
    found = False

    while not found:
        # Calculate fitness for each chromosome and sort by fitness (lower is better)
        population = sorted(population, key=lambda chromo: calculate_fitness(chromo))

        # Print best result in the current generation
        best_chromosome = population[0]
        best_fitness = calculate_fitness(best_chromosome)
        print(f"Generation: {generation}\tString: {''.join(best_chromosome)}\tFitness: {best_fitness}")

        # If the best chromosome's fitness is 0, we have found the target
        if best_fitness == 0:
            found = True
            break

        # New generation creation
        new_generation = []

        # Elitism: retain the top 10% of the population (best chromosomes)
        s = int(0.1 * POPULATION_SIZE)
        new_generation.extend(population[:s])

        # For the remaining 90%, perform mating (crossover) and mutation
        s = int(0.9 * POPULATION_SIZE)
        for _ in range(s):
            parent1 = random.choice(population[:50])  # Select from top 50 chromosomes
            parent2 = random.choice(population[:50])
            child = mate(parent1, parent2)
            new_generation.append(mutate(child))

        # Update population and increase generation count
        population = new_generation
        generation += 1

# Run the genetic algorithm
genetic_algorithm()
