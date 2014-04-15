
(define (sqrt x)
    (sqrt_guess 1 x))
        
(define (sqrt_guess guess target)
    (if (within_tol (* guess guess) target)
        guess
        (sqrt_guess (average guess (/ target guess)) target)))

(define (average x y)
    (/ (+ x y) 2.))

(define tolerance .0001)

(define (within_tol x y)
    (< (abs (- x y)) tolerance))

	
(sqrt 10000)
