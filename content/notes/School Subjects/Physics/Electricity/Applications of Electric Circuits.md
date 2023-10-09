---
title: "Applications of Electric Circuits"
---
#physics #electricity 


> [!question] How can we model the nehaviour of real electrical components, such as light bulbs?
> Light bubls produce light by passing a current through the filament, causing it to heat up and glow. Resistance is dependant on temperature, so when the filament heats up, its resistance increases.

This produces the following I-V graph of an incandescent bulb.

```functionplot
---
title: Current & Potential Difference in Light Bulb
xLabel: V (V)
yLabel: I (A)
bounds: [0,10,0,4]
disableZoom: false
grid: true
---
f(x)=sqrt(x)
```

## [[Internal Resistance]]
How to determine voltage provided to the load resistor, $R_{L}$:

$$
V_{L} = \frac{R_{L}}{R_{i}+R_{L}}\times V_{in}
$$

## Diodes
![[Diode Diagram.png]]
A diode only allows the current to go through in one direction, which is the direction of the arrow. In the other direction, it blocks that.

Most diodes "switch on" at about 0.7V. Refer to the graph below.
![[Knee Voltage.png]]
