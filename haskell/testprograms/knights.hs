module Main where
    data Islander = Knight | Knave deriving (Eq, Show)
    john :: (Islander, Islander) -> Bool
    john (x,y) = (x,y) == (Knave, Knave)
    solution3 :: [(Islander, Islander)]
    solution3 = [ (x,y) | x <- [Knight, Knave], y <- [Knight, Knave],john(x,y) == (x == Knight) ]
