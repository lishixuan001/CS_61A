(define (cddr s)
  (cdr (cdr s)))



(define (cadr s)
(if (cdr s)
(car (cdr s))
nil))



(define (caddr s)
(if (cddr s)
(car (cddr s))
nil)
)



(define (sign x)
(cond
((> x 0) '1)
((< x 0) '-1)
(else '0)))


(define (square x) (* x x))

(define (pow b n)
  (cond
  ((= n 1) b)
  ((even? n) (square (pow b (/ n 2))))
  (else (* b (pow b (- n 1))))))

(define (ordered? s)
(cond
((null? s) 'True)
((null? (cdr s)) 'True)
((> (car s) (car (cdr s))) 'False)
(else (ordered? (cdr s)))))

(define (nodots s)
  (cond
    ((null? s) nil)
    ((pair? (car s))
      (if (pair? (cdr s))
        (cons (nodots(car s)) (nodots(cdr s)))
        (cons (nodots(car s)) (cons (cdr s) nil))
      )
    )
    (else
      (if (pair? (cdr s))
        (cons (car s) (nodots (cdr s)))
        (if (null? (cdr s))
          (cons (car s) nil)
          (cons (car s) (cons (cdr s) nil))
        )
      )
    )
  )
)



; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) 'False)
          ((> (car s) v) 'False)
          ((= (car s) v) 'True)
          (else (contains? (cdr s) v))
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
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          (else
            (if (< v (car s))
              (cons v s)
              (cons (car s) (add (cdr s) v) )
          ))))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t))
          )))

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
          (else (cons (car t) (union s (cdr t)))
          )))

; Q9 - Survey
(define (survey)
    ; Midsemester Survey: https://goo.gl/forms/a3NTVfZWFjWReu0x1
    'procedure
)

(define (concat a b)
(cond
((null? a) b)
((null? b) a)
(else (cons (car a) (concat (cdr a) b)))))

(define (map fn lst)
    (if (null? lst)
        nil
    (cons (fn (car lst)) (map fn (cdr lst)))))

  (define (deep-apply fn nested-list)
    (if (list? (car nested-list))
       (cons (map (car fn)) (deep-apply fn (cdr nested-list)))
       (if (null? (cdr nested-list))
       (fn (car nested-list))
       (cons (fn (car nested-list)) (deep-apply fn (cdr nested-list))))))
