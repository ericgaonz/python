# 全班所有同学都选课了，大家各自都选择了自己的课程。
# 以下的同学选了数学：
# Amy, Tom, Jack, Tim, Kelly, Jacky, Aurora, Hieu
# 以下的同学都选了篮球：
# Jason, Jacky, Tom, Tim, Max, Jack, Rex, Kunal
# 以下的同学都选择了Python编程：
# Christina, Jason, Tim, Hieu, Selina, Jack, Jerry

# 请把以上数据存入三个集合（set），然后通过集合做交集、并集、差集运算，计算出以下数据：
# 1，全班一共有多少同学，每个同学的名字是什么？
# 2，同时选择三门课程的有多少人，都是谁？
# 3，只选择数学的有几人，都是谁？
# 4，都有哪些同学只选择了一门课，都是谁，多少人？

math = {'Amy', 'Tom', 'Jack', 'Tim', 'Kelly', 'Jacky', 'Aurora', 'Hieu'}
basketball = {'Jason', 'Jacky', 'Tom', 'Tim', 'Max', 'Jack', 'Rex', 'Kunal'}
python = {'Christina', 'Jason', 'Tim', 'Hieu', 'Selina', 'Jack', 'Jerry'}

all = math | basketball | python
print('There are totally %d students:' % len(all))
print(all)

common = math & basketball & python
print('\nThere are %d students who chose all three subjects:' % len(common))
print(common)

mathonly = math - basketball - python
print('\nThere are %d students who chose the math only:' % len(mathonly))
print(mathonly)

# unique = math ^ basketball ^ python
# print('\nThere are %d students who only chose one subject:' % len(unique))
# print(unique)

mathonly1 = math - (basketball | python)
print('\nThere are %d students who chose the math only:' % len(mathonly1))
print(mathonly1)

