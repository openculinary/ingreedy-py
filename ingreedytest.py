# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from ingreedypy import Ingreedy

test_cases = {
    '1.0 cup flour': {
        'amount': 1,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '1 1/2 cups flour': {
        'amount': 1.5,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '1 1/2 potatoes': {
        'amount': 1.5,
        'ingredient': 'potatoes',
        'unit': None,
    },
    '12345 potatoes': {
        'amount': 12345,
        'ingredient': 'potatoes',
        'unit': None,
    },
    '1 2/3 cups flour': {
        'amount':  round(float(5.0/3), 3),
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '12 (6-ounce) boneless skinless chicken breasts': {
        'amount': 72,
        'ingredient': 'boneless skinless chicken breasts',
        'unit': 'ounce',
    },
    '1 (28 ounce) can crushed tomatoes': {
        'amount': 28,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
    },
    '1/2 cups flour': {
        'amount': 0.5,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '12g potatoes': {
        'amount': 12,
        'ingredient': 'potatoes',
        'unit': 'gram',
    },
    '12oz potatoes': {
        'amount': 12,
        'ingredient': 'potatoes',
        'unit': 'ounce',
    },
    '12oz tequila': {
        'amount': 12,
        'ingredient': 'tequila',
        'unit': 'ounce',
    },
    '1/2 potato': {
        'amount': 0.5,
        'ingredient': 'potato',
        'unit': None,
    },
    '1.5 cups flour': {
        'amount': 1.5,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '1.5 potatoes': {
        'amount': 1.5,
        'ingredient': 'potatoes',
        'unit': None,
    },
    '1 clove garlic, minced': {
        'amount': 1,
        'ingredient': 'clove garlic, minced',
        'unit': None,
    },
    '1 cup flour': {
        'amount': 1,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '1 garlic clove, sliced in 1/2': {
        'amount': 1,
        'ingredient': 'garlic clove, sliced in 1/2',
        'unit': None,
    },
    '1 tablespoon (3 teaspoons) Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market': {
        'amount': 1,
        'ingredient': 'Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market',
        'unit': 'tablespoon',
    },
    '2 (28 ounce) can crushed tomatoes': {
        'amount': 56,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
    },
    '.25 cups flour': {
        'amount': 0.25,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    '2 cups of potatoes': {
        'amount': 2,
        'ingredient': 'potatoes',
        'unit': 'cup',
    },
    '2 eggs, beaten': {
        'amount': 2,
        'ingredient': 'eggs, beaten',
        'unit': None,
    },
    '3 28 ounce cans of crushed tomatoes': {
        'amount': 84,
        'ingredient': 'cans of crushed tomatoes',
        'unit': 'ounce',
    },
    '5 3/4 pinches potatoes': {
        'amount': 5.75,
        'ingredient': 'potatoes',
        'unit': 'pinch',
    },
    '.5 potatoes': {
        'amount': 0.5,
        'ingredient': 'potatoes',
        'unit': None,
    },
    'a cup of flour': {
        'amount': 1,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    'ground black pepper to taste': {
        'amount': None,
        'ingredient': 'ground black pepper to taste',
        'unit': None,
    },
    'one 28 ounce can crushed tomatoes': {
        'amount': 28,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
    },
    'one cup flour': {
        'amount': 1,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    'three 28 ounce cans crushed tomatoes': {
        'amount': 84,
        'ingredient': 'cans crushed tomatoes',
        'unit': 'ounce',
    },
    'two 28 ounce cans crushed tomatoes': {
        'amount': [2, 28],
        'ingredient': 'cans crushed tomatoes',
        'unit': 'ounce',
    },
    'two five ounce can crushed tomatoes': {
        'amount': [2, 5],
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
    },
    '1kg / 2lb 4oz potatoes': {
        'amount': 1,
        'ingredient': 'potatoes',
        'unit': 'kilogram',
    },
    '2lb 4oz potatoes': {
        'amount': [2, 4],
        'ingredient': 'potatoes',
        'unit': 'pound',
    },
    '1-1/2 ounce vanilla ice cream': {
        'amount': 1.5,
        'ingredient': 'vanilla ice cream',
        'unit': 'ounce',
    },
    '1-½ ounce vanilla ice cream': {
        'amount': 1.5,
        'ingredient': 'vanilla ice cream',
        'unit': 'ounce',
    },
    'apple': {
        'amount': None,
        'ingredient': 'apple',
        'unit': None,
    },
    '3-⅝ ounces, weight feta cheese, crumbled/diced': {
        'amount': 3.625,
        'ingredient': 'weight feta cheese, crumbled/diced',
        'unit': 'ounce'
    },
    '16-ounce can of sliced pineapple': {
        'amount': 16,
        'ingredient': 'can of sliced pineapple',
        'unit': 'ounce'
    },
}


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_parser(description, expectation):
    result = Ingreedy().parse(description)
    for key in expectation:
        assert result[key] == expectation[key]
