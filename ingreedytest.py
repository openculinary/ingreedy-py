# -*- coding: utf-8 -*-

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
        'amount': 12,
        'ingredient': 'boneless skinless chicken breasts',
        'unit': 'ounce',
        'weight': 6,
    },
    '1 (28 ounce) can crushed tomatoes': {
        'amount': 1,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
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
        'weight': 3,
    },
    '2 (28 ounce) can crushed tomatoes': {
        'amount': 2,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
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
        'amount': 3,
        'ingredient': 'cans of crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
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
        'amount': 1,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
    },
    'one cup flour': {
        'amount': 1,
        'ingredient': 'flour',
        'unit': 'cup',
    },
    'three 28 ounce cans crushed tomatoes': {
        'amount': 3,
        'ingredient': 'cans crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
    },
    'two 28 ounce cans crushed tomatoes': {
        'amount': 2,
        'ingredient': 'cans crushed tomatoes',
        'unit': 'ounce',
        'weight': 28,
    },
    'two five ounce can crushed tomatoes': {
        'amount': 2,
        'ingredient': 'can crushed tomatoes',
        'unit': 'ounce',
        'weight': 5,
    },
    '1kg / 2lb 4oz potatoes': {
        'amount': 1,
        'ingredient': 'potatoes',
        'unit': 'kilogram',
        'weight': 4,
    },
    '2lb 4oz potatoes': {
        'amount': 2,
        'ingredient': 'potatoes',
        'unit': 'pound',
        'weight': 4,
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
}


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_amounts(description, expectation):
    result = Ingreedy().parse(description)
    assert result['amount'] == expectation['amount']


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_unit(description, expectation):
    result = Ingreedy().parse(description)
    assert result['unit'] == expectation['unit']


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_ingredient(description, expectation):
    result = Ingreedy().parse(description)
    assert result['ingredient'] == expectation['ingredient']


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_weight(description, expectation):
    result = Ingreedy().parse(description)
    assert result.get('weight') == expectation.get('weight')
