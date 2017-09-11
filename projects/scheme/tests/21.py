test = {
  'name': 'Problem 21 (EC)',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (function return)
          ....   (return 'return-value)
          ....   'after-return)
          function
          scm> (function (lambda (x) x))
          after-return
          scm> (call/cc function)
          return-value
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (call/cc (lambda (return) (return 'return-value) 'other-value))
          return-value
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (helper-two return)
          ....   (define (f cont) (cont 2) 3)
          ....   (return (* 10 (call/cc f))))
          helper-two
          scm> (call/cc helper-two)
          20
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (hailstone n return)
          ....         (print n)
          ....         (if (= n 1)
          ....             (return ()))
          ....         (if (= 1 (modulo n 2))
          ....             (hailstone (+ 1 (* 3 n)) return))
          ....         (hailstone (quotient n 2) return))
          hailstone
          scm> (call/cc (lambda (cont) (hailstone 100 cont)))
          100
          50
          25
          76
          38
          19
          58
          29
          88
          44
          22
          11
          34
          17
          52
          26
          13
          40
          20
          10
          5
          16
          8
          4
          2
          1
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
