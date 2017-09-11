test = {
  'name': 'test-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (= 8 (exp 2 3))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (= 1 (exp 9.137 0))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (= 1024 (exp 4 5))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (= 6.25 (exp 2.5 2))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (= 16 (remainder (exp 2 (exp 2 10)) 100)))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
