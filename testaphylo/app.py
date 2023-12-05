from aphylogeo.alignement import AlignSequences
from aphylogeo.params import Params
from aphylogeo import utils
from aphylogeo.genetic_trees import GeneticTrees

Params.load_from_file(".\\params_tutorial.yaml")
sequenceFile = utils.loadSequenceFile(Params.reference_gene_filepath)

print(f"Sequence file loaded: {sequenceFile}")