from __future__ import print_function
import numpy as np
import tensorflow as tf


class FizzBuzzModel:
    def __init__(self, learn_rate=0.1, num_digits=10, num_hidden=100,
                       num_epochs=10000, batch_size=128, verbose=True):
        self.learn_rate = learn_rate
        self.num_digits = num_digits
        self.num_hidden = num_hidden
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.verbose = verbose

    @staticmethod
    def binary_encode(i, num_digits):
        return np.array([i >> digit & 1 for digit in range(num_digits)])

    @staticmethod
    def fizz_buzz_encode(i):
        if i % 15 == 0:
            return np.array([0, 1, 1])
        elif i % 5 == 0:
            return np.array([0, 0, 1])
        elif i % 3 == 0:
            return np.array([0, 1, 0])
        else:
            return np.array([1, 0, 0])

    @staticmethod
    def init_weights(shape):
        return tf.Variable(tf.random_normal(shape, stddev=0.01))

    @staticmethod
    def init_bias(shape):
        return tf.Variable(tf.constant(0.001, shape=shape))

    @staticmethod
    def model(data, weights_h, bias_h, weights_o, bias_o):
        hidden = tf.nn.relu6(tf.matmul(data, weights_h) + bias_h)
        return tf.matmul(hidden, weights_o) + bias_o

    @staticmethod
    def fizz_buzz(i, prediction):
        return ''.join(np.where(prediction, [str(i), "fizz", "buzz"], ['', '', '']))

    def solve(self):
        train_range = range(101, 2 ** self.num_digits)
        train_data = np.array([self.binary_encode(i, self.num_digits) for i in train_range])
        train_labels = np.array([self.fizz_buzz_encode(i) for i in train_range])

        data = tf.placeholder("float", [None, self.num_digits])
        labels = tf.placeholder("float", [None, 3])

        weights_h = self.init_weights([self.num_digits, self.num_hidden])
        bias_h = self.init_bias([self.num_hidden])
        weights_o = self.init_weights([self.num_hidden, 3])
        bias_o = self.init_bias([3])

        logits = self.model(data, weights_h, bias_h, weights_o, bias_o)

        cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=labels))
        train_operation = tf.train.GradientDescentOptimizer(self.learn_rate).minimize(cost)

        predict_operation = tf.where(logits >= 0.5, tf.ones_like(logits), tf.zeros_like(logits))

        with tf.Session() as sess:
            tf.global_variables_initializer().run()

            for epoch in range(self.num_epochs):
                p = np.random.permutation(range(len(train_data)))
                train_data, train_labels = train_data[p], train_labels[p]

                for start in range(0, len(train_data), self.batch_size):
                    end = start + self.batch_size
                    sess.run(train_operation, feed_dict={data: train_data[start:end], labels: train_labels[start:end]})

                if self.verbose and not epoch % 100:
                    print("Epoch:", epoch, "Accuracy:", np.mean(train_labels ==
                                         sess.run(predict_operation, feed_dict={data: train_data, labels: train_labels})))

            numbers = np.arange(1, 101)
            test_data = np.transpose(self.binary_encode(numbers, self.num_digits))
            test_labels = sess.run(predict_operation, feed_dict={data: test_data})

            return [self.fizz_buzz(numbers[i], test_labels[i].astype(bool)) for i in range(len(test_labels))]

if __name__ == '__main__':
    print(FizzBuzzModel().solve())
