from create_diamond import create_diamond

def test_correct_diamond():
    b_diamond = " A\nABA\n A"
    assert(create_diamond('B') == b_diamond)
