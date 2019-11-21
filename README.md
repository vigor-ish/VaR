# VaR, CVaR  - Value at Risk, Expected shortfall 


This small project is about computing value at risk using different methods such as :

- Exponentially weighted moving average

- GARCH

- Historically simulation

- Monte Carlo simulation

- Exteme value theory

- Copulas

The computation have been backtested against several equity indices and foreign exchanges.

The code is written in C++ and relies on Boost and Eigen libraries. It has been compiled using GNU compiler.

g++ -g ./test/test_ptf_mc_var.cpp -o ./test/test_ptf_mc_var -I ./eigen-eigen-323c052e1731 -I ./include ./src/compute_returns_eigen.cpp ./src/instrument.cpp ./src/path.cpp ./src/pca.cpp ./src/portfolio.cpp ./src/ptf_var.cpp ./src/rng.cpp ./src/var_model.cpp
