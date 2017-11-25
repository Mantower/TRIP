from nlpComponent import PyNLP
import sys

pyNLP = PyNLP('9000')
nlp_input = sys.argv[1]
print(nlp_input)

pyNLP.eval_input(nlp_input)
