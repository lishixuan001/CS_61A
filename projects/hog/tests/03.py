test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select_dice(True) == four_sided
          True
          >>> select_dice(False) == four_sided
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure None isn't returned
          >>> select_dice(True) == six_sided
          False
          >>> select_dice(False) == six_sided
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
