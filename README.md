# Earley algorithm
Here is an implementation of the Earley parsing algorithm using Python: given grammatic rules and a word, the algorithm outputs whether this word is appropriate for dictionary generated by this grammatic or not. 

_P.S. Non-terminal characters are considered to be uppercase and terminal lowercase, starting non-teminal is 'S'._

## Installation

> git clone git@github.com:limerentt/earley_algorithm.git

## Usage

To set your own grammar and testing word, input grammar in file "__tests/local_grammar.txt__" in format: **Not_terminal_character -> Derivation** (e.g. S -> AaB). Execute __main.py__ and input your word in terminal.

There are also pytests included in project ("__./tests/test_words.py__"), to start them enter:

> make test

Coverage test:

> make test-cov

Covered lines are shown in ("__./htmlcov/index.html__").

## Pleasant using!
