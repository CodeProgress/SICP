
; SICP - 1.2.4 Exponentiation

(define (is_even x)
    (= (mod x 2) 0))

(define (square x)
    (* x x))

(define (pow base expon)
    (if (= expon 0)
        1
        (if (is_even expon)
            (square (pow base (/ expon 2)))
            (* base (pow base (- expon 1))))))

		
