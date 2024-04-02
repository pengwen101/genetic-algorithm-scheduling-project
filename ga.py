import random

class Product:
    id = None
    duration = None
    price = None
    machine = None

    def __init__(self, id, duration):
        self.id = id
        self.duration = duration


class GASchedule:
    population_size = None
    crossover_rate = None
    mutation_rate = None
    population = None
    generation = None


    def __init__(self, population_size, crossover_rate, mutation_rate):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
    
    def create_population(self, product_list):
        self.population = []
        for i in range(self.population_size):
            chromosome = []
            chosen = []
            for j in range(14):
                subchromosome = []
                for k in range(4):
                    if(len(chosen) == len(product_list)):
                        subchromosome.append("0")
                    else:
                        chosen_index = random.choice(range(len(product_list)))
                        while(chosen.count(chosen_index)):
                            chosen_index = random.choice(range(len(product_list)))
                        subchromosome.append(product_list[chosen_index].id)
                        chosen.append(chosen_index)
                chromosome.append(subchromosome)
            self.population.append(chromosome)
    
    def print_population(self):
        for i in range(len(self.population)):
            print("Chromosome")
            for j in range(len(self.population[i])):
                for k in range(len(self.population[i][j])):
                    print(self.population[i][j][k], end = " ")
                print()
            print()
    
    # def fitness_value(chromosome):
    #     #Maintenance schedule
    #     fcms = None
    #     for i in range(4):
    #         for j in range(14):
    #             product_id = chromosome[i][j]

            

        #Efficiency per machine
        #evaluate through every machine, count the number of products (right ones)
        #rata2 differences per machine paling small

        #

    
    # def select_best(self):

        
    
    # def genetic_algorithm(self, product_list):
    #     for i in range(self.generation):
    #         self.create_population(product_list)
    #         selected_chromosome = self.select_best()

sched = GASchedule(50, 0.1,0.1)

product0 = Product("0", 0)
product1 = Product("B1", 1)
product2 = Product("B2", 2)
product3 = Product("B3", 3)
product4 = Product("B4", 2)
product5 = Product("B5", 1)
product6 = Product("B6", 4)
product7 = Product("B7", 2)
product8 = Product("B8", 1)
product9 = Product("B9", 3)
product10 = Product("B10", 2)
product11 = Product("B11", 4)
product12 = Product("B12", 5)

sched.create_population([product0, product1, product2, product3, product4, product1, product2, product3, product4, product1, product2, product3, product4, product1, product2, product3, product4])

sched.print_population()


