# README

An ML implementation of [the Fizz Buzz Kata](http://agilekatas.co.uk/katas/FizzBuzz-Kata). You can find the
implementation up to feature 1 on the `fizz_buzz` branch. The `master` branch contains an implementation of
feature 2 ("pop") as well.

## Credits

Heavily borrowed from [Fizz Buzz Tensorflow](https://github.com/joelgrus/fizz-buzz-tensorflow),
"enhanced" with some integration testing, multiclass prediction and the second fizz buzz feature "pop".

## How to run
* Install python 2.7.x: on OSX `brew install python`, on Linux `apt-get python-dev`
* Install virtualenv: `pip install virtualenv`
* Create a virtualenv in the repo root folder with the python 2.7 runtime: `virtualenv --python=python2.7 .`
* Install dependencies: `pip install -r requirements.txt`
* Run the tests: `./run-test`

## Have fun
You can use this as a sandbox for tensorflow to get a feeling for deep learning / neural networks.
What happens if...
 *  you add more data (Increase `num_digits`)?
 *  you increase the depth of the network (Increase `num_hidden`)?
 *  you allow the network to learn for longer (Increase `num_epochs`)?
 *  you change the `learning_rate`?
 *  you change the `batch_size`?
 *  you change the optimisation method?
 *  you increase the complexity of the model by adding more or different layers in?
