; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((= x 0) 0)
    (else -1)
  )
)

(define (ordered? s)
  (cond
   ((null? (cdr s)) #t)
   ( (>= (car (cdr s) ) (car s) ) (and #t (ordered? (cdr s))))
   (else #f)
  )
)

(define (nodots s)
  (if (null? s)
    nil     ; Note that for the returned value, we cannot add(nil)
    (if (pair? (car s))                                      ; The first if: car is pair or nor
      (if (pair? (cdr s))                                    ; If yes
        (cons (nodots (car s)) (nodots (cdr s)))
        (cons (nodots (car s)) (cons (cdr s) nil))
      )
      (if (pair? (cdr s))
        (cons (car s) (nodots (cdr s)))
        (if (null? (cdr s))
          (cons (car s) nil)
          (cons (car s) (cons (cdr s) nil))
        ) ;second condition
      ) ;second condition
    ) ;t he big if
  ) ; the super big if
) ; define

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f) ; set the base cases: totally three
          ((> (car s) v) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v)) ;recursion
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))   ; totally two base cases
          ((contains? s v) s)
          (else
            (if (< v (car s))
              (cons v s)
              (cons (car s) (add (cdr s) v) )
            )
          )
    )
)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil) ; totally three base cases
          ( (= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ( (< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          (else (cons (car t) (union s (cdr t))))
          ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (helper b n total)
    (if (= n 0)
      total
      (helper b (- n 1) (* total b))
    )
  )
  (helper b n 1)
)

(define (filter pred lst)
  (define (helper fn lst new)
    (if (null? lst)
      new
      (if(fn (car lst))
        (helper fn (cdr lst) (append new (list (car lst))))
        (helper fn (cdr lst) new)
      )
    )
  )
  (helper pred lst ())
)
