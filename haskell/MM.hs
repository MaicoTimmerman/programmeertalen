---
-- Name:    Maico Timmerman
-- CKnum:   10542590
--
-- module MM:
--  This module implements the mastermind game, the module contains a algorithm
--  to find the secret pattern.
---
module MM where

import Data.List
import Control.Monad

data Color = Red | Yellow | Blue | Green | Orange | Purple
    deriving (Eq, Show, Bounded, Enum)

type Pattern = [ Color ]

-- Amount of back and white pins.
type Feedback = ( Int, Int)

reaction :: Pattern -> Pattern -> Feedback
reaction x y = (a, b)
    where a = whitepins x y
    where b = blackpins x y

whitepins :: Pattern -> Pattern -> Int
whitepins x y i n = if

blackpins :: Pattern -> Pattern -> Int
blackpins x y i n = if (x !! i) == (y !! i) then blackpins


-- Naïef algoritme
-- colors :: [Color]
-- colors = [minBound..maxBound]
