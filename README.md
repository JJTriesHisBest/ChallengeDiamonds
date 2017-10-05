# Challenge 4 - Diamonds

I drew some of these out from A - C and counted the number of letters in each diamond. Out of curiosity I then googled that sequence 1, 5, 13 and the first wiki result was **Centered square number**. Pretty cool stuff!

I generated the letters based on their unicode values, and took advantage of the shape's symmetry by using reverse slices to create the rest of the diamond from the top left section.

I haven't added a bound check yet, so anything with a unicode value less than A won't print a diamond. A bonus of this is you can print a diamond for the character `_` and you'll get a happy face in the centre.

If we did want this strictly to work for [A-Z], we could also use a hash table approach should memory allow.
## Usage
```
python create_diamond.py [A-Z]
```
