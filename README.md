# Introduction
The problem requires us to place tiles on a landscape of square shape, on which certain bushes grow, marked by colors: 1, 2, 3, 4. The landscape is of square shape of 200 x 200, and we are given a set of tiles of three different shapes: full block, outer boundary, and EL shaped. Each tile is of size 4x4 and covers only part of the landscape. Our task is to place these tiles in a way that we fulfill the target of which bushes should be visible after tile placement.
# Variables
The variables in this problem are the positions where each tile is placed on the landscape. Each tile can be placed in any position on the landscape.
# Domains
The domains for the variables are the set of all possible tile placements. The domain of each variable represents all possible placements of tiles of the three different shapes (full block, outer boundary, and EL shaped) on the landscape.
# Constraints
The constraints for the problem are as follows:
•	Each tile should be placed on a valid position on the landscape. It should not overlap with any other tile, and it should not be placed outside of the landscape.
•	For each tile placement, the bushes visible after tile placement should match the target bushes specified.
•	The total number of tiles should be equal to the size of the landscape divided by the size of the tile.
