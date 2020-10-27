# MadLibs


# Instructions

Write a program that will ask the user for a series of words. Then plug them into your short story.

Be careful! **Make sure your prompts and variables match up with how you use them in your story.**


# Criteria/Constraints
*   Prompts
    *   Prompts match up with the order the words are used in the story.
    *   At least 8 inputs/variables
    *   Inputs should use a variety of parts of speech (noun, adjective, verb, etc.) and/or specific types of nouns (place, food, etc.)
*   Short story
    *   Has proper spelling and grammar
    *   Is at least 6 sentences/lines long.
*   Print statements
    *   At least one `print()` statement that outputs on multiple lines (ie. uses `"\n"`)
    *   At least one `print()` statement that concatenates (“adds”) two strings together (eg. `"Hello " + "world"`)
    *   At least one f-string or `.format()` that correctly inserts the variables.

# Sample Run

```
Let's play Silly Sentences!

Enter a name: Grace
Enter an adjective: stinky
Enter an adjective: blue
Enter an adverb: quietly
Enter a food: soup
Enter another food: bananas
Enter a noun: button
Enter a place: Paris
Enter a verb: jump

Grace was planning a dream vacation to Paris.
Grace was especially looking forward to trying the local
cuisine, including stinky soup and bananas.

Grace will have to practice the language quietly to
make it easier to jump with people.

Grace has a long list of sights to see, including the
button museum and the blue park.
```


# Sample Template

You should write your own prompt, but your output should be based on a template like this:

```
Let's play Silly Sentences!

[name] was planning a dream vacation to [place].
[name] was especially looking forward to trying the local
cuisine, including [adjective 1] [food 1] and [food 2].


[name] will have to practice the language [adverb] to
make it easier to [verb] with people.


[name] has a long list of sights to see, including the
[noun] museum and the [adjective 2] park.
```

# Benchmarks

As you work on this assignment, you may find it helpful to track your progress against the benchmarks listed below.  Follow the steps in order to ensure that you are writing clear, concise code that will meet all criteria.  Remember that the formatting of your output must be exact - be careful about the spacing and line breaks.


1. Using the `print()` function, output, "Let's play Silly Sentences!"  
2. Using the `input()` function, prompt the user to, `"Enter a name: "`, then assign and store their response to a variable.
3. Repeat benchmark 2 for the other 8 inputs that we need from the user:
   1. (eg. adjective, adjective, adverb, food, food, noun, place, and verb.)
4. Using a `print()` function, output a line such as:
   1. `"[name] was planning a dream vacation to [place]."` Replace `[name]` and `[place]` with the proper variables.
5. Repeat step 4 with the other 6 lines of output.
6. Double-check to make sure the output is formatted correctly - including spaces before and after variables and line spacing.
7. Run and test your program.
8. Debug and repeat step 7 as needed.