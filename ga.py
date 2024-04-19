import random

class Product:
    id = None
    duration = None
    price = None
    machine = None

    def __init__(self, id, duration, price, machine):
        self.id = id
        self.duration = duration
        self.price = price
        self.machine = machine
     
    def __str__(self):
        return self.id


class GASchedule:
    population_size = None
    crossover_rate = None
    mutation_rate = None
    population = None
    generation_count = None
    machine = ["M1", "M2", "M3", "M4"]
    initial_size = None
    initial_product = {}


    def __init__(self, population_size, crossover_rate, mutation_rate, generation_count):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generation_count = generation_count
    
    def create_population(self, product_list):
        for product in product_list:
            if (product.id in self.initial_product):
                self.initial_product[product.id] += 1
            else:
                self.initial_product[product.id] = 1
        self.population = []
        for i in range(self.population_size):
            chromosome = []
            chosen = []
            duration = [0,0,0,0]
            for j in range(14):
                subchromosome = []
                for k in range(4):
                    if(j!=0 and duration[k]!=1 and duration[k] != 0):
                        subchromosome.append(chromosome[j-1][k])
                        duration[k] -= 1
                    else:
                        if(len(chosen) == len(product_list)):
                            subchromosome.append(product0)
                        else:
                            chosen_index = random.choice(range(len(product_list)))
                            while(chosen.count(chosen_index)):
                                chosen_index = random.choice(range(len(product_list)))
                            subchromosome.append(product_list[chosen_index])
                            chosen.append(chosen_index)
                            duration[k] = product_list[chosen_index].duration
                chromosome.append(subchromosome)
            self.population.append(chromosome)
        self.initial_size = len(product_list)-1

    
    def print_population(self):
        for i in range(len(self.population)):
            print("Chromosome")
            for j in range(len(self.population[i])):
                for k in range(len(self.population[i][j])):
                    print(self.population[i][j][k].id, end = " ")
                print()
            print("FCMS:", self.fcms(self.population[i]))
            print("FCPD:", self.fcpd(self.population[i]))
            print("FCPQA:", self.fcpqa(self.population[i]))

    def selection(self, scores):
        selected_ix = random.randint(0, self.population_size-1)
        for ix in random.randint(0, self.population_size-1, 2):
            if scores[ix] > scores[selected_ix]:
                selected_ix = ix
        
        return(self.population[selected_ix])

    def scores(self):
        total_score = list()
        for i in range (self.population_size):
            total_score[i] = self.fcms(self.population[i]) + self.fcpd(self.population[i]) + self.fcms(self.population[i]) + self.fcfwe(self.population[i]) + self.fcr(self.population[i])
        
        return (total_score)
    
    
    
    def fcms(self,chromosome):
        zero_count = [0,0,0,0]
        fcms = 0
        for i in range(14):
            for j in range(4):
                if (chromosome[i][j].id == "0"):
                    if(zero_count[j] == 2):
                        continue
                    if(i != 0 and chromosome[i-1][j].id == "0"):
                        zero_count[j] += 1
                    else:
                        zero_count[j] == 1
        for i in zero_count:
            if(zero_count[i] == 2):
                fcms+=0.25
        return fcms

    def fcpd(self, chromosome):
        duration = [0,0,0,0]
        score = 0
        for i in range(14):
            for j in range(4):
                if(chromosome[i][j].machine.count(self.machine[j])):
                    if(i != 0 and chromosome[i-1][j] == chromosome[i][j] and duration[j] != 1):
                        duration[j] -= 1
                    else:
                        duration[j] = chromosome[i][j].duration
                    if(duration[j] == 1):
                        score+=1
        #duration = [3, 0, 0, 0]     
        return score/self.initial_size
    
    def fcpqa(self, chromosome):
        duration = [0,0,0,0]
        initial_product = self.initial_product.copy()

        score = 0
        for i in range(14):
            for j in range(4):
                    if(i != 0 and chromosome[i-1][j] == chromosome[i][j] and duration[j] != 1):
                        duration[j] -= 1
                    else:
                        duration[j] = chromosome[i][j].duration
                    if(duration[j] == 1):
                        initial_product[chromosome[i][j].id] -=1
        
        total_count = 0
        for key in self.initial_product:
            difference = self.initial_product[key] - initial_product[key]
            total_count += self.initial_product[key]
            score += difference

        return(score/(total_count-1))


sched = GASchedule(100, 0.1,0.1)

product0 = Product("0", 0, 0, ["M1", "M2", "M3", "M4"])
product1 = Product("B1", 1, 150000, ["M1", "M3"])
product2 = Product("B2", 2, 200000, ["M1", "M3"])
product3 = Product("B3", 3, 220000, ["M1", "M3"])
product4 = Product("B4", 2, 300000, ["M1", "M4"])
product5 = Product("B5", 1, 430000, ["M1", "M4"])
product6 = Product("B6", 4, 345000, ["M2", "M4"])
product7 = Product("B7", 2, 150000, ["M2", "M4"])
product8 = Product("B8", 1, 400000, ["M2", "M4"])
product9 = Product("B9", 3, 250000, ["M2"])
product10 = Product("B10", 2, 300000, ["M2"])
product11 = Product("B11", 4, 175000, ["M3"])
product12 = Product("B12", 5, 125000, ["M3"])

sched.create_population([product0, product1, product2, product3, product4, product1, product2, product3, product4, product1, product2, product3, product4, product1, product2, product3, product4])

sched.print_population()




