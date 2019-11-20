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

g++ -g /home/gg/Var_/test/test_ptf_mc_var.cpp -o /home/gg/Var_/test/test_ptf_mc_var -I /home/gg/Var_/eigen-eigen-323c052e1731 -I /home/gg/Var_/include /home/gg/Var_/src/compute_returns_eigen.cpp /home/gg/Var_/src/instrument.cpp /home/gg/Var_/src/path.cpp /home/gg/Var_/src/pca.cpp /home/gg/Var_/src/portfolio.cpp /home/gg/Var_/src/ptf_var.cpp /home/gg/Var_/src/rng.cpp /home/gg/Var_/src/var_model.cpp
