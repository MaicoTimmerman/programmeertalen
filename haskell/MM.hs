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
import Debug.Trace
import Control.Monad

-- Specify Color datatype.
data Color = Red | Yellow | Blue | Green | Orange | Purple
    deriving (Eq, Show, Bounded, Enum)

-- type Pattern is a list of colors.
type Pattern = [ Color ]

-- Amount of back and white pins.
type Feedback = (Int, Int)

-- Returns the reaction of the inserted pattern x compared to the
-- "secret" pattern y in blackpins and whitepins (_,_).
reaction :: Pattern -> Pattern -> Feedback
reaction x y = (blackpins x y, whitepins x y)

-- Return an amount of whitepins in the reaction, which is the number of elements
-- appearing in both lists minus the blackpins. These are elements on the correct
-- position.
whitepins :: Pattern -> Pattern -> Int
whitepins list1 list2 = 4 - length ( list1 \\ list2 ) - blackpins list1 list2

-- Return the amount of black pins in the reaction, which is the number of elements
-- that are equal in both lists.
blackpins :: Pattern -> Pattern -> Int
blackpins list1 list2 = length ( [ (x,y) | (x,y) <- zip list1 list2, x == y] )

-- Setting some standard variables for the Algorithms:
-- store is a list of lists with 4 elements with all possible options.
colors :: [Color]
colors = [minBound..maxBound]
store = replicateM 4 colors

-- Tests a solving algorithm for the average amount of tries needed to solve the puzzle.
tester :: (Pattern -> [Pattern]) -> Double
tester algorithm =
    (fromIntegral(sum [length (algorithm x) | x  <- store ])) / (fromIntegral(length (store)))

-- Initializer for the Naïef algoritm.
naiveAlgorithm :: Pattern -> [Pattern]
naiveAlgorithm secret = naiveFilterOptions secret store []


-- Filters the options for the naiveAlgorithm, takes the secret, the options left and a list of tries.
-- When finished gives back a list of tried patterns in reversed order.
naiveFilterOptions :: Pattern -> [Pattern] -> [Pattern] -> [Pattern]
naiveFilterOptions secret allLeft tries
    | (reaction secret next) == (4,0) = next : tries
    | otherwise = naiveFilterOptions secret
        [ x | x <- allLeft, (reaction next x) == (reaction secret next)] (next:tries)
             where next = (head allLeft)
