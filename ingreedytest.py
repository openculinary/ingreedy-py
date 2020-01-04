# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from ingreedypy import Ingreedy

test_cases = {
    '1.0 cup flour': {
        'quantity': [{
            'amount': 1.0,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '1 1/2 cups flour': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '1 1/2 potatoes': {
        'quantity': [{
            'amount': 1.5,
            'unit': None
        }],
        'ingredient': 'potatoes',
    },
    '12345 potatoes': {
        'quantity': [{
            'amount': 12345,
            'unit': None
        }],
        'ingredient': 'potatoes',
    },
    '1 2/3 cups flour': {
        'quantity': [{
            'amount': round(float(5.0/3), 3),
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '12 (6-ounce) boneless skinless chicken breasts': {
        'quantity': [{
            'amount': 72,
            'unit': 'ounce'
        }],
        'ingredient': 'boneless skinless chicken breasts',
    },
    '1 (28 ounce) can crushed tomatoes': {
        'quantity': [{
            'amount': 28,
            'unit': 'ounce'
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '1/2 cups flour': {
        'quantity': [{
            'amount': 0.5,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '12g potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram'
        }],
        'ingredient': 'potatoes',
    },
    '12oz potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'ounce'
        }],
        'ingredient': 'potatoes',
    },
    '12oz tequila': {
        'quantity': [{
            'amount': 12,
            'unit': 'ounce'
        }],
        'ingredient': 'tequila',
    },
    '1/2 potato': {
        'quantity': [{
            'amount': 0.5,
            'unit': None
        }],
        'ingredient': 'potato',
    },
    '1.5 cups flour': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '1.5 potatoes': {
        'quantity': [{
            'amount': 1.5,
            'unit': None
        }],
        'ingredient': 'potatoes',
    },
    '1 clove garlic, minced': {
        'quantity': [{
            'amount': 1,
            'unit': None
        }],
        'ingredient': 'clove garlic, minced',
    },
    '1 cup flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '1 garlic clove, sliced in 1/2': {
        'quantity': [{
            'amount': 1,
            'unit': None
        }],
        'ingredient': 'garlic clove, sliced in 1/2',
    },
    '1 tablespoon (3 teaspoons) Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market': {
        'quantity': [{
            'amount': 1,
            'unit': 'tablespoon'
        }],
        'ingredient': 'Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market',
    },
    '2 (28 ounce) can crushed tomatoes': {
        'quantity': [{
            'amount': 56,
            'unit': 'ounce'
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '.25 cups flour': {
        'quantity': [{
            'amount': 0.25,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    '2 cups of potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'cup'
        }],
        'ingredient': 'potatoes',
    },
    '2 eggs, beaten': {
        'quantity': [{
            'amount': 2,
            'unit': None
        }],
        'ingredient': 'eggs, beaten',
    },
    '3 28 ounce cans of crushed tomatoes': {
        'quantity': [{
            'amount': 84,
            'unit': 'ounce'
        }],
        'ingredient': 'cans of crushed tomatoes',
    },
    '5 3/4 pinches potatoes': {
        'quantity': [{
            'amount': 5.75,
            'unit': 'pinch'
        }],
        'ingredient': 'potatoes',
    },
    '.5 potatoes': {
        'quantity': [{
            'amount': 0.5,
            'unit': None
        }],
        'ingredient': 'potatoes',
    },
    'a cup of flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    'ground black pepper to taste': {
        'quantity': None,
        'ingredient': 'ground black pepper to taste',
    },
    'one 28 ounce can crushed tomatoes': {
        'quantity': [{
            'amount': 28,
            'unit': 'ounce'
        }],
        'ingredient': 'can crushed tomatoes',
    },
    'one cup flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup'
        }],
        'ingredient': 'flour',
    },
    'three 28 ounce cans crushed tomatoes': {
        'quantity': [{
            'amount': 84,
            'unit': 'ounce'
        }],
        'ingredient': 'cans crushed tomatoes',
    },
    'two 28 ounce cans crushed tomatoes': {
        'quantity': [{
            'amount': 56,
            'unit': 'ounce'
        }],
        'ingredient': 'cans crushed tomatoes',
    },
    'two five ounce can crushed tomatoes': {
        'quantity': [{
            'amount': 10,
            'unit': 'ounce'
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '1kg / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram'
        }],
        'ingredient': 'potatoes',
    },
    '2lb 4oz potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound'
        }, {
            'amount': 4,
            'unit': 'ounce'
        }],
        'ingredient': 'potatoes',
    },
    '2lb 4oz (1kg) potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound'
        }, {
            'amount': 4,
            'unit': 'ounce'
        }],
        'ingredient': 'potatoes',
    },
    '1-1/2 ounce vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce'
        }],
        'ingredient': 'vanilla ice cream',
    },
    '1-½ ounce vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce'
        }],
        'ingredient': 'vanilla ice cream',
    },
    'apple': {
        'quantity': None,
        'ingredient': 'apple',
    },
    '3-⅝ ounces, weight feta cheese, crumbled/diced': {
        'quantity': [{
            'amount': 3.625,
            'unit': 'ounce'
        }],
        'ingredient': 'weight feta cheese, crumbled/diced',
    },
    '16-ounce can of sliced pineapple': {
        'quantity': [{
            'amount': 16,
            'unit': 'ounce'
        }],
        'ingredient': 'can of sliced pineapple',
    },
    '750ml/1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter'
        }],
        'ingredient': 'hot vegetable stock',
    },
    'pinch salt': {
        'quantity': [{
            'amount': 1,
            'unit': 'pinch'
        }],
        'ingredient': 'salt',
    },
}


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_parser(description, expectation):
    result = Ingreedy().parse(description)
    for key in expectation:
        assert result[key] == expectation[key]
