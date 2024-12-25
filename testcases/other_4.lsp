(define diff 
    (
        fun (x y) (
            (
                fun (x) ((
                    (if (< x 0) (- 0 x) x)
                ))
            ) (- x y)
        )
    )
)
(print-num (diff 6 12))