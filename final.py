from inputs.input_formating import *
from inputs.forest_input_formating import *
from utility.constants import *
from utility.file_loader import *


def final_function(data_i) :
    sequences = parse_sequences(data_i[1])
    processes = parse_processes(data_i[0])
    tree, source = generate_subprocess_tre(processes)
    forest = generate_API_behavior_graph(sequences)
    return forest_input(tree, source, forest)

def to_be_encoded(data_i):
    sequences = parse_sequences(data_i[1])
    forest = generate_API_behavior_graph(sequences)
    vector = forest_api_frequency(forest)
    return vector

def return_matrix(data_i):
    sequences = parse_sequences(data_i[1])
    forest = generate_API_behavior_graph(sequences)
    matricex = forest_romain_matrix(forest)
    return matricex
