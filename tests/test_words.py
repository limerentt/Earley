import src.grammar as grammar

def test_word():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("aac")
    
def test_epsilon():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("aa$c")

def test_empty_word():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("$$$")
    
def test_no_empty_word():
    GR = grammar.Grammar("./tests/test_no_eps.txt")
    assert not GR.word_is_suitable("$$$")
    