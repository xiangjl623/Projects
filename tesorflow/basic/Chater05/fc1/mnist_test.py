#coding:utf-8
import time
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import mnist_backward

TEST_INTERVAL_SECS = 5

def test(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
        y = mnist_forward.forward(x, None)
        ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)
		
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
                    print("After %s training step(s), test accuracy = %g" % (global_step, accuracy_score))
                else:
                    print('No checkpoint file found')
                    return
            time.sleep(TEST_INTERVAL_SECS)

def main():
    #print(tf.__version__)
    mnist = input_data.read_data_sets("./data/", one_hot=True)
    #返回训练集 train 样本数
    #print("train data size:", mnist.train.num_examples)
    #返回验证集 validation 样本数
    #print("validation data size:", mnist.validation.num_examples)
    #返回测试集 test 样本数
    #print("test data size:", mnist.test.num_examples)
    #使用 train.labels 函数返回 mnist 数据集标签
    #print(mnist.train.labels[0])
    #使用 train.images 函数返回 mnist 数据集图片像素值
    #print(mnist.train.images[0])
    #使用 mnist.train.next_batch()函数将数据输入神经网络, 该函数包含一个参数 BATCH_SIZE，表示随机从训练集中抽取 BATCH_SIZE 个样本输入神经网络，并将样本的像素值和标签分别赋给 xs 和 ys
    #BATCH_SIZE = 200
    #xs, ys = mnist.train.next_batch(BATCH_SIZE)
    #print("xs shape:", xs.shape)
    #print("ys shape:", ys.shape)
    test(mnist)

if __name__ == '__main__':
    main()
