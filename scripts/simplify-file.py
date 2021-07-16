import argparse

from muss.simplify import ALLOWED_MODEL_NAMES, simplify_sentences
from muss.utils.helpers import read_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simplify a file line by line.')
    parser.add_argument('filepath', type=str, help='File containing the source sentences, one sentence per line.')
    parser.add_argument(
        '--model-name',
        type=str,
        default=ALLOWED_MODEL_NAMES[0],
        choices=ALLOWED_MODEL_NAMES,
        help=f'Model name to generate from. Models selected with the highest validation SARI score.',
    )
    args = parser.parse_args()
    source_sentences = read_lines(args.filepath)
    pred_sentences = simplify_sentences(source_sentences, model_name=args.model_name)
    outfile = open('content/en_simp_inf.txt','w')
    for c, s in zip(source_sentences, pred_sentences):
        outfile.write('%s \n' % s)
