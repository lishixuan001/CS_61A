(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map fn items)
  (cond ((null? items) items)
        (else
          (cons (fn (car items)) (map fn (cdr items)))
        )
  )
)

(define (cons-all first rests)
  (map (lambda (lst) (cons first lst)) rests)
)

(define (zip pairs)
  (cons (map car pairs) (cons (map cadr pairs) nil) )
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (helper s index)
  (if (null? s)
  nil
  (cons (list index (car s)) (helper (cdr s) (+ index 1)))))
  (helper s 0))
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond
    ((null? denoms) nil)
    ((= total 0) '())
    ;((> total (car denoms)) () )
    ((< total (car denoms)) (list-change total (cdr denoms)))
    (else (append (cons (car denoms) (list-change (- total (car denoms) ) denoms) )
                  (list-change total (cdr denoms))
          ) ; append
    ) ; else
  )
)
(define (list-change total denoms)
  (define (helper total denoms)
    (cond
      ((= total (car denoms)) (list (list total)))
      ((> total (car denoms)) (cons-all (car denoms) (list-change (- total (car denoms)) denoms)))))
  (cond ((null? denoms) ())
        ((< total (car denoms)) (list-change total (cdr denoms)))
        (else (append (helper total denoms) (list-change total (cdr denoms))))))
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
          ; the condition for 'or'
           (let ((form   (car expr))
                 (params (cadr expr))
                 (body   (cddr expr)))
              ; (let ((x 42) (y 16)) (+ x y))
              ; ((lambda (x y) (+ x y)) 42 16)
             ; BEGIN PROBLEM 19
             (cons form (cons params (map let-to-lambda body) ) )
             ; END PROBLEM 19
             )
        )
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons (cons 'lambda (cons (car (zip values))
                                      (map let-to-lambda body)
                                )
                  )
                 (map let-to-lambda (cadr (zip values) ) )
            )

           ; END PROBLEM 19
           )
        )
        (else
         ; BEGIN PROBLEM 19
         (cons (car expr)
               (map let-to-lambda (cdr expr))
         )
         ; END PROBLEM 19
         )))
