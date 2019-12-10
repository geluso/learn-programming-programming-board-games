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
* **null:** The `null` data type represents the absence of something.

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

## Variables
Variables are used to store data. Programs wouldn't be very useful if we
weren't keeping track of all our data!

Variables have names and values. 

Here's a small program representing someone ordering a meal. We use variables
to store the price of each item. We're able to calculate the subtotal and the
overall total by referring to the variables. Finally, we're able to print out
the values of the variables.

```python
food_price = 9.99
drink_price = 1.29

sub_total = food_price + drink_price

tax_rate = .08
total = sub_total + sub_total * tax_rate

print("Subtotal:", sub_total)
print("   Total:", total)
```

## Attacking Misconceptions
Here's something that confused me when I first tried to teach myself
programming. Do not think of variables as anything algebraic. The equality sign
`=` does not mean that things are equal to each other, like in math. The
equality sign here in programming means that a variable will store the value of
some data.

This program outputs "1". The variable `x` is first set to zero. Then `x` is
set to take on the value of "x plus 1" and then it is printed out.

```
x = 0
x = x + 1
console.log(x)
```

Specifically, the line that confused me in the past was `x = x + 1`. When
I looked at this line I really thought it was an algebraic expression.
I rewrote it as `x - 1 = x` trying to solve for `x`. It made no sense to me!

It was hard for me to understand that the program wasn't using the `=` equals
sign like in algebra because I didn't have a way to run the program. (I was
learning this from a site called W3Schools in a language called PHP. PHP is not
as an interactive programming language as JavaScript it!)

There's two good lessons to learn here:

1. Programmers get tripped up on stupid stuff! Get in the habit of asking for
   help when you're stuck.
2. Don't take assumptions for granted! Find ways to prove to yourself that your
   program is doing (or not doing) what you think it is doing.

One thing I really like about programming is it is so accessible. Programming
makes it very easy to build things and test out ideas. Unlike an architect
ideas for programming aren't bound by brick and mortar. It's awesome to be able
to build things mostly unfettered from material goods.

## Copy-by-Value vs Copy-by-Reference
Here's one thing about variables that might trip you up.

```
cows = 99
birds = 240

cow_bells = cows
beaks = birds

cow_bells = cows * 2

console.log('Cow Stuff:', cows, cow_bells)
console.log('Bird Stuff:', birds, beaks)
```

What's the output?

```
Cow Stuff: 99 198
Bird Stuff: 240 240
```

When the `cow_bells` and `beaks` variables are created they **copy-by-value**
stored in the `cows` and `birds` variables. When we write `cow_bells = cows`
we're not saying that `cow_bells` refers to the same things as the `cows`
variable. The program copies the **value** of what's stored in the `cows`
variable. Later, when we write `cow_bells = cows * 2` we see that the `cows`
variable is still `99` when we print it.

Here's another example:

```js
colors1 = ['orange', 'red', 'green', 'blue']
colors2 = colors1

colors2[0] = 'purple'

console.log('Colors #1', colors1)
console.log('Colors #2', colors2)
```

The output is:

```
Colors #1 ['purple', 'red', 'green', 'blue']
Colors #2 ['purple', 'red', 'green', 'blue']
```

In the last example we copied the value of a variable storing an integer and
put it in a new variable. We said we copied the variable by **value**. The new
`cow_bells` variable did not refer back to the `cows` variable. When we
multipled `cow_bells` by two the value in `cows` was unaffected. 

In the array example we see the opposite effect. We set `colors2 = colors1`,
then overwrite the array spot in the front at index `0` with `colors2[0]
= 'pink'`. Finally, when they're printed out we see `colors1` was changed as
well!

This is called **copy-by-reference**. Instead of copying the array like in the
integer example the variable copies a **reference** to the array. Both
variables refer to the same array.

Why are their two different ways to copy variables?

It's actually nice. It's efficient. It is an optimization. Integers are small.
The data taken to represent an integer doesn't take up much room. Arrays on the
other hand can be large. Very very large! If an array had a hundred, a thousand
(heck, even 10 things) it would be an expensive operation to copy the whole
array from one variable to another. Instead of copying the entire **value** of
the array the program just copies a **reference** to the array.

Think of the variable as storing a street address to a house.

## Functions


## Parameters


## Return Statements
