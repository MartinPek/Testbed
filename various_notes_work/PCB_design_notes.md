
* Group related components together with the required test points
* place adjacent and related parts in the same orientation 
* use wider Traces for VCC unless using a plane for it, keep planes centered and symmetrical if possible.
* higher power lines need to be bigger https://www.4pcb.com/trace-width-calculator.html
* seperate analog and digital, dont run analog traces over digital mass
* putting capacitors near vin and vout pins of buck
* dont run return signals parrallel to digital
* daisy chains create noise
* reduce right angles traces (this is due to manufacturing reasons and possible track length and not EMI unlike often claimed)
* tracks between pads of components are to be avoided particualarily crystals or oscillators (atleast not the layer directly below)
* parts like voltage converters should be placed away from the center of the board 
* consider solder migration when making SMD solder pads
* Star topology > Single Poing > Multipoint (daisy chain) see TI guide fig. 6
* avoid loops in ground or powernets
* route signals away from each other 

### Hacks
* ground vias between as possible shielding from analog


### watchlist
* https://youtu.be/gHF5JyJF-N4
* official TI guide on PCB design https://www.ti.com/lit/an/szza009/szza009.pdf?ts=1642661339384&ref_url=https%253A%252F%252Fwww.google.de%252F
* https://www.youtube.com/c/RobertFeranec/videos (beginner and emi videos)