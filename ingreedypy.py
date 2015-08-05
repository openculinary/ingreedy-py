from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

number_value = {
    'a': 1,
    'an': 1,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}


class Ingreedy(NodeVisitor):
    """Visitor that turns a parse tree into HTML fragments"""

    def __init__(self):
        self.res = {
            'unit': None,
            'unit_type': None,
            'amount': 1,
            'ingredient': None
        }

    grammar = Grammar(
        """
        ingredient_addition = amount space? container? (unit)? space? ingredient?

        amount
        = float
        / mixed_number
        / fraction
        / integer
        / number

        space
        = " "
        / ~"[\t]"

        ingredient
        = (word comma? (space word)*)

        container = open? amount space? unit close?

        open = "("
        close = ")"

        word
        = (letter+)

        float
        = (integer? ~"[.]" integer)

        mixed_number
        = (integer space fraction)

        fraction
        = (integer ~"[/]" integer)

        integer
        = ~"[0-9]+"

        letter
        = ~"[a-zA-Z]"

        comma
        = ","

        unit
        = (english_unit !letter)
        / (metric_unit !letter)
        / (imprecise_unit !letter)

        english_unit
        = cup
        / fluid_ounce
        / gallon
        / ounce
        / pint
        / pound
        / quart
        / tablespoon
        / teaspoon

        cup
        = "cups"
        / "cup"
        / "c."
        / "c"

        fluid_ounce
        = fluid space ounce

        fluid
        = "fluid"
        / "fl."

        gallon
        = "gallons"
        / "gallon"
        / "gal."
        / "gal"

        ounce
        = "ounces"
        / "ounce"
        / "oz."
        / "oz"

        pint
        = "pints"
        / "pint"
        / "pt."
        / "pt"

        pound
        = "pounds"
        / "pound"
        / "lbs."
        / "lbs"
        / "lb."
        / "lb"

        quart
        = "quarts"
        / "quart"
        / "qts."
        / "qts"
        / "qt."
        / "qt"

        tablespoon
        = "tablespoons"
        / "tablespoon"
        / "tbsp."
        / "tbsp"
        / "tbs."
        / "tbs"
        / "T."
        / "T"

        teaspoon
        = "teaspoons"
        / "teaspoon"
        / "tsp."
        / "tsp"
        / "t."
        / "t"

        metric_unit
        = gram
        / kilogram
        / liter
        / milligram
        / milliliter

        gram
        = "grams"
        / "gram"
        / "gr."
        / "gr"
        / "g."
        / "g"

        kilogram
        = "kilograms"
        / "kilogram"
        / "kg."
        / "kg"

        liter
        = "liters"
        / "liter"
        / "l."
        / "l"

        milligram
        = "milligrams"
        / "milligram"
        / "mg."
        / "mg"

        milliliter
        = "milliliters"
        / "milliliter"
        / "ml."
        / "ml"

        imprecise_unit
        = dash
        / handful
        / pinch
        / touch

        dash
        = "dashes"
        / "dash"

        handful
        = "handfuls"
        / "handful"

        pinch
        = "pinches"
        / "pinch"

        touch
        = "touches"
        / "touch"

        number
        = "a"
        / "an"
        / "zero"
        / "one"
        / "two"
        / "three"
        / "four"
        / "five"
        / "six"
        / "seven"
        / "eight"
        / "nine"
        / "ten"
        / "eleven"
        / "twelve"
        / "thirteen"
        / "fourteen"
        / "fifteen"
        / "sixteen"
        / "seventeen"
        / "eighteen"
        / "nineteen"
        / "twenty"
        / "thirty"
        / "forty"
        / "fifty"
        / "sixty"
        / "seventy"
        / "eighty"
        / "ninety"
        """)

    def visit_ingredient(self, node, visited_children):
        text = node.text
        if node.text.startswith('of '):
            text = text[3:]
        self.res['ingredient'] = text

    def visit_imprecise_unit(self, node, visited_children):
        self.res['unit'] = node.children[0].expr_name
        self.res['unit_type'] = 'imprecise'

    def visit_metric_unit(self, node, visited_children):
        self.res['unit'] = node.children[0].expr_name
        self.res['unit_type'] = 'metric'

    def visit_english_unit(self, node, visited_children):
        self.res['unit'] = node.children[0].expr_name
        self.res['unit_type'] = 'english'

    def visit_integer(self, node, visited_children):
        return int(node.text)

    def visit_fraction(self, node, visited_children):
        return round(float(visited_children[0]) / float(visited_children[2]), 3)

    def visit_mixed_number(self, node, visited_children):
        return float(visited_children[0]) + float(visited_children[2])

    def visit_float(self, node, visited_children):
        return float(node.text)

    def visit_amount(self, node, visited_children):
        self.res['amount'] *= sum(visited_children)

    def visit_ingredient_addition(self, node, visited_children):
        return self.res

    def visit_number(self, node, visited_children):
        return number_value[node.text]

    def generic_visit(self, node, visited_children):
        pass
