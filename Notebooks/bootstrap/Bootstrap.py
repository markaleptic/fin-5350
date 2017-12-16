import numpy as np


def stationary_bootstrap(data_vec_to_resapmle, q = 0.1, replications = 1000):
    """
    Algorithm to implement stationary boostrap resampling technique as described by Politis and Romano (1994), 
    Appendeix C of Sullivan et all (1999), and most specifically from Appendex 1 of Alizadeh and Nomikos (2008).
    Inputs:
        data_vec_to_resapmle    Original data set used for resampling
        q                       Probability that the next observation in the resampled array is randomly
                                selected from the original observations
        
        replications            Number of resampled arrays to return
    Return:
        1,000 (or however many designated) numpy array's resampled from data_vec_to_resapmle
    """

    vec_len = len(data_vec_to_resapmle)
    end_of_vec_index_adj = vec_len - 1
    resample_vec = np.zeros(shape=(replications, vec_len), dtype=float)
 
    for i in range(replications):
        index_vec = np.zeros(vec_len, dtype=int)
        starting_pos = np.random.randint(0, vec_len, dtype=int)
        index_vec[0] = starting_pos

        std_unifs = np.random.normal(0.0, 1.0, vec_len)

        for j in range(1, vec_len):
            if std_unifs[j] < q:
                index_vec[j] = np.random.randint(0, vec_len, dtype=int)
            else:
                if index_vec[j - 1] == end_of_vec_index_adj:
                    index_vec[j] = 0
                else:
                    index_vec[j] = index_vec[j - 1] + 1

        resample_vec[i] = data_vec_to_resapmle[index_vec]
        index_vec = np.zeros(vec_len, dtype=int)

    return resample_vec
