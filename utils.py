def generate_random_ar_1(seed=1,
                          vertical_shift=10, 
                          size=1000,
                          interval = [-0.5, 0.5]
                          ):

    # Generate synthetic AR(p) series

    # Imports
    import numpy as np
    import pandas as pd
    from statsmodels.tsa.arima_process import ArmaProcess

    np.random.seed(seed)
    interval_low = interval[0]
    interval_high = interval[1]
    ar_params = np.array([1, np.random.uniform(interval_low, interval_high)])
    ma_params = np.array([1])
    ar_process = ArmaProcess(ar_params, ma_params)
    synthetic_ar_data = ar_process.generate_sample(nsample=size)
    synthetic_ar_series = pd.Series(synthetic_ar_data)
    synthetic_ar_series = synthetic_ar_series + vertical_shift

    return synthetic_ar_series

def generate_ar_p_series(p,
                       nsample=100,
                       interval = [-0.5, 0.5], 
                       seed=None):
    """
    Generates an AR(p) time series.

    Parameters:
    -----------
    p : int
        The order of the AR process (number of lags).
    nsample : int, optional
        The number of samples in the time series (default is 100).
    seed : int, optional
        The seed for the random number generator (default is None).

    Returns:
    --------
    pd.Series
        The generated AR(p) time series.
    """

    # Imports
    import numpy as np
    import pandas as pd 
    from statsmodels.tsa.arima_process import ArmaProcess

    # Check for seed
    if seed is not None:
        np.random.seed(seed)
    
    # Randomly generate AR coefficients between interval_low and interval_high
    interval_low = interval[0]
    interval_high = interval[1]
    ar_params = np.random.uniform(interval_low, interval_high, p)
    
    # Add 1 as the coefficient for y(t) term (which is conventionally set to 1)
    ar_params = np.concatenate(([1], -ar_params))
    
    # MA parameters are set to 1 for AR process
    ma_params = np.array([1])
    
    # Create ARMA process with AR(p) and MA(0)
    ar_process = ArmaProcess(ar_params, ma_params)
    
    # Generate the time series
    synthetic_ar_data = ar_process.generate_sample(nsample=nsample)
    synthetic_ar_series = pd.Series(synthetic_ar_data)
    
    return synthetic_ar_series

def generate_shifts(y, n_series=1):

    return 0
