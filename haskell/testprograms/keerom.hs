module Main where
    keerom a = foldr (\x y -> y ++ [x]) [] a
