(define foo (
    fun (n) (
        if (< n 2)
            1
            (*
                n
                (foo (- n 1))
            )
        )
    )
)
(print-num (foo 5))