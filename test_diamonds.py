from create_diamond import create_diamond

def test_correct_diamond():
    b_diamond = " A\nABA\n A"
    assert(create_diamond('B') == b_diamond)
    a_diamond = "A"
    assert(create_diamond('A') == a_diamond)
    c_diamond = "  A\n ABA\nABCBA\n ABA\n  A"
    assert(create_diamond('C') == c_diamond)

def test_lower_case():
    b_diamond = " A\nABA\n A"
    assert(create_diamond('b') == b_diamond)
