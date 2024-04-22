# HANYA PAKE FCTC, CROSSOVER DIGANTI CARANYA

import matplotlib.pyplot as plt
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


class GASchedule:
    population_size = None
    crossover_rate = None
    mutation_rate = None
    population = None
    generation_count = None
    machine = ["M1", "M2", "M3", "M4"]
    initial_size = None
    initial_product = {}
    elitism_rate = None

    def __init__(
        self,
        population_size,
        crossover_rate,
        mutation_rate,
        generation_count,
        elitism_rate,
    ):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generation_count = generation_count
        self.elitism_rate = elitism_rate

    def create_population(self, product_list):

        for product in product_list:
            if product in self.initial_product:
                self.initial_product[product] += 1
            else:
                self.initial_product[product] = 1

        self.population = []

        for n in range(self.population_size):
            chromosome = []
            for i in range(14):
                subchromosome = []
                for j in range(4):
                    subchromosome.append(product0)
                chromosome.append(subchromosome)
            initial_product = self.initial_product.copy()
            for i in range(14):
                for j in range(4):
                    if chromosome[i][j] == product0:
                        random_key = random.choice(list(initial_product.keys()))
                        while (
                            initial_product[random_key] == 0
                            and sum(initial_product.values()) != 0
                        ):
                            random_key = random.choice(list(initial_product.keys()))
                        if initial_product[random_key] > 0:
                            duration = random_key.duration
                            for k in range(0, duration):
                                if i + k < 14:
                                    chromosome[i + k][j] = random_key
                            initial_product[random_key] -= 1
            self.population.append(chromosome)
        self.initial_size = len(product_list)

    def print_population(self):
        for i in range(len(self.population)):
            print("Chromosome")
            for j in range(len(self.population[i])):
                for k in range(len(self.population[i][j])):
                    if isinstance(self.population[i][j][k], Product):
                        print(self.population[i][j][k].id, end=" ")
                    else:
                        print(self.population[i][j][k], end=" ")
                print()
            # print("FCMS:", self.fcms(self.population[i]))
            print("FCTC:", self.fctc(self.population[i]))
            # print("FCPQA:", self.fcpqa(self.population[i]))

            pop_dict = self.list_to_dict(self.population[i])
            pop_list = self.dict_to_list(self.list_to_dict(self.population[i]))

            for m in range(4):
                for product, count in pop_dict[m].items():
                    print(product.id, ",", count)
                print()

            for a in range(14):
                for b in range(4):
                    print(pop_list[a][b].id, end=" ")
                print()

    def print_fitness(self, chromosome):
        print("FCMS:", self.fcms(chromosome))
        print("FCTC:", self.fctc(chromosome))
        print("FCPQA:", self.fcpqa(chromosome))

    def selection(self, scores):
        selected_ix = random.randint(0, self.population_size - 1)
        random_range = []
        a = random.randint(0, self.population_size - 1)
        while a == selected_ix:
            a = random.randint(0, self.population_size - 1)
        b = random.randint(0, self.population_size - 1)
        while a == b or b == selected_ix:
            b = random.randint(0, self.population_size - 1)
        random_range.append(a)
        random_range.append(b)

        for ix in random_range:
            if scores[ix] > scores[selected_ix]:
                selected_ix = ix

        return self.population[selected_ix]

    def scores(self):
        total_score = list()
        for i in range(self.population_size):
            total_score.append(
                (8 * self.fcms(self.population[i]))
                + (8 * self.fctc(self.population[i]))
                + (self.fcpqa(self.population[i]))
            )

        return total_score

    def fcms(self, chromosome):
        score = 0
        zero_consecutive = [0, 0, 0, 0]
        for i in range(13):
            for j in range(4):
                current_item = chromosome[i][j]
                next_item = chromosome[i + 1][j]
                if current_item.id == "0" and next_item.id == "0":
                    zero_consecutive[j] += 1

        for i in zero_consecutive:
            if i >= 1:
                score += 0.25

        return score

    def list_to_dict(self, chromosome):
        list_of_dict = []
        M1 = {}
        i = 0
        while i < 14:
            if chromosome[i][0] != product0:
                product = chromosome[i][0]
                i = i + product.duration
                if product in M1:
                    M1[product] += 1
                else:
                    M1[product] = 1
            else:
                i += 1
        M2 = {}
        i = 0
        while i < 14:
            if chromosome[i][1] != product0:
                product = chromosome[i][1]
                i = i + product.duration
                if product in M2:
                    M2[product] += 1
                else:
                    M2[product] = 1
            else:
                i += 1
        M3 = {}
        i = 0
        while i < 14:
            if chromosome[i][2] != product0:
                product = chromosome[i][2]
                i = i + product.duration
                if product in M3:
                    M3[product] += 1
                else:
                    M3[product] = 1
            else:
                i += 1
        M4 = {}
        i = 0
        while i < 14:
            if chromosome[i][3] != product0:
                product = chromosome[i][3]
                i = i + product.duration
                if product in M4:
                    M4[product] += 1
                else:
                    M4[product] = 1
            else:
                i += 1
        list_of_dict.append(M1)
        list_of_dict.append(M2)
        list_of_dict.append(M3)
        list_of_dict.append(M4)

        return list_of_dict

    def dict_to_list(self, list_of_dict):
        chromosome = []
        for i in range(14):
            subchromosome = []
            for j in range(4):
                subchromosome.append(product0)
            chromosome.append(subchromosome)

        for i in range(4):
            a = 0
            for product, count in list_of_dict[i].items():
                duration = product.duration
                for j in range(count * duration):
                    if a < 14:
                        chromosome[a][i] = product
                        a += 1
        # i = 0
        # while i < 14:
        #     for j in range(4):
        #         product_machine_j = list_of_dict[j]
        #         for k in range(len(product_machine_j)):
        #             for l in range(list(product_machine_j.values())[k]):
        #                 if (i + l < 14):
        #                     chromosome[i+l][j] = list(product_machine_j.keys())[k]
        #             i = i + list(product_machine_j.values())[k] + 1

        return chromosome

    def fctc(self, chromosome):
        score = 0
        product_count = {}
        i_continue = [0, 0, 0, 0]
        for i in range(14):
            for j in range(4):
                if i_continue[j] <= i:
                    if chromosome[i][j] != product0 and chromosome[i][j].machine.count(
                        self.machine[j]
                    ):
                        valid = True
                        for k in range(chromosome[i][j].duration):
                            if i + k < 14:
                                if chromosome[i + k][j] != chromosome[i][j]:
                                    valid = False
                                    break
                        if valid:
                            if chromosome[i][j] not in product_count:
                                product_count[chromosome[i][j]] = 1
                            else:
                                product_count[chromosome[i][j]] += 1
                            i_continue[j] = i + k + 1

        for key in self.initial_product:
            if key in product_count:
                difference = abs(product_count[key] - self.initial_product[key])
            else:
                difference = self.initial_product[key]
            score += difference

        # for key, value in product_count.items():
        #     print(key.id + ": " + str(value), end = " ")
        # print()
        # for key, value in self.initial_product.items():
        #     print(key.id + ": " + str(value), end = " ")

        return 1 / (score + 1)

    def fcpqa(self, chromosome):

        initial_product = self.initial_product.copy()

        initial_product = {x: 0 for x in initial_product}

        score = 0

        i_continue = [0, 0, 0, 0]

        for i in range(14):
            for j in range(4):
                if i_continue[j] <= i:
                    if chromosome[i][j] != product0:
                        valid = True
                        for k in range(0, chromosome[i][j].duration):
                            if i + k < 14:
                                if chromosome[i][j] != chromosome[i + k][j]:
                                    valid = False
                                    break
                        if valid:
                            initial_product[chromosome[i][j]] += 1
                            i_continue[j] = i + k + 1

        for key in initial_product:
            difference = abs(self.initial_product[key] - initial_product[key])
            score += 1 / (difference + 1)

        return score / len(self.initial_product)

    def crossover(self, parent1, parent2, crossover_rate):
        p1 = self.list_to_dict(parent1)
        p2 = self.list_to_dict(parent2)

        randomize = random.random()
        if randomize >= crossover_rate:
            return [parent1.copy(), parent2.copy()]

        child1 = []
        child2 = []

        skip_outer = False

        for i in range(4):
            product_child1_machine_i = {}
            product_child2_machine_i = {}
            product_parent1_machine_i = p1[i]
            product_parent2_machine_i = p2[i]
            for j in range(
                max(len(product_parent1_machine_i), len(product_parent2_machine_i))
            ):
                # if(j < len(product_parent1_machine_i)):
                #     key1, value1 = list(product_parent1_machine_i.items())[j]
                #     total_child1 = 0
                #     for i in range(len(child1)):
                #         for product, count in child1[i].items():
                #             if(product == key1):
                #                 total_child1 += count
                #     if total_child1 == self.initial_product[key1]:
                #         product_child2_machine_i.update({key1: value1})
                #         skip_outer = True
                #     if skip_outer == False:
                #         total_child2 = 0
                #         for i in range(len(child2)):
                #             for product, count in child2[i].items():
                #                 if(product == key1):
                #                     total_child2 += count
                #         if total_child2 == self.initial_product[key1]:
                #             product_child1_machine_i.update({key1: value1})
                #             skip_outer = True
                # if skip_outer == False:
                #     if(j < len(product_parent2_machine_i)):
                #         key2, value2 = list(product_parent2_machine_i.items())[j]
                #         total_child1 = 0
                #         for i in range(len(child1)):
                #             for product, count in child1[i].items():
                #                 if(product == key2):
                #                     total_child1 += count
                #         if total_child1 == self.initial_product[key2]:
                #             product_child2_machine_i.update({key2: value2})
                #             skip_outer = True
                #         if skip_outer == False:
                #             total_child2 = 0
                #             for i in range(len(child2)):
                #                 for product, count in child2[i].items():
                #                     if(product == key2):
                #                         total_child2 += count
                #             if total_child2 == self.initial_product[key2]:
                #                 product_child2_machine_i.update({key2: value2})
                #                 skip_outer = True

                # if(skip_outer):
                #     continue

                randomize = random.random()
                if randomize < 0.5:
                    if j >= len(product_parent1_machine_i):

                        key2, value2 = list(product_parent2_machine_i.items())[j]
                        product_child1_machine_i.update({key2: value2})
                        continue
                    if j >= len(product_parent2_machine_i):
                        key1, value1 = list(product_parent1_machine_i.items())[j]
                        product_child2_machine_i.update({key1: value1})
                        continue
                    key1, value1 = list(product_parent1_machine_i.items())[j]
                    product_child1_machine_i.update({key1: value1})
                    key2, value2 = list(product_parent2_machine_i.items())[j]
                    product_child2_machine_i.update({key2: value2})
                else:
                    if j >= len(product_parent1_machine_i):
                        key2, value2 = list(product_parent2_machine_i.items())[j]
                        product_child2_machine_i.update({key2: value2})
                        continue
                    if j >= len(product_parent2_machine_i):
                        key1, value1 = list(product_parent1_machine_i.items())[j]
                        product_child2_machine_i.update({key1: value1})
                        continue
                    key2, value2 = list(product_parent2_machine_i.items())[j]
                    product_child1_machine_i.update({key2: value2})

                    key1, value1 = list(product_parent1_machine_i.items())[j]
                    product_child2_machine_i.update({key1: value1})

            child1.append(product_child1_machine_i)
            child2.append(product_child2_machine_i)

        return [self.dict_to_list(child1), self.dict_to_list(child2)]

    def run(self, input):
        self.create_population(input)
        best = self.population[0]
        best_eval = self.scores()[0]
        generation_scores = []
        genCounts = 0

        for gen in range(0, self.generation_count):
            scores = self.scores()
            best_pop = scores[0]
            genCounts += 1

            for i in range(self.population_size):
                if scores[i] > best_pop:
                    best_pop = scores[i]

                if scores[i] > best_eval:
                    best = self.population[i]
                    best_eval = scores[i]
                    print("Gen " + str(gen) + ", new best:")
                    for row in range(14):
                        for column in range(4):
                            print(best[row][column].id, end=" ")
                        print()
                    print("Fitness =", best_eval)
                    self.print_fitness(best)

            new_population = []

            elitism_count = self.elitism_rate * self.population_size

            # Create a list of tuples containing the index and value
            indexed_numbers = list(enumerate(scores))

            # Sort the list of tuples by the value (the second item in the tuple)
            indexed_numbers.sort(key=lambda x: x[1])

            # Extract the original indices of the sorted list
            sorted_indices = [index for index, value in indexed_numbers]

            for i in range(int(elitism_count)):
                new_population.append(self.population[sorted_indices[i]])

            selected = [
                self.selection(scores) for _ in range(int(self.population_size))
            ]
            children = list()
            for i in range(0, int(self.population_size - elitism_count), 2):
                p1, p2 = selected[i], selected[i + 1]
                for c in self.crossover(p1, p2, self.crossover_rate):
                    self.mutation(c, self.mutation_rate)
                    children.append(c)
            new_population.extend(children)
            self.population = new_population

            gen += 1
            generation_scores.append(best_pop)

        # Plot skor per generasi di luar loop generasi
        plt.plot(range(1, genCounts + 1), generation_scores)
        plt.xlabel("Generation")
        plt.ylabel("Score")
        plt.title("Generation vs. Score")
        plt.grid(True)
        plt.show()
        return [best, best_eval]

    def mutation(self, chromosome, mutation_rate):
        p1 = self.list_to_dict(chromosome)

        temp = {i: {} for i in range(4)}

        for i in range(4):
            product_parent1_machine_i = p1[i]

            if random.random() < mutation_rate:
                items = list(product_parent1_machine_i.items())
                random.shuffle(items)
                hasil_shuffle = {key: value for key, value in items}
                new_hasil_shuffle = {}
                for product, count in hasil_shuffle.items():
                    new_hasil_shuffle[
                        random.choice(list(self.initial_product.keys()))
                    ] = 1
                    new_hasil_shuffle[product] = count - 1

                temp[i] = new_hasil_shuffle
            else:
                temp[i] = product_parent1_machine_i

            chromosome = self.dict_to_list(temp)
            if self.fcms(chromosome) < 1:
                for i in range(12, 14):
                    for j in range(4):
                        chromosome[i][j] = product0

        return chromosome

    # def mutation(self, chromosome, mutation_rate):
    #     for i in range(14):
    #         for j in range(4):
    #             if random.random() < mutation_rate:
    #                 random_zero = random.random()
    #                 if self.fcms(chromosome) < 1 and random_zero < 0.3:
    #                     chromosome[i][j] = product0
    #                 else:
    #                     chromosome[i][j] = random.choice(list(self.initial_product.keys()))
    #     return chromosome


sched = GASchedule(1000, 0.8, 0.8, 300, 0.1)

product0 = Product("0", 2, 0, ["M1", "M2", "M3", "M4"])
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
product11 = Product("B11", 2, 175000, ["M3"])
product12 = Product("B12", 3, 125000, ["M3"])

best = sched.run(
    [
        product1,
        product2,
        product3,
        product4,
        product5,
        product6,
        product7,
        product8,
        product9,
        product10,
        product11,
        product12,
        product1,
        product2,
        product3,
        product4,
    ]
)


# sched.print_population()
# sched.create_population(
#     [
#         product1,
#         product2,
#         product3,
#         product4,
#         product5,
#         product6,
#         product7,
#         product8,
#         product9,
#         product10,
#         product11,
#         product12,
#         product1,
#         product2,
#         product3,
#         product4,
#         product5,
#         product6,
#         product7,
#         product8
#     ]
# )
# sched.print_population()
