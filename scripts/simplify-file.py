from muss.simplify import ALLOWED_MODEL_NAMES, simplify_sentences
from muss.utils.helpers import read_lines

source_sentences = read_lines('en_comp.txt')
pred_sentences = simplify_sentences(source_sentences, model_name=' muss_en_mined')
outfile = open('content/en_simp_inf.txt','w')
for c, s in zip(source_sentences, pred_sentences):
    outfile.write('%s \n' % s)