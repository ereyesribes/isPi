
# What is this?

I've seen there's a lot of people wondering how to detect if their script is running on RPi,
in fact one of those people was me.

Seeing the confusion and the variety of responses given in StackOverflow I have decided to
create this tiny library and share it with the world, because it not only gives accurate
results but it also allows you to use "isPi()" instead of some ugly code that no one really
understands at first sight.

Yay for syntactic sugar.

## So how do I use it


```
  import * from isPi.isPi

  print isPi() # True/False
  print piModel() # String containing the Model of the Pi or False if not running on a Pi.
```

That's it guys! Hope you find it useful!

## If you liked this consider buying me a coffee!

<a href='https://pledgie.com/campaigns/33403'><img alt='Click here to lend your support to: isPi and make a donation at pledgie.com !' src='https://pledgie.com/campaigns/33403.png?skin_name=chrome' border='0' ></a>
