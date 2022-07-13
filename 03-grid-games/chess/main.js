let dictBoard = {
  h1: new R(), h2: new N(), h3: new B(), h4: new Q(), h5: new K(), h6: new B(), h7: new N(), h8: new R()
}

let rectBoard = [
  [new Rook(), new Knight(), new Bishop(), new Queen(), new King(), new Bishop(), new Knight(), new Rook()],
  [new Pawn(), new Pawn(),   new Pawn(),   new Pawn(),  new Pawn(), new Pawn(),   new Pawn(),   new Pawn()],
  [          ,             ,             ,            ,           ,             ,             ,           ],
  [          ,             ,             ,            ,           ,             ,             ,           ],
  [          ,             ,             ,            ,           ,             ,             ,           ],
  [          ,             ,             ,            ,           ,             ,             ,           ],
  [new Pawn(), new Pawn(),   new Pawn(),   new Pawn(),  new Pawn(), new Pawn(),   new Pawn(),   new Pawn()],
  [new Rook(), new Knight(), new Bishop(), new Queen(), new King(), new Bishop(), new Knight(), new Rook()],
]

