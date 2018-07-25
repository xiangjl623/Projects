import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#两层简单神经网络（全连接）

#定义输入和参数
#x = tf.constant([[0.7, 0.5]]) #理解一下张量的阶
#x = tf.placeholder(tf.float32, shape=(1, 2)) # 1行两列
x = tf.placeholder(tf.float32, shape=(None, 2)) # 多组数据
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

#定义前向传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
print(x)
print(a)
print(y)

#用会话计算结果
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    print(sess.run(y, feed_dict={x: [[0.7, 0.5], [0.5, 0.5]]}))
