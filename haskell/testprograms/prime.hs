module Main where
    priem :: [Integer]
    priem = zeef [2..]
    where zeef (p:xs) = p : zeef [ x | x <- xs, x`mod`p /= 0]
