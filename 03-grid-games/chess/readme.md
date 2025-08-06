# Programming Chess

## Table of Contents
* The Board
* Making moves
* Verifying moves
* Preventing pinned moves
* Castling
* En Passant
* Allow take backs?

Chess is delightful to play and a joy to program. My general strategy for
programming Chess is to start simple then add more complexity. First make a
board. Then add pieces to the board. Then make the pieces move. Now make sure
the pieces can't make absurd moves. Now make the pieces follow the rules a
little bit more. Then mix in more complex rules like promotion, castling and En
Passant and see how it affects the design. Once we've got a legit Chess engine
built we can have more fun and consider implementing variations! Should players
be allowed to take turns back? What does it take to build variations like chess
960, King of the Hill, nuclear chess, anti-chess, duck chess, bughouse or three
or four player Chess?