## Purpose ##

Scalepack outputs only systematic absences, and not the rest of reflections. The best way to identify screw axis is probably to look at the whole set of reflections, so that you can compare systematic absences with present reflections. Another relevant situation is when you need to identify which axis are screw in, say, P2221. You have to run scalepack at least twice to do it.

So, the general rule is:

1. Run scalepack in the spacegroup with no screw axis (e.g. P2, P222, I422, etc).

2. Use the following python script to extract specific reflection types.

## Syntax ##

```
./gethkl <file-name> 'absence code'
```

Absence code should be in quotes but has a human(e) format, such as (0,0,l), (0,2k,0), etc. Other examples are (h,0,0), (h,1,2), (h,2k,4) and so on.

## Alternatives ##

Program pointless helps with identification of the space group.  hklview viewer in CCP4 is helpful in visualizing intensities.  Both would require that the scalepack output is converted to MTZ format though.