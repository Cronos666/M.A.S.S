# M.A.S.S. (Modeling and Analysing of Spacetime Simulation)

## **Python** physics engine for simulating gravitational forces using **Euler Integration**.
___

## Requirements

 * Python 3.x
 * NumPy
 * Matplotlib

```
pip instal numpy matplotlib
```
___
## Usage
 Script run via terminal. An **csv** file with initial conditions must be provided.

```
python mass.py -f <filename.csv> [options]
```
Avabile arguments can be seen by runing script wiht `-h` flag.

```
python mass.py -h
```
___
## Engine 
Physics engine lies in `balls.py` and use simple vector math for optimalization purposes.

 * $\vec{a} = \vec{F_{net}}/m$
 2. $\vec{v} = \vec{v_{0}} + \vec{a} dt$
 3. $\vec{r} = \vec{r_{0}} + \vec{v} dt$
 4. $ \vec{F_{net}} = \sum -G \frac{m_{j}   m_{i}}{|r_{ij}|^{3}} \vec{r_{ij}}$
q