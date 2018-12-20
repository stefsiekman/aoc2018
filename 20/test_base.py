from unittest import TestCase, main
import base

class TestBase(TestCase):


    def test_conat_example1(self):
        regex = "(WNSE|)SSS$"
        conat = base.continueAt(regex, 5)
        self.assertEqual(conat, 7)

    def test_conat_example2(self):
        regex = "(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE))$"
        conat = base.continueAt(regex, 15)
        self.assertEqual(conat, 34)

    def test_conat_example3(self):
        regex = "(WENS|NEEW)NN"
        conat = base.continueAt(regex, 5)
        self.assertEqual(conat, 11)

    def test_conat_example4(self):
        regex = "(WENS|)NN"
        conat = base.continueAt(regex, 6)
        self.assertEqual(conat, 7)

    def test_conidx_example0(self):
        regex = "NNN()SSS$"
        conidx = base.continueIndices(regex, 3)
        self.assertEqual(conidx, [4])

    def test_conidx_example1(self):
        regex = "(WNSE|)SSS$"
        conidx = base.continueIndices(regex, 0)
        self.assertEqual(conidx, [1, 6])

    def test_conidx_example2(self):
        regex = "(WNSE|ESN)SSS$"
        conidx = base.continueIndices(regex, 0)
        self.assertEqual(conidx, [1, 6])

    def test_conidx_example3(self):
        regex = "(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
        conidx = base.continueIndices(regex, 0)
        self.assertEqual(conidx, [1, 3])

    def test_regex_example1(self):
        regex = "(WNSE|)SSS$"
        sections, after = base.splitSections(regex)
        self.assertEqual(sections, ["WNSE", ""])
        self.assertEqual(after, "SSS$")

    def test_regex_example2(self):
        regex = "(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE))$"
        sections, after = base.splitSections(regex)
        self.assertEqual(sections, ["EESS(WNSE|)SSS", "WWWSSSSE(SW|NNNE)"])
        self.assertEqual(after, "$")

    def test_regex_example3(self):
        regex = "(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
        sections, after = base.splitSections(regex)
        self.assertEqual(sections, ["E", "NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE))"])
        self.assertEqual(after, "$")

if __name__ == "__main__":
    main()
