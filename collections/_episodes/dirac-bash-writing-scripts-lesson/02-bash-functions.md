---
title: "Functions in Bash"
slug: dirac-bash-writing-scripts-functions-bash
teaching: 25
exercises: 10
questions:
- What is a function?
- Why use a function?
- Where do I write a function?
- When should I use a function?
- How do I write a function?
objectives:
- Understand the use case for a function.
- Write a simple function.
- Write a function that accepts inputs.
- Write a function that returns an output.
- Refactor a piece of code to use functions.
keypoints:
- Functions reduce code duplication.
- Functions make testing the behaviour of code easier by isolating tasks.
- Functions make abstracting tasks easier.
---

## What is a function and why use one?
This is a function:

```
function hello_world {
  echo Hello World from teh function 'hello_world'!
}
```
{: .language-bash}

or with a different syntax,
```
hello_world () {
  echo Hello World from teh function 'hello_world'!
}
```
{: .language-bash}

Both of these blocks define a function that when used prints ```Hello World from teh function 'hello_world'!``` the following to the terminal.

Try it out now by copying one of the functions into the command line hit return to save it. Then run it by typing ```hello_world``` and pressing return.

```
Hello World from teh function 'hello_world'!
```
{: .output}

You may note that this is quite similar to running other commands we have been using in the terminal like ```pwd``` or
```ls```. These are both functions that have been predefined for us because they are useful tools that we are likely to
want to use multiple times.

We use functions to provide utilities that we want to use quickly and repeatedly, the above ```hello_world``` function
is actually a bad example in this regard. Whilst we can now print the string
```Hello World from teh function 'hello_world'!``` somewhat more quickly, is is unlikely that this is something we will
frequently want to do. On the other hand ```pwd``` is an extremely useful tool that we will use frequently.

## Where do I write a function and when should I use them?
In the above example we wrote and used a function directly on the command line. Whilst there is nothing wrong with this,
it doesn't give us any options to edit the function without completely rewriting it. For example, in the above function
there was a typo and we put ```teh``` and not ```the``` to fix this we need to write the whole function again and update
it in the command line.

```
function hello_world {
  echo Hello World from the function 'hello_world'!
}
```
{: .languaage-bash}

```
Hello World from the function 'hello_world'!
```
{: .output}

It's therefore much more useful to define and use your functions inside a script where they can be edited and
used quickly.

Using the following command we will make a script to work on some functions. Then use chmod so we can run it.
```
touch my_functions.sh
chmod +x my_functions.sh
```
{: .language-bash}

You can then edit this script in which ever text editor we choose. For the sake of consistency let's use Nano
```
nano my_functions.sh
```
{: .language-bash}

Let's start by using the following script that checks the time 100 times but only prints it if the seconds are a
multiple of 3:

```
#!/bin/bash

# Start a loop
while [ $i -le 100 ]
do
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, minutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
   # use the moduli operator to check if the number is divisible by 3
   if ((${time_arr[2]} % 3 == 0));
   then
      # if the number of seconds is divisible by 3 then print the time to console
      echo $time_var
   fi
   # wait one second
   sleep 1
   ((i++))
done
```
{: .language-bash}

This script has many lines and a decent amount of complexity and is inflexible. So we may want to break it down
We can use functions to address this. Along the way we will learn about the way
functions return data and how to instruct a function to have different behaviours.

## How can I use the result of my function?

Let's start by considering a function that reads the current time and returns the time array -- the first four lines of
the while loop.
```
function get_time_arr {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, minutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
   echo ${time_arr[@]}
}
```
{: .language-bash}

If you have experience with other programing languages then you may be hesitant about the way this function looks. Most
languages have some kind of return to end a function to return the result. However, in bash the return is only used to
return the status of the function, a 0 indicates success and anything else indicates failure. To check the status of the
last run function one can use a special variable ```$?```. To get the result of this function we are using
'command substitution.' The final line of the function prints the result of the function which can be collected.

Let's take an aside to look at this behaviour.

Copy and paste the above function to the terminal then run.

```
get_time_arr

echo $?
```
{: .language-bash}

The function prints the time then the function result which should be ```0```. But this isn't particularly useful we
want to be able to collect and use the output. To do this we collect the output of the function in a variable.

```
time_arr=$( get_time_arr )
echo $?
echo $time_arr
```
{: .language-bash}

Here we have assigned the output to the variable ```time_arr``` then printed it at our convince. We will look at other
ways of returning variables later.

For now lets get back to our script and replace the first few lines with the function we just wrote.

```
#!/bin/bash

# Define a function to get a time and split it into an array
function get_time_arr {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, miniutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
   # return the array
   echo $time_arr
}

# Start a loop
while [ $i -le 100 ]
do
   # Run the funtion to get the current time as an array are assign the result to time_arr
   time_arr=$( get_time_arr )

   # use the moduli operator to check if the number is divisible by 3
   if ((${time_arr[2]} % 3 == 0));
   then
      # if the number of seconds is divisible by 3 then print the time to console
      echo ${time_arr[@]}
   fi
   # wait one second
   sleep 1
   ((i++))
done
```
{: .language-bash}

Unfortunately, whilst before we had access to the variables ```time_var``` and ```time_arr```, we now we only have
```time_arr``` as using 'command substitution' we can only return a single argument. So now we will upgrade the
```get_time_array``` to be able to assign multiple values.

```
#!/bin/bash

# Define a function to get a time and split it into an array
function get_time_vars {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, miniutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
}
```
{: .language-bash}

To use the function above we need to use two variables that will store the results

```
time_var='time_var'
time_arr='time_arr'
get_time_vars
# check the return status of the function
echo $?
# print the variables to the console
echo $time_var
echo ${time_arr[*]}
```
{: .language-bash}

We can use this updated function to restructure our script like so:

```
#!/bin/bash

function get_time_vars {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, miniutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
}

# Initilise some variables
i=0
time_var='time_var'
time_arr='time_arr'
# Start a loop
while [[ $i -le 100 ]]; do
   # Run the funtion to get the current time as an array
   get_time_vars
   # use the moduli operator to check if the number is divisible by 3 n.b. we are using '10#' to let bash know seconds '01, 02, 03...' are in base 10
   seconds=10#${time_arr[2]}
   floor_val=$(( seconds % 3 ))
   # if the number of seconds is divisible by 3 then print the time to console
   if [ $floor_val -eq 0 ]; then
      echo $time_var
   fi
   # wait one second
   sleep 1
   (( i++ ))
done
```
{: .language-bash}

We should note here that we don't return the variables from the function, we let the function edit global variables. This
means the function is less useful than it could be, as we have to know the names of the variables beforehand. But it is
necessary for returning more than one variable (where one of the variables isn't a status code). The above function is
also dangerous, it can edit variables without the user being aware. This concept is called [variable scope](
   https://en.wikipedia.org/wiki/Scope_(computer_science)) and its worth investigating in more detail.

Let's consider a simple example, run the three following codes and predict the outcome of each before you do:
> ## Predict the outcome
> Firstly we assign and read out two variables.
> ```
> var_a = 'I am global var_a'
> var_b = 'I am global var_b'
>
> echo $var_a
> echo $var_b
> ```
> {: .language-bash}
>
> ```
> I am global var_a
> I am global var_b
> ```
> {: .output}
>
> Now we introduce a function like the one above that uses these variable names, what should the output be now?
> ```
> function i_break_things {
> var_a = 'I am var_a inside a function'
> var_b = 'I am var_b inside a function'
> echo $var_a
> echo $var_b
> }
>
> var_a = 'I am global var_a'
> var_b = 'I am global var_b'
>
> echo $var_a
> echo $var_b
>
> i_break_things
>
> echo $var_a
> echo $var_b
> ```
> {: .language-bash}
>
> > ## Solution
> > ```
> > I am global var_a
> > I am global var_b
> > I am var_a inside a function
> > I am var_b inside a function
> > I am var_a inside a function
> > I am var_b inside a function
> > ```
> > {: .output}
> >
> > The function has updated the variables in this example and the function we created above it seems intentional but
> > what if your code contained hundreds of lines or the function got included in a path there would be no way to
> > predict what any given output should be!
> {: .solution}
>
> This time we add the local keyword to `var_b`. Have a guess how this might change the result...
>
> ```
> function i_break_fewer_things {
> var_a = 'I am var_a inside a function'
> local var_b = 'I am local var_b'
> echo $var_a
> echo $var_b
> }
>
> var_a = 'I am global var_a'
> var_b = 'I am global var_b'
>
> echo $var_a
> echo $var_b
>
> i_break_fewer_things
>
> echo $var_a
> echo $var_b
> ```
> {: .language-bash}
> > ## Solution
> > ```
> > I am global var_a
> > I am global var_b
> > I am var_a inside a function
> > I am local var_b
> > I am var_a inside a function
> > I am global var_b
> > ```
> > {: .output}
> >
> > The inclusion of the local keyword has changed the scope of the variable `var_b` now it is local to the function
> > and the variable outside the function is left unchanged. The words here 'global' and 'local' are the names of the
> > scopes. The 'global' scope is accessible from anywhere in the script including inside functions
> {: .solution}
{: .challenge}

## How can I tell my function what do?

Let's gert back to our script. The stages are currently:
- Initilise variables
- Start a loop
  - Use our function 'get_time_vars' to query the time and date and assign them to the global variables time_var and time_arr
  - Check if the number of seconds is divisible by three.
    - true: print the date and time
    - false: do nothing
  - sleep for one second

```
#!/bin/bash

function get_time_vars {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, miniutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
}

# Initilise some variables
i=0
time_var='time_var'
time_arr='time_arr'
# Start a loop
while [[ $i -le 100 ]]; do
   # Run the funtion to get the current time as an array
   get_time_vars
   # use the moduli operator to check if the number is divisible by 3 n.b. we are using '10#' to let bash know seconds '01, 02, 03...' are in base 10
   seconds=10#${time_arr[2]}
   floor_val=$(( seconds % 3 ))
   # if the number of seconds is divisible by 3 then print the time to console
   if [ $floor_val -eq 0 ]; then
      echo $time_var
   fi
   # wait one second
   sleep 1
   (( i++ ))
done
```
{: .language-bash}

> ## Try modifying the function
> We may want to change the divisor so that it prints on multiples of five. How would you make this change?
> > ## Solution
> > We need to change the line:
> > ```
> > floor_val=$(( seconds % 3 ))
> > ```
> > {: .language-bash}
> >
> > to this:
> > ```
> > floor_val=$(( seconds % 5 ))
> > ```
> > {: .language-bash}
> >
> {: .solution}
>
> Now we want to print on multiples of seven. How would you make this change?
>
> > ## Solution
> > We need to change the line:
> > ```
> > floor_val=$(( seconds % 5 ))
> > ```
> > {: .language-bash}
> >
> > to this:
> > ```
> > floor_val=$(( seconds % 7 ))
> > ```
> > {: .language-bash}
> >
> {: .solution}
>
{: .challenge}

We can see that by working this way to change something simple, a user is required to edit a line in the middle of the
code. Let's move the floor operation to a function and pass it a variable instead.

```
#!/bin/bash

function get_time_vars {
   # get the time
   time_var=$(date "+%H:%M:%S")
   # split the time into hours, miniutes, and seconds
   IFS=':' read -ra time_arr <<< "$time_var"
}

function check_multiple {
   #  we use '10#' to let bash know seconds '01, 02, 03...' are in base 10
   local seconds=10#${time_arr[2]}
   # use the moduli operator to check if the number is divisible by 3 n.b.
   local floor_val=$(( seconds % $1 ))
   echo $floor_val
}

# Initilise some variables
divisor=5
i=0
time_var='time_var'
time_arr='time_arr'
# Start a loop
while [[ $i -le 100 ]]; do
   # Run the funtion to get the current time as an array
   get_time_vars
   # check if the number is a multiple of divisor
   do_i_print=$( check_multiple $divisor )

   # if the number was a multiple then print the time to console
   if [ $do_i_print -eq 0 ]; then
      echo $time_var
   fi

   # wait one second
   sleep 1
   (( i++ ))
done
```
{: .language-bash}

> ## Check your understanding
> The changes made to the script have a few advantages. It allows a variable to be set and used by the new function
> check_multiple. how is it different to our scoped variables, why might this be better in this instance?
>
> > ## Solution
> > The variable `divisor` is passed to the function and accessed using `$1`, as we haven't used a variable in the global
> > scope we could use this to set two divisor variables and use them without needing to change anything. More on this
> later...
> >
> {: .solution}
>
> But how has the code been made more readable?
>
> > ## Solution
> > Defining the variable seconds as a number in base 10 was only necessary because we wanted to use the moduli operator
> > we can move it into the function and give it a local scope so that it de-clutters the while loop making the loop
> > appear simpler and more closely follow the steps we defined earlier.
> >
> {: .solution}
>
{: .challenge}

## What can I do with a function now?

We've shown how a function is defined, where and why functions are written, how to use the result of a function, the
affect of variable scope, and how to pass variables to a function. There is a common coding challenge called fizzbuzz,
where numbers are looped over. If the number is a multiple of 3 "fizz" is printed, if it is a multiple
of 5 "buzz" is printed, and if it is a multiple of both "fizzbuzz" is printed. The pseudocode logic for this is like this:

- Loop over integers i from 1 to n
  - check if i is a multiple of 3 assign result to a
  - check if i is a multiple of 5 assign result to b
  - check if a and b are both true
    - if true:
      - print fizzbuzz
    - if false:
      - check if a is true:
        - if true: print fizz
      - else check if b is true:
        - if true: print buzz
      - else:
        - print i

We will make one alteration that the user calling the function fizzbuzz should be able to specify the two divisors and
number at which to stop at.

If you want a stretch challenge try to write this from scratch now using functions where possible to simplify the
script. Otherwise, just reveal the answer and move onto the next question.

> ## Fizzbuzz
> ```
> function check_multiple {
>    # use the moduli operator to check if the first argument is a multiple of the second
>    local floor_val=$(( $1 % $2 ))
>    echo $floor_val
> }
>
> function fizzbuzz {
> # this function takes three arguments in the following order, divisor a, divisor b, stop
> i = 1
> # loop while i is less than the 3rd argument
> while [[ $i -le $3 ]]; do
>   # check if i is a multiple of the first and second argument
>   a = $( check_multiple $i $1 )
>   b = $( check_multiple $i $2 )
>
>   # add a and b (if both are zero then fum is zero and thats a fizzbuzz)
>   a_and_b = $(( $a + $b ))
>
>   # Check the multiple output being careful to use else correctly so to not print the number if it is a multiple.
>   if [ $a_and_b -eq 0 ]; then
>       echo fizzbuzz
>   else
>     if [ $b -eq 0 ]; then
>       echo fizz
>     elif [ $a -eq 0 ]; then
>       echo buzz
>     else
>       echo $i
>     fi
>   fi
>   # increment i
>   (( i ++ ))
> done
> }
>
> # run classic fizzbuzz to 100
> fizzbuzz 3 5 100
> ```
> {: .language-bash}
>
> We've created the function fizzbuzz that takes three arguments that define the two number to check for multiples of
> and the number to stop at. The function check_multiple uses command substitution to return the moduli of the current
> loop value, by letting this function take arguments we can avoid writing separate functions for each input to check.
>
{: .solution}

Now you have seen the way functions can be used in bash try these exorcises to apply what you have learnt.

> ## Exercises
> Thinking about the script that prints the time when seconds are a multiple of three and fizzbuzz example above write
> some pseudocode for a function that prints the time (not more than once a second) 100 times unless the seconds are a
> multiple of one or both of the two input values, in which case it should print fizz, buzz or fizzbuzz for both.
>
> > ## Solution
> > - Loop over the values 1 to 100
> >   - Get the time, strip the seconds
> >   - Check if time is a multiple of either of the inputs (call them a and b)
> >   - Multiple of both?
> >     - true
> >       - print fizzbuzz
> >     - false
> >       - multiple of a
> >         - true
> >           - print fizz
> >         - false
> >           - multiple of b
> >             - print buzz
> >          - false
> >             - print time
> >
> {: .solution}
>
> Turn your pseudocode into an actual function that uses the time to play fizzbuzz.
>
> > ## Solution
> >```
> >#!/bin/bash
> >
> ># Global variables for function returns
> >time_var='time_var'
> >time_arr='time_arr'
> >
> >function get_time_vars {
> >  # get the time
> >  time_var=$(date "+%H:%M:%S")
> >  # split the time into hours, miniutes, and seconds
> >  IFS=':' read -ra time_arr <<< "$time_var"
> >}
> >
> >function check_multiple {
> >  #  we use '10#' to let bash know seconds '01, 02, 03...' are in base 10
> >  local seconds=10#${time_arr[2]}
> >  # use the moduli operator to check if the number is divisible by 3 n.b.
> >  local floor_val=$(( seconds % $1 ))
> >  echo $floor_val
> >}
> >
> >function date_fizzbuzz {
> >  # this function takes three arguments in the following order, divisor a, divisor b
> >  local i=0
> >  while [[ $i -le 100 ]]; do
> >    # Run the funtion to get the current time as an array
> >    get_time_vars
> >
> >    # check if the number is a multiple of divisor
> >    res_a=$( check_multiple $1 )
> >    res_b=$( check_multiple $2 )
> >    # add to combine both, using moduli zero is true so if sum is 0 then both were 0
> >    res_ab=$(( $res_a + $res_b ))
> >
> >
> >    if [ $res_ab -eq 0 ]; then
> >      echo fizzbuzz
> >    else
> >      if [ $res_a -eq 0 ]; then
> >        echo fizz
> >      elif [ $res_b -eq 0 ]; then
> >        echo buzz
> >      else
> >        echo $time_var
> >      fi
> >    fi
> >
> >    # wait one second
> >    sleep 1
> >    (( i++ ))
> >  done
> > }
> >
> > # Run the function with classic fizzbuzz multiples
> > date_fizzbuzz 3 5
> > ```
> > {: .language-bash}
> {: .solution}
>
{: .challenge}

That's all we have to say about bash functions for now. This isn't an extensive tutorial, but it should give you a
*functional* understanding of how they work. If you want more practice working on functions, try modifying the
date_fizzbuzz to do other more interesting things.
