test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_swap(19, 91)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(20, 40)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(40, 20)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(41, 14)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(13, 32)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(34, 17)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(15, 30)
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
