# Output, Data, Variables and Functions
If we're writing computer programs we're going to need some way to observe
them. As we begin we'll first start making programs that print out text. Using
just text is actually a totally fun medium to create programs in. Its fun to
figure out how to make programs look good just printing out letters, numbers,
and symbols on a grid.

The book covers 2D graphics in a later chapter. This book does not cover
anything about 3D graphics as they are entirely complex!

## Print Statements
Here's what a print statement looks like in various languages. A print
statement prints text inside quotation marks.

| Language   | Print Statement                      |
|============|======================================|
| Ruby       | puts "Hello world!"                  |
| Python     | print("Hello world!")                |
| Java       | System.out.println("Hello world!");  |
| JavaScript | console.log("Hello world!");         |

## Data
Most programming languages support a small collection of fundamental
"primitive" data types. These are the building blocks of all the programs we
create.

Everything is made up of from these primitive data types. Look at the different
data types below and think about what different data types you would need to
keep track of a game of Chess.

Here's several common primitive data types:

* **Booleans:** a piece of data that represents only either the value `true` or
  `false`
* **Integers:** whole numbers like 1, 2, 3, 4, 0, -42.
* **Decimals:** decimal numbers (often also called "floats") like .5, .999,
  -20.333
* **Characters:** single letters like a, b, c.

In addition to the primitive data types programming languages often have these
other common built-in data types:

**Strings:** We call text Strings because they are a "string" of characters,
multiple characters all in a row. A String can be text of any length and
contain anything you would expect in text: letters, numbers, punctuation and
symbols.

**Arrays:** An array stores a list of things.

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
["cat", "dog", "gerbil", "parakeet"]
```

**Objects/Dictionaries/Maps:** These go by so many different names it is hard
to choose one! No matter the name this data type stores a collection of
key-value pairs. Whereas an array stores things in a certain order data in
a dictionary stores things according to it's key.

```
{city: "Seattle", state: "Washington", population: 724745}
```


## Modelling Chess
So, what would you need for Cheese? Sorry, Chess.

First of all: there are SO MANY ways to represent a game. There's not going to
be any one perfect way to capture the state of a Chess game, or any other game,
or any other program. Refer to the short topic in the Personal Philosophies
section, [Rightness vs Ramifications]().

Here's one way to store all the data of a Chess game. You can use one String to
make a big grid of the whole board and manually place a letter at the locations
for each piece. You can even represent "black" and "white" using different
uppercase and lowercase letters!

```
RNBKQBNR
PPPPPPPP
........
........
........
........
rnbkqbnr
pppppppp
```

It's totally possible to store a game like this. Actually it's a very good way
to begin serializing a game to save it (see [Serialization]()).


## Variables


## Functions


## Parameters


## Return Statements
