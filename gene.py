import random
import string

goal = "HELLOWORLD"  # 目標の文字列
crossover_rate = 0.5  # 最も適応度の高い個体を選択する割合
mutation_rate = 0.8  # 突然変異を起こす確率


def get_fitness(gene):
    return sum(map(lambda c1, c2: c1 == c2, gene, goal))


def crossover(gene1, gene2):
    new_gene = ""
    for c1, c2 in zip(gene1, gene2):
        if random.random() > crossover_rate:  # 交叉
            new_gene += str(c1)
        else:
            new_gene += str(c2)
        if random.random() > mutation_rate:  # 突然変異
            new_gene = new_gene[:-1] + random.choice(string.ascii_uppercase)
    return new_gene


genes = ["X" * len(goal) for _ in range(10)]
generation = 0

print(generation, genes)
while max(map(get_fitness, genes)) != get_fitness(goal):
    generation += 1
    gene_with_fitness = [(gene, get_fitness(gene)) for gene in genes]
    ranking = sorted(gene_with_fitness, key=lambda x: x[1], reverse=True)
    first_gene = ranking[0][0]
    second_gene = ranking[1][0]
    genes = [crossover(first_gene, second_gene) for _ in range(len(genes))]
    print(generation, genes)
