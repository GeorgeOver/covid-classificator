import classificator

model = classificator.loadModel('covid19.model')
pred = classificator.classifySingleImage('2.jpg', model)
if pred[0] == 0:
    print('Covid')
else:
    print('Normal')