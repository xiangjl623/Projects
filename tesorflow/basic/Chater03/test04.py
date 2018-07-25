import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np

BATCH_SIZE  = 8
seed = 2345

#基于seed产生随机数
rng = np.random.RandomState(seed)

X = rng.rand(32, 2)

Y = [[int (x0 + x1 < 1)] for (x0, x1) in X]
print("X\n", X)
print("Y\n", Y)

#两层简单神经网络（全连接）

#1 定义输入和参数及传播过程
x = tf.placeholder(tf.float32, shape=(None, 2)) # 多组数据
y_ = tf.placeholder(tf.float32, shape=(None, 1)) # 1组数据

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

#2 定义损失函数及方向传播方法
loss = tf.reduce_mean(tf.square(y-y_))
#trans_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss);
#trans_step = tf.train.AdamOptimizer(0.001).minimize(loss);
trans_step = tf.train.MomentumOptimizer(0.001, 0.9).minimize(loss);

#3生成会话 训练Steps

#用会话计算结果
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    #输入目前（未经过训练） 的参数取值
    print("W1:\n", sess.run(w1))
    print("W2:\n", sess.run(w2))
    print("\n")

    #训练模型
    STEPS = 3000
    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(trans_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 500 == 0:
            total_loss = sess.run(loss, feed_dict={x: X, y_: Y})
            print(("After %d training step(s), loss on all data is %g" % (i, total_loss)))

    # 输出训练后的参数取值
    print("\n")
    print ("W1:\n", sess.run(w1))
    print ("W2:\n", sess.run(w2))


