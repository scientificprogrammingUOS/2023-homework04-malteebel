import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if isinstance(loc, (int, float)) and isinstance(scale, (int, float)) and isinstance(lower_bound, (int, float)) and isinstance(upper_bound, (int, float)):
        if lower_bound < upper_bound:
        
            dis = np.random.normal(loc=loc, scale=scale, size=100)
            mask = (dis > lower_bound) & (dis < upper_bound)
            bounded_dis = dis[mask]
            mean = np.mean(bounded_dis)
            std = np.std(bounded_dis)

            return (mean, std)
    
        else:
            raise ValueError("lower_bound has to be lower then upper_bould")
    else:
        raise TypeError("One of the inputs is not a float or int")

if __name__ == "__main__":
    # use this for your own testing!

    pass
