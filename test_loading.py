cd ..
cd mnist-ml-test

pwd

from helpers import loading

#laeb treening data-st laisalt tagastades (label, pilt) tupple-id
training_gen = loading.read(path="data")

e = next(training_gen)
