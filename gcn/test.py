# from __future__ import division
# from __future__ import print_function

# import time
# import tensorflow as tf

# from gcn.utils import *
# from gcn.models import GCN, MLP
from utils import load_data

# Set random seed
# seed = 123
# np.random.seed(seed)
# tf.set_random_seed(seed)

# Settings
# flags = tf.app.flags
# FLAGS = flags.FLAGS
# flags.DEFINE_string('dataset', 'cora', 'Dataset string.')  # 'cora', 'citeseer', 'pubmed'
# flags.DEFINE_string('model', 'gcn', 'Model string.')  # 'gcn', 'gcn_cheby', 'dense'
# flags.DEFINE_float('learning_rate', 0.01, 'Initial learning rate.')
# flags.DEFINE_integer('epochs', 200, 'Number of epochs to train.')
# flags.DEFINE_integer('hidden1', 16, 'Number of units in hidden layer 1.')
# flags.DEFINE_float('dropout', 0.5, 'Dropout rate (1 - keep probability).')
# flags.DEFINE_float('weight_decay', 5e-4, 'Weight for L2 loss on embedding matrix.')
# flags.DEFINE_integer('early_stopping', 10, 'Tolerance for early stopping (# of epochs).')
# flags.DEFINE_integer('max_degree', 3, 'Maximum Chebyshev polynomial degree.')

# Load data
adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = load_data('cora')
# print(test_mask[:100])

# lst = [[1, 2], [3, 4], [5, 6]]
# idx = [0, 1]
# print(lst[idx, :])
