data Contents = Treasure | Tiger
              deriving(Eq, Show)

sign1, sign2 :: (Contents, Contents) -> Bool
sign1 (x,y) = x == Treasure || y == Treasure
sign2 (x,y) = y == Tiger

solution1 :: [(Contents, Contents)]
solution1 = [ (x,y) | x <- [Treasure, Tiger], y <- [Treasure, Tiger], sign1(x,y) == sign2 (x,y)]
