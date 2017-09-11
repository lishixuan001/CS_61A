test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_perfect_piggy(10)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(1)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(27)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(81)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(121)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(34)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(64)
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
