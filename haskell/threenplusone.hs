module Main where
nextitem :: Integer -> Integer
nextitem x = if odd x then (3*x) + 1
                else x`div`2
nextuple :: (Integer, Integer) -> (Integer, Integer)
nextuple (x, 0) = (x, 0)
nextuple (x, y) = nextuple(nextitem(x),y -1)
