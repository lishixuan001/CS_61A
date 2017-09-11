test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 2)
          05f1f66ac99018feaad782542193b841
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          1db8597eac84e7adb36454b21eb78535
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          9055f90977ba85f1aad2f33322841711
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          5aa726f3ee5e32f3b1aaf920885bb5df
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 (cons 2 3))
          f8534fd9ad22447ac08f93a5bad2a7e5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(1 2 3)
          5aa726f3ee5e32f3b1aaf920885bb5df
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . 3)
          2155c721bb6c60b079cfd1bbd927e423
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . (3))               ; Recall dot notation rule
          b4eb2ccc685d977fb768f6cc0fed5095
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (eq? '(1 . (2 . 3)) (cons 1 (cons 2 (cons 3 nil))))
          a38287396efb23327499adcd0bcb4286
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (eq? '(1 . (2 . 3)) (cons 1 (cons 2 3)))
          0964e7a8804eb2749fbf7b014d9c25aa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (eq? '(1 . (2 . 3)) (list 1 (cons 2 3)))
          a38287396efb23327499adcd0bcb4286
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))     ; Recall quoting
          ab131c71478f14072589d60d12d7ce02
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
