# From Siraj Raval's video
# Introduction - Learn Python for Data Science #1
# https://youtu.be/T5pRlIbr6gg

from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44],
     [177,70,43],
     [160,60,38],
     [154,54,37],
     [166,65,40],
     [190,90,47],
     [175,65,39]]

Y = ['male', 'female', 'female', 'male', 'male', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[160,60,38]])

print(prediction) 
