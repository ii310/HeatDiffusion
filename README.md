# Heat Diffusion: A Visual Physics Simulator
This project is an interactive real-time simulation of the 2D heat diffusion equation, a fundamental partial differential equation (PDE) that governs the distribution of temperature in a given medium over time.
At its core, it numerically solves the heat equation:
<p align="center">
  <img src="assets/heat_diffusion_equation.png" width="300" style="background:white; padding:10px;"/>
</p>
where:

𝑇 (𝑥, 𝑦, 𝑡) is the temperature at time 𝑇 and position (𝑥 ,𝑦)

A constant specific to a given fundamental terms, 𝛼 is the thermal diffusivity.

By implementing finite difference techniques to discretize the continuous equation, the simulation allows users to interact with the mouse to "transmit energy" (heat) into the system, simulating a localized heat source.


