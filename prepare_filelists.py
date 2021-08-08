import os
import sys
import argparse
from pprint import pprint
import random
def split_dataset(samples, split_ratio=(80, 10, 10)):
    
    train_size, test_size, val_size = [ int( i/100*len(samples) ) for i in split_ratio ]

    random.shuffle(samples)
    offset = 0
    train = samples[offset:offset+train_size]

    offset += train_size
    test = samples[offset:offset+test_size]
    
    offset += test_size
    val = samples[offset:]

    return train, test, val
        

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input',
                        default='metadata.csv',
                        help='path to metadata.csv')
    
    parser.add_argument('-o', '--output',
                        default='indictts_filelists',
                        help='output file path')
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='verbose')
    
    args = parser.parse_args()

    pprint(args)

    print('creating {} dir...'.format(args.output))
    os.makedirs(args.output, exist_ok=True)

    samples = []
    dirname = os.path.dirname(args.input)
    for line in open(args.input):
        line = line.strip()
        id_, line1, line2 = line.split('|')
        
        id_ = '{}/wav/{}.wav'.format(dirname, id_)
        
        samples.append((id_, line1, line2))


    print('total number of samples: {}'.format(len(samples)), file=sys.stderr)
    train, test, val = split_dataset(samples, (80, 10, 10))
    assert len(samples) == len(train) + len(test) + len(val)

    
    pattern = args.output + '/text_{}_filelist.txt'
    print('output filelists pattern: {}'.format(pattern), file=sys.stderr)
    for fname, dset in zip(['train', 'test', 'val'],
                          [ train,   test,   val]):

        print('total number of samples: {}'.format(len(dset)), file=sys.stderr)
        with open(pattern.format(fname), 'w') as f:
            for sample in dset:
                print('|'.join(sample), file=f)
