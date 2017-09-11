test = {
  'name': 'test-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(0 1 1 2 3 5 8))
          (0 2 8)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter even? '(2 4 6 8 10))
          (2 4 6 8 10)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter even? '(1 3 5))
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter even? (longlink 8))
          (8 8 8 8 8 8 8 8)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter even? (longlink 15))
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      scm> (define (even? x)
        (= (modulo x 2) 0))
      scm> (define (longlink num)
              (define (helper count num result)
                  (if (= count 0)
                    result
                    (helper (- count 1) num (cons num result))
                  )
              )
              (helper num num '())
            )
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
