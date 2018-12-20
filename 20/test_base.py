from unittest import TestCase, main
import base

class TestBase(TestCase):

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
