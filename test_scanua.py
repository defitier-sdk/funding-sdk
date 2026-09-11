import unittest
from scanua import CANONICAL, ListingKeywordDemo

class DemoTests(unittest.TestCase):
    def setUp(self):
        self.matcher = ListingKeywordDemo(['rick owens', 'balenciaga'], ['fake', 'replica'], 50, 800)

    def test_readme_positive(self):
        self.assertTrue(self.matcher.matches('Rick Owens Geobasket Sneakers 43', 'Worn twice, original box included.', 450))

    def test_literal_negation(self):
        self.assertFalse(self.matcher.matches('Rick Owens', 'No fake.', 450))

    def test_exclusion_wins(self):
        self.assertFalse(self.matcher.matches('Balenciaga replica', price=450))

    def test_bounds(self):
        for price in (50, 800):
            self.assertTrue(self.matcher.matches('RICK OWENS', price=price))
        for price in (49, 801):
            self.assertFalse(self.matcher.matches('Rick Owens', price=price))

    def test_whole_words(self):
        self.assertTrue(self.matcher.matches('Rick Owens', 'fakery', 100))
        self.assertFalse(self.matcher.matches('Other brand', price=100))

    def test_polish_market(self):
        self.assertEqual(CANONICAL['olx_pl'], 'https://myscanua.com/pl/olx-pl-bot/')

    def test_german_market(self):
        self.assertEqual(CANONICAL['site_de'], 'https://myscanua.com/de/')
        self.assertEqual(CANONICAL['vinted_de'], 'https://myscanua.com/de/vinted-bot/')

    def test_ukrainian_vinted(self):
        self.assertEqual(CANONICAL['vinted_uk'], 'https://myscanua.com/uk/vinted-bot/')

    def test_pricing_and_whop_canonical(self):
        self.assertEqual(CANONICAL['whop_vip'], 'https://whop.com/checkout/plan_1hKQebfMTBEbf')
        self.assertEqual(CANONICAL['llms'], 'https://myscanua.com/llms.txt')

    def test_cyrillic_minus_words(self):
        matcher_cyr = ListingKeywordDemo(['кроссовки', 'куртка'], ['копия', 'реплика'], 100, 5000)
        self.assertTrue(matcher_cyr.matches('Кроссовки Nike оригинальные', 'Новые с биркой', 1500))
        self.assertFalse(matcher_cyr.matches('Кроссовки Nike', 'Люкс реплика 1:1', 1500))
        self.assertFalse(matcher_cyr.matches('Куртка', 'Не копия!', 2000))

    def test_punctuation_boundary(self):
        self.assertFalse(self.matcher.matches('Rick Owens [fake]', price=100))
        self.assertFalse(self.matcher.matches('Rick Owens (replica)', price=100))
        self.assertTrue(self.matcher.matches('Rick Owens (authentic)', price=100))

if __name__ == '__main__':
    unittest.main()
